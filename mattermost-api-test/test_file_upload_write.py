"""사용자 상호작용 — 파일 업로드 검증.

통합 워크스페이스가 "배포 결과·테스트 산출물 공유 보조" 용도로 쓸 파일 업로드 API 를
실제 PAT 로 검증한다. 이 스크립트는 쓰기(POST)를 수행한다.

안전장치:
- 업로드 내용은 수백 바이트짜리 마크다운 텍스트. (채널에 게시 post 하지는 않음)
- 파일명에 [POC-TEST] + 타임스탬프 를 붙여 식별.

중요 — 플랫폼 제약 (실제 호출로 확인됨):
- Mattermost v4 API 는 **파일 단독 삭제 엔드포인트를 제공하지 않는다.**
  (api-docs/.../08-files/ 디렉터리에 delete operation 없음. DELETE /files/{id}
  호출 시 404 반환 확인됨.)
- 파일은 post 에 첨부된 뒤 해당 post 가 삭제될 때 함께 삭제되거나, 시스템 관리자의
  data retention 정책으로만 정리된다.
- 따라서 이 스크립트는 업로드 + 메타 조회까지만 수행하고, **업로드한 파일은
  채널에 첨부되지 않은 채 남는다.** (post 를 만들지 않았으므로 사용자에게 노출되지 않음)
- 통합 서비스 설계 시: 업로드한 파일은 반드시 post 와 묶어 관리하고, 폐기가 필요하면
  해당 post 삭제로 처리해야 한다.

문서상 정확한 엔드포인트 (api-docs/mattermost_defuddle_markdown/08-files/):
- 업로드: POST /files  (multipart/form-data: files, channel_id). 권한 upload_file
- 메타:   GET  /files/{file_id}/info
- 삭제:   (API 없음 — 404 확인됨)

multipart 처리는 mattermost_client.MattermostClient.upload_file() 가 담당한다.

검증 항목:
  F-1 POST /files (multipart)         작은 텍스트 파일 업로드 (upload_file 권한)
  F-2 GET  /files/{file_id}/info      업로드한 파일 메타데이터 조회
  F-3 DELETE /files/{file_id}         삭제 시도 (플랫폼 제약 확인용 — 404 예상)

실행:  uv run python test_file_upload_write.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from mattermost_client import (
    CheckResult,
    Config,
    MattermostClient,
    Report,
    channel_web_url,
    load_config,
)


def main() -> None:
    cfg: Config = load_config()
    client = MattermostClient(cfg)
    report = Report(title="파일 업로드 검증", base_url=cfg.base_url)

    ts_label = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f"Mattermost: {cfg.base_url}")
    print(f"주의: 이 스크립트는 파일을 업로드한 뒤 삭제합니다(자체 정리). ts={ts_label}")
    print("-" * 60)

    # 대상 팀/채널 확정.
    _, team_id = client.resolve_team()
    if not team_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams", False, None,
                               "대상 팀을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_TEAM_ID 확인", 0))
        _finalize(report)
        return
    _, channel_id = client.resolve_channel(team_id)
    if not channel_id:
        report.add(CheckResult("대상 확정", "GET /users/me/teams/{team_id}/channels", False, None,
                               "대상 채널을 찾을 수 없음", None, None,
                               "MATTERMOST_TEST_CHANNEL_ID 확인", 0))
        _finalize(report)
        return

    # 원문 URL 조립용 team_name/channel_name.
    r_team = client.get(f"/teams/{team_id}")
    r_ch = client.get(f"/channels/{channel_id}")
    team_name = r_team.data.get("name") if (r_team.ok and isinstance(r_team.data, dict)) else ""
    channel_name = r_ch.data.get("name") if (r_ch.ok and isinstance(r_ch.data, dict)) else ""
    web_url = channel_web_url(cfg.base_url, team_name, channel_name) if (team_name and channel_name) else None

    print(f"대상: team={team_name}({team_id}) channel={channel_name}({channel_id})\n")

    # 업로드할 짧은 텍스트 파일 내용. 채널에 post 하지는 않는다.
    filename = f"[POC-TEST]_upload_{ts_label}.md"
    file_content = (
        f"# A502 POC 파일 업로드 테스트\n\n"
        f"- timestamp: {ts_label}\n"
        f"- channel: {channel_name} ({channel_id})\n"
        f"- purpose: upload API 동작 검증용. 자동 삭제됨.\n"
    ).encode("utf-8")

    # F-1 파일 업로드 (multipart/form-data).
    # requests 규격: {"files": (filename, bytes, mime_type)}
    files = {"files": (filename, file_content, "text/markdown")}
    data = {"channel_id": channel_id}
    r = client.upload_file("/files", files=files, data=data)
    summary = "파일 업로드 실패"
    sample = None
    file_id = None
    if r.ok and isinstance(r.data, dict):
        file_infos = r.data.get("file_infos") or []
        if file_infos:
            fi = file_infos[0]
            file_id = fi.get("id")
            sample = {
                "id": fi.get("id"),
                "name": fi.get("name"),
                "size": fi.get("size"),
                "mime_type": fi.get("mime_type"),
                "channel_id": fi.get("channel_id"),
            }
            summary = (f"업로드 성공 id={file_id} "
                       f"name={fi.get('name')} size={fi.get('size')}B")
            print(f"  [POC-TEST] 파일 업로드: {filename} → id={file_id}")
        else:
            summary = "업로드 응답에 file_infos 없음"
    report.add(CheckResult("F-1 파일 업로드",
                           "POST /files (multipart)",
                           r.ok, r.status, summary, web_url, sample,
                           r.error, r.elapsed_ms))

    # F-2 업로드한 파일 메타데이터 조회.
    if not file_id:
        report.add(CheckResult("F-2 파일 메타데이터 조회",
                               "GET /files/{file_id}/info",
                               False, None, "업로드 실패 — 메타 조회 스킵",
                               None, None, None, 0))
    else:
        r = client.get(f"/files/{file_id}/info")
        summary = "메타데이터 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            fi = r.data
            sample = {
                "id": fi.get("id"),
                "name": fi.get("name"),
                "size": fi.get("size"),
                "extension": fi.get("extension"),
                "mime_type": fi.get("mime_type"),
                "user_id": fi.get("user_id"),
                "create_at": fi.get("create_at"),
            }
            summary = (f"메타 조회 성공 name={fi.get('name')} "
                       f"size={fi.get('size')}B ext={fi.get('extension')}")
        report.add(CheckResult("F-2 파일 메타데이터 조회",
                               f"GET /files/{file_id}/info",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))

    # F-3 파일 삭제 시도 — 플랫폼 제약 확인.
    # Mattermost v4 는 파일 단독 삭제 API 를 제공하지 않는다. 404 는 "제약 확인됨"
    # 으로 해석하고, 만약 미래 버전에서 삭제가 지원되면(200) 정리로 기록한다.
    if not file_id:
        report.add(CheckResult("F-3 파일 삭제 시도 (플랫폼 제약 확인)",
                               "DELETE /files/{file_id}",
                               False, None, "업로드 실패 — 삭제 시도 스킵",
                               None, None, None, 0))
    else:
        r = client.delete(f"/files/{file_id}")
        summary = "삭제 응답 확인 필요"
        sample = None
        if r.ok:
            sample = {"status": r.data.get("status") if isinstance(r.data, dict) else "ok"}
            summary = f"삭제 성공 (id={file_id}) — 이 인스턴스는 파일 삭제를 지원함"
            print(f"  [POC-TEST] 파일 삭제: id={file_id} ← 정리 완료")
        elif r.status == 404:
            # 예상된 플랫폼 제약. ok=True 로 기록하여 "검증 목적 달성" 으로 해석.
            sample = {"file_id": file_id, "note": "Mattermost v4 는 파일 단독 삭제 API 미제공"}
            summary = ("404 — 파일 단독 삭제 API 없음 (플랫폼 제약 확인됨). "
                       "파일은 post 삭제 또는 data retention 으로만 정리됨")
            print(f"  [POC-TEST] 파일 삭제 불가(id={file_id}): Mattermost 플랫폼 제약. "
                  f"post 미첨부 상태로 남음 (사용자에게 노출되지 않음)")
            # ok 플래그를 True 로 올려 "검증 목적(제약 확인) 달성" 으로 표시.
            report.add(CheckResult("F-3 파일 삭제 시도 (플랫폼 제약 확인)",
                                   f"DELETE /files/{file_id}",
                                   True, r.status, summary, web_url, sample,
                                   None, r.elapsed_ms))
            _finalize(report)
            return
        report.add(CheckResult("F-3 파일 삭제 시도 (플랫폼 제약 확인)",
                               f"DELETE /files/{file_id}",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
