"""P1 읽기 전용 Notion API 동작 검증.

api-docs/notion-api-priority-filter.md 의 P1 카테고리 중 GET/조회용 POST 위주 후보를
실제 토큰으로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

P0(test_p0_readonly.py)이 핵심 데이터(토큰 정체·페이지·DB·댓글)라면,
P1은 데이터 소스 query 의 정렬/필터 동작과 보조 메타데이터를 검증한다.

검증 항목:
  4단계 - 보조 메타데이터
    4-1 GET /users                       사용자/봇 목록 (workspace file size limit)
  5단계 - 데이터 소스 쿼리 동작 (sort/filter)
    5-1 POST /data_sources/{id}/query    기본(정렬 없음)
    5-2 POST /data_sources/{id}/query    sorts 적용 (created_time desc)
    5-3 POST /data_sources/{id}/query    filter 적용 (빈 결과여도 동작 확인)
  6단계 - 검색 옵션·마크다운 옵션
    6-1 POST /search?filter=page         페이지 타입 필터
    6-2 POST /search?filter=database     DB 타입 필터
    6-3 GET /pages/{id}/markdown         include_transcript=true 옵션 (meeting notes 후보)

설계 원칙 (P0 과 동일):
- 데이터가 비어 있어도(0건/필터 무결과) API 정상 응답이면 ok=True.
  "지금 데이터가 없을 뿐"인지와 "API가 막혀 있는지"를 구분하는 것이 목적.

실행:  uv run python test_p1_readonly.py
"""

from __future__ import annotations

from pathlib import Path

from notion_client import (
    ApiResponse,
    CheckResult,
    Config,
    NotionClient,
    Report,
    database_web_url,
    load_config,
    page_web_url,
)


def _resolve_data_source_id(client: NotionClient, cfg: Config
                             ) -> tuple[ApiResponse | None, str | None, str | None]:
    """DB 의 첫 data_source_id 를 확정한다.

    반환: (사용한 ApiResponse|None, data_source_id|None, page_id|None)
    """
    detect_resp, page_id, db_id = client.resolve_page_or_db()
    if not db_id:
        return detect_resp, None, page_id

    r = client.get(f"/databases/{db_id}")
    if r.ok and isinstance(r.data, dict):
        dsl = r.data.get("data_sources") or []
        if dsl:
            return r, dsl[0].get("id"), page_id
    return r, None, page_id


def _summarize_query(r: ApiResponse) -> tuple[str, list | None]:
    """/data_sources/{id}/query 결과를 요약."""
    if not (r.ok and isinstance(r.data, dict)):
        return "쿼리 실패", None
    results = r.data.get("results") or []
    rows = [{"id": x.get("id"), "object": x.get("object")}
            for x in results[:5] if isinstance(x, dict)]
    summary = f"결과 {len(results)}건 (has_more={r.data.get('has_more')})"
    return summary, rows


