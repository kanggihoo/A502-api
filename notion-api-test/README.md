# Notion API 동작 테스트 (POC)

`api-docs/notion-api-priority-filter.md` 의 "우선 검증할 기능 가설" P0/P1 카테고리를
실제 토큰으로 호출해 보기 위한 Python 스크립트 모음. 완성도보다 **검증 가능성·재현성**을 우선한다.

> 이 도구는 **읽기 전용(P0/P1)** 과 **OAuth 토큰 검증** · **webhook 제약 확인** 네 스크립트로 분리되어 있다.
> 리소스를 생성/수정/삭제하는 호출은 일절 하지 않는다 (OAuth `code→token` 교환, `refresh_token` 갱신은 제외).

## 구성

| 파일 | 역할 | 쓰기 여부 |
| --- | --- | --- |
| `notion_client.py` | 공통: 설정 로드, HTTP 클라이언트, 결과 리포트 | — |
| `test_p0_readonly.py` | P0 1~3단계 GET/조회용 POST 검증 (사용자·search·페이지·blocks·markdown·DB·댓글·파일) | 읽기 전용 |
| `test_p1_readonly.py` | P1 읽기 후보 검증 (users·data_sources query/sort/filter·search filter·include_transcript) | 읽기 전용 |
| `test_oauth_token.py` | OAuth 토큰 종류 식별 + refresh 흐름 검증 | token 갱신만 |
| `test_webhooks.py` | Notion webhook 부재 — "확인된 제약"으로 기록 | — |
| `docs/notion-oauth-postman.md` | Postman/curl 로 OAuth 토큰 획득하는 절차 가이드 | — |

## 사전 준비

### 1. Integration/토큰 준비

두 가지 방식 중 하나 선택:

- **Internal connection** (POC 추천): <https://www.notion.so/my-integrations> →
  New integration (Internal) → Configuration 탭에서 **Internal Integration Secret** 복사.
- **OAuth 2.0** (public connection): `docs/notion-oauth-postman.md` 절차대로
  Postman/curl 로 access_token 발급.

### 2. 대상 페이지/DB 공유 (공통)

Integration/OAuth connection 이 접근할 페이지/DB 를 Notion UI 의
`•••` → **Add connections** 으로 명시적으로 공유해야 한다. 공유하지 않으면 404/403.

### 3. 환경변수 설정

```bash
cd notion-api-test
cp .env.example .env
# .env 를 열어 아래 값 입력
```

| 변수 | 필수 | 설명 |
| --- | --- | --- |
| `NOTION_API_KEY` | O | Bearer 토큰. Internal secret 또는 OAuth `access_token` |
| `NOTION_API_VERSION` | X | `2026-03-11` (기본값) |
| `NOTION_BASE_URL` | X | `https://api.notion.com/v1` (기본값) |
| `NOTION_TEST_PAGE_ID` | X | 대상 페이지 UUID. 비우면 search 로 자동 탐지 |
| `NOTION_TEST_DATABASE_ID` | X | 대상 DB UUID. 비우면 search 로 자동 탐지 |
| `REQUEST_TIMEOUT` | X | 요청 타임아웃(초). 기본 30 |
| `MAX_RESULTS` | X | 페이지 사이즈. 기본 10 (Notion 상한 100) |
| `NOTION_OAUTH_CLIENT_ID` | X | OAuth refresh 검증용 |
| `NOTION_OAUTH_CLIENT_SECRET` | X | OAuth refresh 검증용 |
| `NOTION_OAUTH_REFRESH_TOKEN` | X | OAuth refresh 검증용 |
| `NOTION_OAUTH_REDIRECT_URI` | X | OAuth redirect URI (Postman 콜백) |

> `.env` 는 `.gitignore` 로 커밋되지 않는다. 토큰·secret 등 민감 정보는 절대 저장소에 올리지 말 것.

## 실행

```bash
# 의존성 설치 (최초 1회)
uv sync

# P0 읽기 전용 검증 (안전, GET/조회용 POST만)
uv run python test_p0_readonly.py

# P1 읽기 후보 검증 (안전)
uv run python test_p1_readonly.py

# OAuth 토큰 종류 식별 + refresh 검증 (OAuth 변수 있을 때만 refresh 수행)
uv run python test_oauth_token.py

# webhook 부재 — 확인된 제약 기록
uv run python test_webhooks.py
```

## 검증 항목 매트릭스

