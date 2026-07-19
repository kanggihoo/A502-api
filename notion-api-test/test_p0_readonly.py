"""P0 읽기 전용 Notion API 동작 검증.

api-docs/notion-api-priority-filter.md 의 "첫 검증 순서" 1~3단계(GET/조회용 POST만)를
실제 토큰으로 호출해 본다. 이 스크립트는 어떤 리소스도 생성/수정/삭제하지 않는다.

검증 항목:
  1단계 - 토큰 정체·접근 자원 확인
    1-1 GET /users/me                       현재 봇 사용자(토큰 정체)
    1-2 POST /search                        접근 가능 페이지/DB (대상 탐지)
    1-3 GET /pages/{id} | /databases/{id}   대상 상세 메타데이터
  2단계 - 페이지 콘텐츠 읽기
    2-1 GET /blocks/{page_id}/children      페이지 블록 children (page content)
    2-2 GET /pages/{page_id}/markdown       페이지 마크다운 (원문 맥락)
    2-3 GET /databases/{db_id}              데이터베이스 메타 + data_sources (있을 때)
  3단계 - DB 쿼리·댓글·파일 맥락
    3-1 POST /data_sources/{id}/query       데이터 소스 행(페이지) 조회
    3-2 GET /comments?block_id={page_id}    페이지 댓글
    3-3 (blocks children에서) 파일/미디어   file/image/video/audio/pdf 블록 URL 추출

설계 원칙:
- 데이터가 비어 있어도(0건) API 정상 응답이면 ok=True. "데이터가 지금 없을 뿐"인지와
  "API가 막혀 있는지"를 구분하는 것이 검증 목적.
- 모든 응답은 원문 Notion URL 을 web_url 로 함께 기록한다 (상세는 Notion 원문으로).

실행:  uv run python test_p0_readonly.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

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


# 파일/미디어 블록 타입. blocks children 응답에서 URL 추출 대상.
MEDIA_BLOCK_TYPES = {"image", "file", "video", "audio", "pdf"}


def _title_of_page(page_obj: dict) -> str:
    """page 객체에서 title 프로퍼티의 plain_text 를 추출한다."""
    props = page_obj.get("properties") or {}
    # "title" 타입 프로퍼티를 찾는다 (키 이름은 DB 스키마에 따라 다를 수 있음).
    for prop in props.values():
        if isinstance(prop, dict) and prop.get("type") == "title":
            fragments = prop.get("title") or []
            return "".join(f.get("plain_text", "") for f in fragments if isinstance(f, dict))
    return ""


def _db_title(db_obj: dict) -> str:
    fragments = db_obj.get("title") or []
    return "".join(f.get("plain_text", "") for f in fragments if isinstance(f, dict))


def _extract_media_urls(blocks: list) -> list[dict]:
    """blocks children 결과에서 미디어 블록의 (type, name, url, expiry) 를 뽑는다.

    file/image/video/audio/pdf 블록은 type-specific 객체 안에 file 또는 external
    서브객체를 가진다. file 타입은 url + expiry_time (임시 서명 URL).
    """
    out: list[dict] = []
    for b in blocks:
        if not isinstance(b, dict):
            continue
        btype = b.get("type")
        if btype not in MEDIA_BLOCK_TYPES:
            continue
        inner = b.get(btype) or {}
        # 캡션 plain_text
        caption = "".join(f.get("plain_text", "") for f in (inner.get("caption") or [])
                          if isinstance(f, dict))
        entry: dict[str, Any] = {
            "id": b.get("id"),
            "type": btype,
            "caption": caption or None,
        }
        fileobj = inner.get("file") or inner.get("external")
        if isinstance(fileobj, dict):
            entry["url"] = fileobj.get("url")
            entry["source"] = "file" if "file" in inner else "external"
            entry["expiry_time"] = fileobj.get("expiry_time")
        else:
            entry["url"] = None
            entry["source"] = None
        out.append(entry)
    return out


def main() -> None:
    cfg: Config = load_config()
    client = NotionClient(cfg)
    report = Report(title="P0 읽기 전용 API 검증", base_url=cfg.api_base)

    print(f"Notion: {cfg.api_base}  (Notion-Version {cfg.api_version})")
    print(f"대상 페이지: {cfg.page_id or '(자동 탐지)'}")
    print(f"대상 DB: {cfg.database_id or '(자동 탐지)'}")
    print("-" * 60)

    # 2-1 에서 수집한 미디어 블록을 3-3 이 재사용. page_id 가 없으면 빈 리스트.
    media_preview: list[dict] = []

    # ---- 1단계: 토큰 정체·접근 자원 확인 -------------------------------------
    print("\n[1단계] 토큰 정체·접근 자원 확인")

    # 1-1 현재 봇 사용자. /users/me 는 봇 정체를 확인하는 가장 기본 호출.
    r = client.get("/users/me")
    summary = "봇 사용자 조회 실패"
    web_url = None
    sample = None
    if r.ok and isinstance(r.data, dict):
        me = r.data
        bot = me.get("bot") or {}
        owner = bot.get("owner") or {}
        # owner.type 이 "user" 이면 OAuth 기반, "workspace" 이면 internal.
        owner_type = owner.get("type")
        ws_limits = (bot.get("workspace_limits") or {})
        summary = (f"{me.get('name')} (type={me.get('type')}, "
                   f"owner={owner_type}, "
                   f"workspace={bot.get('workspace_name')!r}, "
                   f"max_file_upload={ws_limits.get('max_file_upload_size_in_bytes')})")
        token_kind = ("OAuth (user-authorized)" if owner_type == "user"
                      else "Internal connection" if owner_type == "workspace"
                      else owner_type or "unknown")
        sample = {
            "id": me.get("id"),
            "name": me.get("name"),
            "type": me.get("type"),
            "token_kind": token_kind,
            "owner_type": owner_type,
            "workspace_name": bot.get("workspace_name"),
            "workspace_id": bot.get("workspace_id"),
            "max_file_upload_size_in_bytes": ws_limits.get("max_file_upload_size_in_bytes"),
        }
    report.add(CheckResult("1-1 현재 봇 사용자", "GET /users/me", r.ok, r.status,
                           summary, web_url, sample, r.error, r.elapsed_ms))

    # 1-2 접근 가능 페이지/DB (대상 탐지에도 사용)
    r_search = client.post("/search", json_body={"page_size": cfg.max_results})
    page_sample = None
    db_sample = None
    if r_search.ok and isinstance(r_search.data, dict):
        results = r_search.data.get("results") or []
        page_rows = [{"id": x.get("id"), "title": _title_of_page(x)}
                     for x in results if x.get("object") == "page"][:5]
        db_rows = [{"id": x.get("id"), "title": _db_title(x)}
                   for x in results if x.get("object") == "database"][:5]
        page_sample = page_rows
        db_sample = db_rows
        summary = (f"검색 결과 {len(results)}건 "
                   f"(페이지 {len(page_rows)}+ / DB {len(db_rows)}+ 표시, "
                   f"has_more={r_search.data.get('has_more')})")
    else:
        summary = "search 실패"
    report.add(CheckResult("1-2 접근 가능 페이지/DB", "POST /search",
                           r_search.ok, r_search.status, summary,
                           None, {"pages": page_sample, "databases": db_sample},
                           r_search.error, r_search.elapsed_ms))

    # 대상 page/database ID 확정
    detect_resp, page_id, db_id = client.resolve_page_or_db()
    if not (page_id or db_id):
        report.add(CheckResult(
            "1-3 대상 리소스 상세", "GET /pages|/databases/{id}", False, None,
            "대상 페이지/DB 를 찾을 수 없음 (NOTION_TEST_PAGE_ID/DATABASE_ID 설정 또는 "
            "Integration/OAuth 연결에 리소스 공유 필요)",
            None, None, detect_resp.error or "대상 미확정", 0))
        _finalize(report)
        return

    # 1-3 대상 상세 (페이지 우선)
    sample_obj_id = page_id or db_id
    if page_id:
        r = client.get(f"/pages/{page_id}")
        endpoint = f"GET /pages/{page_id}"
        summary = "페이지 상세 조회 실패"
        web_url = page_web_url(cfg.api_base, page_id)
        sample = None
        if r.ok and isinstance(r.data, dict):
            title = _title_of_page(r.data)
            parent = r.data.get("parent") or {}
            summary = (f"page id={r.data.get('id')} title={title!r} "
                       f"parent_type={parent.get('type')} "
                       f"archived={r.data.get('archived')}")
            sample = {"id": r.data.get("id"), "title": title,
                      "parent": parent, "url": r.data.get("url"),
                      "archived": r.data.get("archived"),
                      "last_edited_time": r.data.get("last_edited_time")}
        report.add(CheckResult("1-3 대상 페이지 상세", endpoint,
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        # 페이지가 없으면 DB 상세를 2-3 에서 처리하므로 여기서는 스킵 표기.
        report.add(CheckResult("1-3 대상 페이지 상세", "GET /pages/{id}", False, None,
                               "접근 가능한 페이지가 없음 (DB 만 탐지됨)",
                               None, None, None, 0))

    # ---- 2단계: 페이지 콘텐츠 읽기 -------------------------------------------
    print("\n[2단계] 페이지 콘텐츠 읽기")

    if page_id:
        # 2-1 페이지 블록 children
        r = client.get(f"/blocks/{page_id}/children",
                       params={"page_size": cfg.max_results})
        summary = "블록 children 조회 실패"
        web_url = page_web_url(cfg.api_base, page_id)
        block_sample = None
        media_preview: list[dict] = []
        if r.ok and isinstance(r.data, dict):
            blocks = r.data.get("results") or []
            block_sample = [{"id": b.get("id"), "type": b.get("type"),
                             "has_children": b.get("has_children")}
                            for b in blocks[:5] if isinstance(b, dict)]
            media_preview = _extract_media_urls(blocks)
            summary = (f"블록 {len(blocks)}개 (has_more={r.data.get('has_more')}, "
                       f"미디어 블록 {len(media_preview)}개)")
        report.add(CheckResult("2-1 페이지 블록 children",
                               f"GET /blocks/{page_id}/children",
                               r.ok, r.status, summary, web_url,
                               {"blocks_sample": block_sample,
                                "media_blocks": media_preview[:3]},
                               r.error, r.elapsed_ms))

        # 2-2 페이지 마크다운 (원문 맥락)
        r = client.get(f"/pages/{page_id}/markdown")
        summary = "페이지 마크다운 조회 실패"
        sample = None
        if r.ok and isinstance(r.data, dict):
            md = r.data.get("markdown") or ""
            preview = md[:120].replace("\n", "\\n")
            summary = (f"markdown {len(md)}자, truncated={r.data.get('truncated')}, "
                       f"unknown_blocks={len(r.data.get('unknown_block_ids') or [])} "
                       f"(미리보기: {preview!r})")
            sample = {"id": r.data.get("id"),
                      "truncated": r.data.get("truncated"),
                      "unknown_block_ids": r.data.get("unknown_block_ids"),
                      "markdown_preview": preview}
        report.add(CheckResult("2-2 페이지 마크다운",
                               f"GET /pages/{page_id}/markdown",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("2-1 페이지 블록 children", "GET /blocks/{page_id}/children",
                               False, None, "접근 가능한 페이지가 없음", None, None, None, 0))
        report.add(CheckResult("2-2 페이지 마크다운", "GET /pages/{page_id}/markdown",
                               False, None, "접근 가능한 페이지가 없음", None, None, None, 0))

    # 2-3 DB 메타 + data_sources
    if db_id:
        r = client.get(f"/databases/{db_id}")
        summary = "데이터베이스 조회 실패"
        web_url = database_web_url(db_id)
        sample = None
        data_source_id: str | None = None
        if r.ok and isinstance(r.data, dict):
            title = _db_title(r.data)
            data_sources = r.data.get("data_sources") or []
            if data_sources:
                data_source_id = data_sources[0].get("id")
            summary = (f"DB id={r.data.get('id')} title={title!r} "
                       f"data_sources={len(data_sources)} "
                       f"is_inline={r.data.get('is_inline')} "
                       f"archived={r.data.get('archived')}")
            sample = {"id": r.data.get("id"), "title": title,
                      "data_sources": data_sources,
                      "parent": r.data.get("parent"),
                      "url": r.data.get("url")}
        report.add(CheckResult("2-3 데이터베이스 메타 + data_sources",
                               f"GET /databases/{db_id}",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("2-3 데이터베이스 메타 + data_sources",
                               "GET /databases/{id}", False, None,
                               "접근 가능한 DB 가 없음", None, None, None, 0))
        data_source_id = None

    # ---- 3단계: DB 쿼리·댓글·파일 맥락 ---------------------------------------
    print("\n[3단계] DB 쿼리·댓글·파일 맥락")

    # 3-1 데이터 소스 행(페이지) 조회. DB 검색 결과에서 data_source_id 를 찾아 사용.
    resolved_ds_id = data_source_id
    if not resolved_ds_id and db_id:
        # 2-3 을 건너뛴 경우 fallback: DB 상세에서 data_source_id 다시 확보.
        r_db = client.get(f"/databases/{db_id}")
        if r_db.ok and isinstance(r_db.data, dict):
            dsl = r_db.data.get("data_sources") or []
            resolved_ds_id = dsl[0].get("id") if dsl else None

    if resolved_ds_id:
        r = client.post(f"/data_sources/{resolved_ds_id}/query",
                        json_body={"page_size": cfg.max_results})
        summary = "데이터 소스 쿼리 실패"
        sample = None
        web_url = database_web_url(resolved_ds_id)
        if r.ok and isinstance(r.data, dict):
            results = r.data.get("results") or []
            rows = [{"id": x.get("id"), "title": _title_of_page(x)}
                    for x in results if x.get("object") == "page"][:5]
            summary = (f"행(페이지) {len(results)}건 (has_more={r.data.get('has_more')})")
            sample = rows
        report.add(CheckResult("3-1 데이터 소스 행(페이지) 조회",
                               f"POST /data_sources/{resolved_ds_id}/query",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("3-1 데이터 소스 행(페이지) 조회",
                               "POST /data_sources/{id}/query", False, None,
                               "쿼리 가능한 data_source 를 찾지 못함 (DB 미공유 가능)",
                               None, None, None, 0))

    # 3-2 페이지 댓글
    if page_id:
        r = client.get("/comments", params={"block_id": page_id,
                                             "page_size": cfg.max_results})
        summary = "댓글 조회 실패"
        sample = None
        web_url = page_web_url(cfg.api_base, page_id)
        if r.ok and isinstance(r.data, dict):
            comments = r.data.get("results") or []
            rows = [{"id": c.get("id"),
                     "created_time": c.get("created_time"),
                     "author": (c.get("created_by") or {}).get("id")}
                    for c in comments[:5] if isinstance(c, dict)]
            summary = (f"댓글 {len(comments)}건 (has_more={r.data.get('has_more')})")
            sample = rows
        report.add(CheckResult("3-2 페이지 댓글",
                               f"GET /comments?block_id={page_id}",
                               r.ok, r.status, summary, web_url, sample,
                               r.error, r.elapsed_ms))
    else:
        report.add(CheckResult("3-2 페이지 댓글", "GET /comments?block_id={page_id}",
                               False, None, "조회할 페이지가 없음", None, None, None, 0))

    # 3-3 파일/미디어 블록 URL. 2-1 에서 이미 수집했으면 그 결과를, 아니면 재조회.
    if page_id:
        media_rows = media_preview
        if not media_rows:
            r_blocks = client.get(f"/blocks/{page_id}/children",
                                  params={"page_size": cfg.max_results})
            if r_blocks.ok and isinstance(r_blocks.data, dict):
                media_rows = _extract_media_urls(r_blocks.data.get("results") or [])
        if media_rows:
            summary = (f"미디어 블록 {len(media_rows)}개 발견 "
                       f"(타입: {sorted({m['type'] for m in media_rows})})")
            ok_flag = True
            status_flag = 200
            err_flag = None
            elapsed = 0
        else:
            summary = "미디어(file/image/video/audio/pdf) 블록 없음 — 데이터 없음"
            ok_flag = True  # API 동작엔 문제없고 데이터만 없는 경우
            status_flag = 200
            err_flag = None
            elapsed = 0
        report.add(CheckResult("3-3 파일/미디어 블록 URL 추출",
                               f"GET /blocks/{page_id}/children (filter media)",
                               ok_flag, status_flag, summary,
                               page_web_url(cfg.api_base, page_id),
                               media_rows[:3] or None, err_flag, elapsed))
    else:
        report.add(CheckResult("3-3 파일/미디어 블록 URL 추출",
                               "GET /blocks/{page_id}/children", False, None,
                               "조회할 페이지가 없음", None, None, None, 0))

    _finalize(report)


def _finalize(report: Report) -> None:
    report.print_summary()
    results_dir = Path(__file__).resolve().parent / "results"
    saved = report.save(results_dir)
    print(f"\nJSON 리포트 저장됨: {saved}")


if __name__ == "__main__":
    main()
