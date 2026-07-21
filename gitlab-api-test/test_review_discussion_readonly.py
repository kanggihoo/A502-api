"""리뷰·토론 맥락 집계용 읽기 전용 GitLab API 검증.

통합 워크스페이스가 "리뷰 대기·토론·피드백" 맥락을 모으는 용도로 쓸 MR 단위
엔드포인트를 실제 토큰으로 검증한다. 이 스크립트는 어떤 리소스도
생성/수정/삭제하지 않는다.

검증 항목 (전부 프로젝트 스코프 /projects/{id}/...):
  R-1 GET /projects/{id}/merge_requests?state=opened                대상 MR iid 확보
  R-2 GET /projects/{id}/merge_requests/{iid}/participants          MR 참여자
  R-3 GET /projects/{id}/merge_requests/{iid}/reviewers             MR 리뷰어
  R-4 GET /projects/{id}/merge_requests/{iid}/approvals             MR 승인 상태(요약)
  R-5 GET /projects/{id}/merge_requests/{iid}/discussions           MR 토론 스레드
  R-6 GET /projects/{id}/merge_requests/{iid}/notes                 MR 댓글

설계 원칙 (P0/P1 검증으로 확정):
- 항상 프로젝트 스코프 엔드포인트 사용. scope=all 금지. 타팀 데이터 노출 방지.
- 데이터가 비어 있어도(0개) API 정상 응답이면 ok=True. "지금 데이터가 없을 뿐" 인지와
  "API가 막혀 있는지"를 구분하는 것이 목적.

문서상 주의사항 (api-docs/gitlab_rest_defuddle_markdown/):
- participants/reviewers/approvals/discussions/notes 모두 MR IID(프로젝트 내 번호) 사용.
  문서 일부는 noteable_id 라 표기하지만 IID로 동작한다.
- approvals(요약: approved_by) 와 approval_state(상세: rules) 가 반대 이름 주의.
  이 스크립트는 요약형인 /approvals 만 검증한다.
- reviewers 응답은 {user:{...}, state, created_at} 중첩 구조 (participants 와 다름).

대상 MR이 없는 경우:
- R-2~R-6 을 모두 "대상 MR 없음 — 스킵" ok=False CheckResult 로 기록.
- 조기 return 대신 개별 실패를 남겨 "어느 항목이 스킵됐는지"를 리포트에 명시.
- MR 이 있는 프로젝트로 GITLAB_TEST_PROJECT_ID 를 바꾸면 정상 동작.

실행:  uv run python test_review_discussion_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from gitlab_client import (
    CheckResult,
    Config,
    GitLabClient,
    Report,
    load_config,
)


def _skip_check(name: str, endpoint: str, reason: str) -> CheckResult:
    """대상 MR이 없을 때 일관된 "스킵" CheckResult 를 만든다."""
    return CheckResult(name, endpoint, ok=False, status=None,
                       summary=reason, web_url=None, sample=None,
                       error=None, elapsed_ms=0)


def main() -> None:
    cfg: Config = load_config()
    client = GitLabClient(cfg)
    report = Report(title="리뷰·토론 읽기 전용 API 검증", base_url=cfg.base_url)

    print(f"GitLab: {cfg.base_url}")
    print(f"대상 프로젝트: {cfg.project_id or '(자동 탐지)'}")
    print("-" * 60)

    # 대상 프로젝트 확정 (P0/P1 과 동일 로직).
    detect_resp, project_pid = client.resolve_project()
    if not project_pid:
        report.add(CheckResult(
            "대상 프로젝트 확정", "GET /projects?membership=true", False, None,
            "대상 프로젝트를 찾을 수 없음", None, None,
            detect_resp.error or "프로젝트 미확정"))
        _finalize(report)
        return

    base = f"/projects/{project_pid}"
    print(f"대상 확정: {project_pid}\n")

    # ========================================================================
    # R-1 대상 MR 확보 (opened 우선, 없으면 all 에서 최근 MR 로 폴백)
    # ========================================================================
    # 대시보드의 "리뷰 대기" 집계 목적상 opened 가 맞다. 단, opened MR 이 없는
    # 프로젝트에서도 이 스크립트가 participants/approvals/discussions/notes API 의
    # 동작을 검증할 수 있도록, opened 가 비면 state=all 최근 MR 로 폴백한다.
    used_state = "opened"
    r = client.get(f"{base}/merge_requests",
                   params={"state": "opened", "per_page": cfg.per_page})
    if r.ok and isinstance(r.data, list) and not r.data:
        # opened 가 비었으면 all 로 재시도해 코드 동작 검증 경로를 확보.
        r_all = client.get(f"{base}/merge_requests",
                           params={"state": "all", "per_page": cfg.per_page})
        if r_all.ok and isinstance(r_all.data, list) and r_all.data:
            r = r_all
            used_state = "all(fallback)"
    summary = "MR 목록 조회 실패"
    sample = None
    mr_iid = None
    mr_web_url = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
        summary = f"MR {len(r.data)}개 (state={used_state})"
        if r.data:
            first = r.data[0]
            mr_iid = first.get("iid")
            mr_web_url = first.get("web_url")
    report.add(CheckResult(f"R-1 대상 MR 확보 (state={used_state})",
                           f"GET {base}/merge_requests?state={used_state}",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    # ========================================================================
    # R-2~R-6: MR 단위 엔드포인트. 대상 MR 이 없으면 일괄 스킵.
    # ========================================================================
    if not mr_iid:
        skip_reason = "MR 없음 — R-2~R-6 스킵 (MR 있는 프로젝트로 GITLAB_TEST_PROJECT_ID 변경 권장)"
        for name, ep in [
            ("R-2 MR 참여자", f"GET {base}/merge_requests/{{iid}}/participants"),
            ("R-3 MR 리뷰어", f"GET {base}/merge_requests/{{iid}}/reviewers"),
            ("R-4 MR 승인 상태", f"GET {base}/merge_requests/{{iid}}/approvals"),
            ("R-5 MR 토론", f"GET {base}/merge_requests/{{iid}}/discussions"),
            ("R-6 MR 댓글", f"GET {base}/merge_requests/{{iid}}/notes"),
        ]:
            report.add(_skip_check(name, ep, skip_reason))
        _finalize(report)
        return

    mr_path = f"{base}/merge_requests/{mr_iid}"
    print(f"대상 MR: !{mr_iid}\n")

    # R-2 MR 참여자
    r = client.get(f"{mr_path}/participants")
    summary = "참여자 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        sample = r.data
        summary = f"참여자 {len(r.data)}명"
    report.add(CheckResult("R-2 MR 참여자",
                           f"GET {mr_path}/participants",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    # R-3 MR 리뷰어 (응답이 {user, state, created_at} 중첩 구조)
    r = client.get(f"{mr_path}/reviewers")
    summary = "리뷰어 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for rv in r.data[:8]:
            u = rv.get("user") or {}
            rows.append({"username": u.get("username"), "name": u.get("name"),
                         "state": rv.get("state"),
                         "created_at": rv.get("created_at")})
        sample = r.data
        summary = f"리뷰어 {len(r.data)}명"
    elif r.ok and isinstance(r.data, dict):
        # 일부 버전은 단일 객체/래퍼로 반환. 방어적 처리.
        sample = {"raw_keys": list(r.data.keys())[:10]}
        summary = "리뷰어 응답이 리스트가 아님 — 스키마 확인 필요"
    report.add(CheckResult("R-3 MR 리뷰어",
                           f"GET {mr_path}/reviewers",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    # R-4 MR 승인 상태 (요약: /approvals). /approval_state 는 상세(rules).
    r = client.get(f"{mr_path}/approvals")
    summary = "승인 상태 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        d = r.data
        approved_by = d.get("approved_by") or []
        approver_names = []
        for a in approved_by[:5]:
            u = a.get("user") or {}
            approver_names.append(u.get("username"))
        sample = r.data
        summary = (f"approved={d.get('approved')} "
                   f"승인자 {len(approved_by)}명 "
                   f"can_approve={d.get('user_can_approve')}")
    report.add(CheckResult("R-4 MR 승인 상태 (approvals)",
                           f"GET {mr_path}/approvals",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    # R-5 MR 토론 스레드
    r = client.get(f"{mr_path}/discussions",
                   params={"per_page": cfg.per_page})
    summary = "토론 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        rows = []
        for d in r.data[:5]:
            notes = d.get("notes") or []
            first_body = (notes[0].get("body") or "")[:60] if notes else ""
            rows.append({
                "id": d.get("id"),
                "individual_note": d.get("individual_note"),
                "resolvable": d.get("resolvable"),
                "resolved": d.get("resolved"),
                "notes_count": len(notes),
                "first_note_preview": first_body,
            })
        sample = r.data
        summary = f"토론 {len(r.data)}개"
    report.add(CheckResult("R-5 MR 토론",
                           f"GET {mr_path}/discussions",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    # R-6 MR 댓글
    r = client.get(f"{mr_path}/notes", params={"per_page": cfg.per_page})
    summary = "댓글 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, list):
        # system 노트(자동 메시지) 와 사용자 노트 구분.
        user_notes = [n for n in r.data if not n.get("system")]
        rows = []
        for n in (user_notes or r.data)[:5]:
            author = n.get("author") or {}
            rows.append({
                "id": n.get("id"),
                "author": author.get("username"),
                "body": (n.get("body") or "")[:60],
                "system": n.get("system"),
                "created_at": n.get("created_at"),
            })
        sample = r.data
        summary = f"댓글 {len(r.data)}개 (사용자 작성 {len(user_notes)}개)"
    report.add(CheckResult("R-6 MR 댓글",
                           f"GET {mr_path}/notes",
                           r.ok, r.status, summary, mr_web_url, sample,
                           r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
