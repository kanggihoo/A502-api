# Jira Cloud API 동작 테스트 (POC)

`api-docs/jira-api-priority-filter.md` 의 "첫 API 검증 순서"를 실제 PAT 로
호출해 보기 위한 Python 스크립트 모음. 완성도보다 **검증 가능성·재현성**을 우선한다.

> 이 도구는 **읽기 위주(P0/P1)** 와 **webhook 권한 검증** 세 스크립트로 분리되어 있다.
> 실수로 쓰기 작업이 실행되는 일을 막기 위해 webhook 테스트는 별도 파일이며,
> 이 스크립트는 GET 조회 시도만 한다(POST 생성은 하지 않는다).

## 구성

| 파일 | 역할 | 쓰기 여부 |
| --- | --- | --- |
| `jira_client.py` | 공통: 설정 로드, HTTP 클라이언트, 결과 리포트 | — |
| `test_p0_readonly.py` | P0 1~3단계 GET 검증 (사용자·프로젝트·JQL검색·이슈·댓글·remote link·필터) | 읽기 전용 |
| `test_p1_readonly.py` | P1 읽기 후보 GET/POST 검증 (상태·우선순위·이슈타입·컴포넌트·버전·대시보드·JQL parse) | 읽기 전용 |
| `test_webhooks.py` | webhook 권한 검증 (GET /webhook 시도, 403 예상) | **조회 시도만** |

## 사전 준비

### 1. OAuth 2.0 Access Token 및 Cloud ID 준비

Atlassian OAuth 2.0 (3LO) 흐름을 통해 Access Token과 Cloud ID를 미리 준비해야 합니다.

- Access Token: `Authorization: Bearer <TOKEN>` 형태로 인증을 통과하기 위한 토큰입니다.
- Cloud ID: API 요청 대상 Jira 인스턴스를 지정하기 위한 UUID 식별자이며, `https://api.atlassian.com/oauth/token/accessible-resources` 조회를 통해 가져올 수 있습니다.

### 2. 환경변수 설정

```bash
cd jira-api-test
cp .env.example .env
# .env 를 열어 아래 값 입력
```

| 변수 | 필수 | 설명 |
| --- | --- | --- |
| `JIRA_BASE_URL` | O | 웹 브라우저용 원문 이동 링크 생성을 위한 베이스 URL (예: `https://ssafy.atlassian.net`). 끝 슬래시 X |
| `JIRA_OAUTH_TOKEN` | O | OAuth 2.0 Access Token |
| `JIRA_CLOUD_ID` | O | API 요청용 Jira Cloud ID (UUID) |
| `JIRA_TEST_PROJECT_KEY` | X | 대상 프로젝트 키(예: `S15P11A502`). 비우면 자동 탐지 |
| `REQUEST_TIMEOUT` | X | 요청 타임아웃(초). 기본 30 |
| `MAX_RESULTS` | X | 페이지당 최대 항목 수. 기본 50 |

> `.env` 는 `.gitignore` 로 커밋되지 않는다. 토큰·이메일 등 민감 정보는 절대 저장소에 올리지 말 것.

## 실행

```bash
# 의존성 설치 (최초 1회)
uv sync

# P0 읽기 전용 검증 (안전, GET만)
uv run python test_p0_readonly.py

# P1 읽기 후보 검증 (안전, GET/JQL parse)
uv run python test_p1_readonly.py

# webhook 권한 검증 (GET 시도만, 403 예상)
uv run python test_webhooks.py
```

## 검증 항목 매트릭스