def main() -> None:
    cfg: Config = load_config()
    client = NotionClient(cfg)
    report = Report(title="P1 읽기 전용 API 검증", base_url=cfg.api_base)

    print(f"Notion: {cfg.api_base}  (Notion-Version {cfg.api_version})")
    print("-" * 60)

    # ---- 4단계: 보조 메타데이터 ----------------------------------------------
    print("[4단계] 보조 메타데이터")

    # 4-1 사용자/봇 목록. 봇의 workspace_limits.max_file_upload_size_in_bytes 포함.
    r = client.get("/users", params={"page_size": cfg.max_results})
    summary = "사용자 목록 조회 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        users = r.data.get("results") or []
        rows = []
        for u in users[:8]:
            if not isinstance(u, dict):
                continue
            bot = u.get("bot") or {}
            ws_limits = (bot.get("workspace_limits") or {}) if bot else {}
            rows.append({
                "id": u.get("id"),
                "name": u.get("name"),
                "type": u.get("type"),
                "bot_owner_type": (bot.get("owner") or {}).get("type") if bot else None,
                "max_file_upload_bytes": ws_limits.get("max_file_upload_size_in_bytes"),
            })
        summary = (f"사용자 {len(users)}건 (has_more={r.data.get('has_more')}) "
                   f"— 봇의 file size limit 확인")
        sample = rows
    report.add(CheckResult("4-1 사용자/봇 목록", "GET /users",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # data_source_id 확정 (5단계에서 사용)
    detect_resp, data_source_id, page_id = _resolve_data_source_id(client, cfg)
    if not data_source_id:
        report.add(CheckResult(
            "5-0 데이터 소스 확정", "GET /databases/{id}", False, None,
            "쿼리 가능한 data_source 를 찾지 못함 (DB 미공유 가능). 5단계는 스킵.",
            None, None, (detect_resp.error if detect_resp else None) or "data_source 미확정", 0))

    # ---- 5단계: 데이터 소스 쿼리 동작 (sort/filter) ---------------------------
    print("\n[5단계] 데이터 소스 쿼리 동작 (sort/filter)")

    if data_source_id:
        # 5-1 기본 쿼리 (정렬 없음)
        r = client.post(f"/data_sources/{data_source_id}/query",
                        json_body={"page_size": cfg.max_results})
        s_summary, s_sample = _summarize_query(r)
        report.add(CheckResult("5-1 데이터 소스 기본 쿼리",
                               f"POST /data_sources/{data_source_id}/query",
                               r.ok, r.status, s_summary,
                               database_web_url(data_source_id), s_sample,
                               r.error, r.elapsed_ms))

        # 5-2 sorts 적용 — created_time desc
        r = client.post(f"/data_sources/{data_source_id}/query", json_body={
            "page_size": cfg.max_results,
            "sorts": [{"timestamp": "created_time", "direction": "descending"}],
        })
        s_summary, s_sample = _summarize_query(r)
        # 정렬이 실제로 적용됐는지 대조용으로 첫 결과 created_time 기록.
        if r.ok and isinstance(r.data, dict):
            results = r.data.get("results") or []
            if results:
                s_summary += f" (첫 결과 created_time={results[0].get('created_time')})"
        report.add(CheckResult("5-2 sorts=created_time desc",
                               f"POST /data_sources/{data_source_id}/query (sorts)",
                               r.ok, r.status, s_summary,
                               database_web_url(data_source_id), s_sample,
                               r.error, r.elapsed_ms))

        # 5-3 filter 적용 — "이번 주 생성" 시도. 결과가 없어도 동작만 확인.
        # property 이름을 모르므로 timestamp 기반 필터로 범용 적용.
        r = client.post(f"/data_sources/{data_source_id}/query", json_body={
            "page_size": cfg.max_results,
            "filter": {"timestamp": "created_time", "past_week": {}},
        })
        if r.ok:
            s_summary, s_sample = _summarize_query(r)
            s_summary += " — past_week 필터 정상 동작 (빈 결과여도 ok)"
        else:
            # filter 스키마가 맞지 않으면 validation_error 가능. 이것도 유효한 정보.
            s_summary = f"필터 요청 거부됨 — {r.error or 'schema 확인 필요'}"
            s_sample = None
        report.add(CheckResult("5-3 filter=created_time past_week",
                               f"POST /data_sources/{data_source_id}/query (filter)",
                               r.ok, r.status, s_summary,
                               database_web_url(data_source_id), s_sample,
                               r.error if not r.ok else None, r.elapsed_ms))
    else:
        for label, endpoint in (
            ("5-1 데이터 소스 기본 쿼리", "POST /data_sources/{id}/query"),
            ("5-2 sorts=created_time desc", "POST /data_sources/{id}/query (sorts)"),
            ("5-3 filter=created_time past_week", "POST /data_sources/{id}/query (filter)"),
        ):
            report.add(CheckResult(label, endpoint, False, None,
                                   "data_source 미확정 — 스킵", None, None, None, 0))

    # ---- 6단계: 검색 옵션·마크다운 옵션 ---------------------------------------
    print("\n[6단계] 검색 옵션·마크다운 옵션")

    # 6-1 search filter=page
    r = client.post("/search", json_body={
        "page_size": cfg.max_results,
        "filter": {"value": "page", "property": "object"},
    })
    summary = "search(page) 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        results = r.data.get("results") or []
        non_page = [x for x in results if x.get("object") != "page"]
        sample = [{"id": x.get("id"), "title": (x.get("properties") or {})}
                  for x in results[:3] if isinstance(x, dict)]
        summary = (f"페이지 검색 결과 {len(results)}건 "
                   f"(page 외 결과: {len(non_page)} — 필터 준수 여부)")
    report.add(CheckResult("6-1 search filter=page",
                           "POST /search (filter value=page)",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # 6-2 search filter=database
    r = client.post("/search", json_body={
        "page_size": cfg.max_results,
        "filter": {"value": "database", "property": "object"},
    })
    summary = "search(database) 실패"
    sample = None
    if r.ok and isinstance(r.data, dict):
        results = r.data.get("results") or []
        non_db = [x for x in results if x.get("object") != "database"]
        sample = [{"id": x.get("id"),
                   "title": [f.get("plain_text", "") for f in (x.get("title") or [])]}
                  for x in results[:3] if isinstance(x, dict)]
        summary = (f"DB 검색 결과 {len(results)}건 "
                   f"(database 외 결과: {len(non_db)} — 필터 준수 여부)")
    report.add(CheckResult("6-2 search filter=database",
                           "POST /search (filter value=database)",
                           r.ok, r.status, summary, None, sample,
                           r.error, r.elapsed_ms))

    # 6-3 페이지 마크다운 with include_transcript. meeting_notes 후보.
    # page_id 가 없으면 6-1/6-2 search 결과에서 하나 고른다.
    target_page = page_id
    if not target_page:
        r_search = client.post("/search", json_body={
            "page_size": 1,
            "filter": {"value": "page", "property": "object"},
        })
        if r_search.ok and isinstance(r_search.data, dict):
            results = r_search.data.get("results") or []
            target_page = results[0].get("id") if results else None

    if target_page:
        r = client.get(f"/pages/{target_page}/markdown",
                       params={"include_transcript": "true"})
        summary = "페이지 마크다운(include_transcript) 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            md = r.data.get("markdown") or ""
            preview = md[:120].replace("\n", "\\n")
            summary = (f"markdown {len(md)}자, truncated={r.data.get('truncated')}, "
                       f"unknown={len(r.data.get('unknown_block_ids') or [])} "
                       f"(미리보기: {preview!r})")
            sample = {"id": r.data.get("id"),
                      "truncated": r.data.get("truncated"),
                      "unknown_block_ids": r.data.get("unknown_block_ids"),
                      "markdown_preview": preview}
        report.add(CheckResult("6-3 페이지 마크다운 include_transcript",
                               f"GET /pages/{target_page}/markdown?include_transcript=true",
                               r.ok, r.status, summary,
                               page_web_url(cfg.api_base, target_page), sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("6-3 페이지 마크다운 include_transcript",
                               "GET /pages/{id}/markdown", False, None,
                               "검증할 페이지가 없음", None, None, None, 0))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
