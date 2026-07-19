# Notion API 동작 테스트 (notion-api-test)

## 목적
`api-docs/notion-api-priority-filter.md` 의 "우선 검증할 기능 가설" P0/P1 카테고리를
실제 토큰으로 검증하는 POC. 완성도보다 검증 가능성·재현성을 우선한다.

## 구성
- `notion_client.py` — 공통 모듈(설정·HTTP 클라이언트·리포트). 모든 테스트가 의존.
- `test_p0_readonly.py` — P0 읽기 전용(사용자·search·페이지·blocks·markdown·DB·댓글·파일).
- `test_p1_readonly.py` — P1 읽기 후보(users·data_sources query/sort/filter·search filter·transcript).
- `test_oauth_token.py` — OAuth 토큰 종류 식별 + refresh 흐름.
- `test_webhooks.py` — Notion webhook 부재(제약 확인).
- `docs/notion-oauth-postman.md` — Postman/curl 로 OAuth 토큰 획득 절차.

## 인증 (token-agnostic)
- `.env` 변수: `NOTION_API_KEY` (필수). Internal installation token 또는 OAuth access_token 어느 쪽이든 가능.
- 세션 헤더: `Authorization: Bearer <token>`, `Notion-Version: 2026-03-11`.
- OAuth 토큰 획득 절차 자체는 스크립트 범위가 아님. Postman으로 발급받아 `NOTION_API_KEY` 에 입력.
- 모든 검증 대상 페이지/DB 는 Notion UI 의 Add connections 로 명시적으로 공유 필요.

## 실행 규칙
- 셸 명령은 `rtk` 우선(`uv run` 은 `rtk proxy uv run ...`). AGENTS.md(루트) 참고.
- 의존성: `uv sync`.
- 실행: `uv run python test_p0_readonly.py` (P1, OAuth, webhooks 동일 패턴).
- 민감 정보(토큰/secret)는 로그에 출력하지 않는다.

## 설계 원칙
- HTTP 오류는 예외로 중단하지 않고 `(status, error)` 로 기록. 403/404 가 어디서 나는지가 핵심.
- 데이터가 비어도(0건) 정상 응답이면 ok=True ("API 막힘" vs "데이터 없음" 구분).
- webhook 미지원은 "실패"가 아니라 "확인된 제약"으로 기록.
- 읽기 전용 GET/조회용 POST(search, data_sources query)만 호출. write 엔드포인트 사용 금지
  (OAuth token 교환/refresh 는 예외).
- 원문 URL(web_url)을 함께 기록 — 상세 내용은 Notion 원문으로 이동.