### `test_p0_readonly.py` (P0, 읽기 전용) — 필터문서 "첫 검증 순서" 1~3단계

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 1-1 | `GET https://api.atlassian.com/me` | 토큰 정체·현재 사용자(accountId) 확인 |
| 1-2 | `GET /project/search` | 접근 가능 프로젝트 + 대상 탐지 |
| 1-3 | `GET /project/{key}` | 대상 프로젝트 상세(lead, issueTypes) |
| 2-1 | `POST /search/jql` | 내 할 일 (JQL) |
| 2-2 | `POST /search/jql` | 프로젝트 이슈 현황 |
| 2-3 | `GET /issue/{key}` | 대표 이슈 상세(필드 구조) |
| 3-1 | `GET /issue/{key}/comment` | 이슈 댓글 |
| 3-2 | `GET /issue/{key}/remotelink` | 외부 링크(GitLab MR/배포 URL 연결 후보) |
| 3-3 | `GET /filter/favourite` | 즐겨찾기 필터(저장 JQL 재사용 후보) |

### `test_p1_readonly.py` (P1, 읽기 전용)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 4-1 | `GET /priority` | 우선순위 |
| 4-2 | `GET /issuetype` | 이슈 타입 |
| 5-1 | `GET /component?projectIds={key}` | 프로젝트 컴포넌트(기능 영역) |
| 5-2 | `GET /project/{key}/versions` | 프로젝트 버전(배포 버전) |
| 6-1 | `GET /dashboard` | 대시보드 목록 |
| 6-2 | `POST /jql/parse` | JQL 유효성 사전 점검(저장 전 검증) |

### `test_webhooks.py` (권한 검증)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| W-1 | `GET /webhook` | 동적 웹훅 목록 조회 **시도**. 403 예상 → PAT 로는 웹훅 API 불가, Connect/Forge/OAuth 앱 필요 |

## 결과 해석

- **터미널**: 단계별 `✓`/`✗` + 상태코드 + 핵심 요약(예: "이슈 12개"). 마지막에 종합 요약.
- **JSON 리포트**: `results/p0_..._YYYYMMDD_HHMMSS.json` (`.gitignore` 됨, 로컬에서만 조회).

상태코드별 의미:

| 코드 | 의미 | 대응 |
| --- | --- | --- |
| `200` | 성공 | — |
| `401` | 토큰/이메일 무효·만료 | 토큰 재발급, 이메일 확인 |
| `403` | 권한 부족 | 앱 권한(scope) 또는 Connect/Forge 앱 필요. 특히 webhook |
| `404` | 리소스 없음 | 프로젝트 키/이슈 키 확인 |
| `NET` | 네트워크 오류 | URL/방화벽/VPN 확인 |

> **webhook 403은 "실패"가 아니라 "확인된 제약"이다.** PAT(Basic Auth)는 사용자 계정
> 권한을 가지지만, `/rest/api/3/webhook` 은 Connect/OAuth 2.0 앱 전용이다. 실시간
> 이벤트 수신이 필요하면 Forge/Connect 앱 등록 또는 OAuth 2.0 연동이 필요하다.

## 설계 참고

- HTTP 오류가 나도 예외로 중단하지 않고 `(status, error)` 로 기록한다. "어느 엔드포인트가
  권한 부족(403)으로 막히는지"가 검증의 핵심 정보이기 때문이다.
- Atlassian Cloud PAT 인증: `email:token` 의 HTTP Basic Auth.
- JQL 에서 `username`/`userkey` 는 privacy 상 사용할 수 없다 → `accountId` 또는 `currentUser()`.
- 원문 URL 매핑: 이슈는 `{base}/browse/{key}`, 프로젝트는 `{base}/jira/software/c/projects/{key}/boards`.

## 다음 조사 항목 (필터 문서 연계)

이 테스트 결과로 아래를 확인한다.

- PAT 계정의 실제 프로젝트 권한 범위(Browse projects 등)
- remote link 로 GitLab MR/배포 URL 을 Jira 이슈에 연결하는 방식 확정
- 저장 필터(favourite filter) 공유 권한과 재사용 가능성
- webhook 이 PAT 로 불가한 것을 확인했다면, Forge/Connect 앱 또는 OAuth 2.0 연동 경로 결정