### `test_p0_readonly.py` (P0, 읽기 전용) — 필터문서 "첫 검증 순서" 1~3단계

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 1-1 | `GET /users/me` | 토큰 정체·봇 owner type (OAuth/Internal 식별) |
| 1-2 | `POST /search` | 접근 가능 페이지/DB + 대상 탐지 |
| 1-3 | `GET /pages/{id}` | 대상 페이지 상세(title, parent) |
| 2-1 | `GET /blocks/{page_id}/children` | 페이지 블록 children (page content) |
| 2-2 | `GET /pages/{id}/markdown` | 페이지 마크다운 (원문 맥락) |
| 2-3 | `GET /databases/{id}` | DB 메타 + data_sources |
| 3-1 | `POST /data_sources/{id}/query` | 데이터 소스 행(페이지) 조회 |
| 3-2 | `GET /comments?block_id={id}` | 페이지 댓글 |
| 3-3 | `GET /blocks/{id}/children` (filter media) | 파일/미디어 블록 URL 추출 |

### `test_p1_readonly.py` (P1, 읽기 전용)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 4-1 | `GET /users` | 사용자/봇 목록 + workspace file size limit |
| 5-1 | `POST /data_sources/{id}/query` | 기본 쿼리 |
| 5-2 | `POST /data_sources/{id}/query` (sorts) | 정렬(created_time desc) |
| 5-3 | `POST /data_sources/{id}/query` (filter) | 필터(past_week) 동작 |
| 6-1 | `POST /search` (filter page) | 페이지 타입 필터 |
| 6-2 | `POST /search` (filter database) | DB 타입 필터 |
| 6-3 | `GET /pages/{id}/markdown?include_transcript=true` | 트랜스크립트 옵션 |

### `test_oauth_token.py` (OAuth)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| O-1 | `GET /users/me` | 토큰 종류 식별 (bot.owner.type: user=OAuth, workspace=Internal) |
| O-2 | `POST /oauth/token` (refresh_token) | refresh_token 갱신 흐름 (OAuth 변수 있을 때) |

### `test_webhooks.py` (제약 확인)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| W-1 | `GET /users/me` | 봇 정체/capability 확인 |
| W-2 | (docs) | Notion REST API webhook 부재 → polling 기반 연동 필요 |

## 결과 해석

- **터미널**: 단계별 `✓`/`✗` + 상태코드 + 핵심 요약(예: "블록 12개"). 마지막에 종합 요약.
- **JSON 리포트**: `results/p0_..._YYYYMMDD_HHMMSS.json` (`.gitignore` 됨, 로컬에서만 조회).

상태코드별 의미:

| 코드 | 의미 | 대응 |
| --- | --- | --- |
| `200`/`201` | 성공 | — |
| `401` | 토큰 무효/만료 | `NOTION_API_KEY` 확인, OAuth access_token 재발급 |
| `403` | 공유 누락 또는 capability 부족 | 페이지/DB 를 connection 에 공유(Add connection) |
| `404` | 리소스 없음 | 페이지/DB ID 또는 공유 범위 확인 |
| `429` | rate limit | 요청 간격 조정 |
| `NET` | 네트워크 오류 | URL/방화벽/VPN 확인 |

> **webhook 미지원은 "실패"가 아니라 "확인된 제약"이다.** Notion REST API 는 동적 webhook
> 등록 엔드포인트를 제공하지 않는다. 변경 감지가 필요하면 `search`/`data_sources query` 를
> 주기적으로 폴링하거나, Notion automation 또는 외부 연결(Zapier/Make 등)을 활용해야 한다.

## 설계 참고

- HTTP 오류가 나도 예외로 중단하지 않고 `(status, error)` 로 기록한다. "어느 엔드포인트가
  권한 부족(403)으로 막히는지"가 검증의 핵심 정보이기 때문이다.
- 토큰은 Internal installation token 이든 OAuth `access_token` 이든 동일한
  `Authorization: Bearer <token>` 헤더로 처리된다 (token-agnostic).
- 원문 URL 매핑: 페이지/DB 모두 `https://www.notion.so/{uuid-no-hyphens}` 형태.
- 데이터가 비어 있어도(0건) 정상 응답이면 ok=True. "지금 데이터가 없을 뿐"인지와
  "API 가 막혀 있는지"를 구분한다.
- 모든 요청에 `Notion-Version` 헤더 필요 (기본 `2026-03-11`).

## 다음 조조사 항목 (필터 문서 연계)

이 테스트 결과로 아래를 확인한다.

- 토큰이 OAuth 기반일 때 workspace 외 사용자 범위, capability 한계
- data_source query 의 filter/sort 가 대시보드용 최소 데이터셋을 커버하는지
- 페이지 마크다운 변환 품질(`<unknown>` 블록 비율) — 외부 동기화 후보
- 파일 블록의 임시 서명 URL 만료(1시간)가 대시보드 표시에 미치는 영향
- webhook 부재를 전제로 polling 주기 설계
