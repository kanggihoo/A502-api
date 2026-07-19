# GitLab API 동작 테스트 (POC)

`api-docs/gitlab-api-priority-filter.md` 의 "첫 API 검증 순서"를 실제 토큰으로
호출해 보기 위한 Python 스크립트 모음. 완성도보다 **검증 가능성·재현성**을 우선한다.

> 이 도구는 **읽기 위주(P0)** 와 **webhook 쓰기** 두 스크립트로 분리되어 있다.
> 실수로 쓰기 작업이 실행되는 일을 막기 위해 webhook 테스트는 별도 파일이며,
> 추가로 `WEBHOOK_TEST_URL` 환경변수가 설정된 경우에만 동작한다.

## 구성

| 파일 | 역할 | 쓰기 여부 |
| --- | --- | --- |
| `gitlab_client.py` | 공통: 설정 로드, HTTP 클라이언트, **PAT/OAuth2 인증**, 결과 리포트 | — |
| `test_oauth2_tokens.py` | OAuth2 access_token 유효성·수동 refresh 동작 검증 | 읽기(토큰 갱신) |
| `test_p0_readonly.py` | P0 1~2단계 GET 검증 (사용자·프로젝트·멤버·MR·이슈·파이프라인·이벤트·할 일·webhook 조회) | 읽기 전용 |
| `test_p1_readonly.py` | P1 읽기 후보 GET 검증 (브랜치·보호규칙·커밋·라벨·마일스톤·릴리스·배포환경·통합·webhook) | 읽기 전용 |
| `test_review_discussion_readonly.py` | MR 참여자·리뷰어·승인상태·토론·댓글 (리뷰 맥락 집계) | 읽기 전용 |
| `test_security_readonly.py` | 보호 태그·보호 환경·push 규칙 (보안 진단) | 읽기 전용 |
| `test_cicd_readonly.py` | CI 트리거·스케줄·변수·파이프라인·잡 (비밀값 마스킹) | 읽기 전용 |
| `test_search_content_readonly.py` | 프로젝트/코드/MR 검색·저장소 트리·README 원문 | 읽기 전용 |
| `test_webhooks.py` | 3단계 webhook 생성·조회·삭제 | **쓰기(Maintainer 전제)** |

## 사전 준비

### 1. 인증 방식 선택 (PAT 또는 OAuth2)

`.env` 의 `GITLAB_AUTH_METHOD` 로 선택. 두 방식 모두 동일한 API 호출 결과를 준다
(GitLab 은 토큰 종류가 아니라 역할·scope 로 권한을 결정).

#### A. PAT 모드 (기본값, 1회성 스크립트·디버그용)

GitLab 프로필 > Access Tokens 에서 발급.

- **읽기 전용(P0~검색)**: scope `read_api`, `read_user`, `read_repository`
- **webhook 쓰기 추가**: scope `api` + Maintainer(40) 역할

`.env`:
```dotenv
GITLAB_AUTH_METHOD=pat
GITLAB_TOKEN=<발급받은 PAT>
```

#### B. OAuth2 모드 (제품용, priority-filter.md 의 권장 방향)

GitLab UI > User Settings > Applications 에서 사용자 수준 OAuth 앱 등록 후,
**Postman** 등으로 Authorization Code + PKCE flow 를 거쳐 토큰을 받는다.
발급받은 access_token / refresh_token 을 `.env` 에 넣는다.

- **scope 권장**: `read_api` (읽기 대시보드) → 필요 시 `api` (쓰기, 팀장만)
- access_token 기본 만료 **2시간(7200초)**. 만료(401) 시 `gitlab_client.py` 가
  refresh_token 으로 **자동 갱신(1회)** 하고 `.env` 의 토큰을 덮어쓴다.
  (GitLab refresh 는 rotate-on-use 라 영속화가 필수.)
- PAT 와 달리 만료 시 사용자 개입 없이 백엔드가 `refresh_token` 으로 갱신 가능.

`.env`:
```dotenv
GITLAB_AUTH_METHOD=oauth2
GITLAB_OAUTH_CLIENT_ID=<앱 Application ID>
GITLAB_OAUTH_CLIENT_SECRET=<앱 secret (Confidential 앱만)>
GITLAB_OAUTH_REDIRECT_URI=<Postman flow 의 callback URL 과 일치>
GITLAB_OAUTH_ACCESS_TOKEN=<Postman 에서 받은 access_token>
GITLAB_OAUTH_REFRESH_TOKEN=<Postman 에서 받은 refresh_token>
```

> PAT/OAuth2 전환은 `.env` 의 `GITLAB_AUTH_METHOD` 와 해당 토큰 값만 바꾸면 된다.
> 나머지 스크립트는 인증 방식을 의식하지 않고 동일하게 동작한다.

### 2. 환경변수 설정

```bash
cd gitlab-api-test
cp .env.example .env
# .env 를 열어 위 A 또는 B 값을 입력
```

| 변수 | 필수 | 설명 |
| --- | --- | --- |
| `GITLAB_BASE_URL` | O | 인스턴스 URL (예: `https://lab.ssafy.com`). 끝 슬래시 X |
| `GITLAB_AUTH_METHOD` | O | `pat` (기본) 또는 `oauth2` |
| `GITLAB_TOKEN` | PAT 시 O | Personal Access Token |
| `GITLAB_OAUTH_ACCESS_TOKEN` | OAuth2 시 O | access_token (Bearer) |
| `GITLAB_OAUTH_REFRESH_TOKEN` | OAuth2 갱신 시 | 자동 갱신용 refresh_token |
| `GITLAB_OAUTH_CLIENT_ID` | OAuth2 갱신 시 | 앱 Application ID |
| `GITLAB_OAUTH_CLIENT_SECRET` | OAuth2 갱신 시 | Confidential 앱의 secret |
| `GITLAB_OAUTH_REDIRECT_URI` | OAuth2 갱신 시 | refresh 시 원래 auth 요청과 일치해야 함 |
| `GITLAB_TEST_PROJECT_ID` | X | 대상 프로젝트 ID 또는 URL-encoded path. 비우면 자동 탐지 |
| `REQUEST_TIMEOUT` | X | 요청 타임아웃(초). 기본 30 |
| `PER_PAGE` | X | 페이지당 항목 수. 기본 20 |
| `WEBHOOK_TEST_URL` | X | webhook 수신 URL. **설정한 경우에만** webhook 쓰기 테스트 동작 |

> `.env` 는 `.gitignore` 로 커밋되지 않는다. 토큰·URL 등 민감 정보는 절대 저장소에 올리지 말 것.
> OAuth2 자동 갱신이 `.env` 의 access/refresh token 값을 덮어쓰므로, `.env` 가 쓰기 가능한 상태여야 한다.

## 실행

```bash
# 의존성 설치 (최초 1회)
uv sync

# (OAuth2 모드) 토큰 유효성 + 자동 refresh 동작 먼저 확인
uv run python test_oauth2_tokens.py

# P0 읽기 전용 검증 (안전, GET만)
uv run python test_p0_readonly.py

# P1 읽기 후보 검증 (안전, GET만)
uv run python test_p1_readonly.py

# 리뷰·토론 맥락 집계 (안전, GET만)
uv run python test_review_discussion_readonly.py

# 보안·보호규칙 진단 (안전, GET만)
uv run python test_security_readonly.py

# CI/CD 자동화 후보 진단 (안전, GET만, 비밀값 마스킹)
uv run python test_cicd_readonly.py

# 검색·콘텐츠 조회 (안전, GET만)
uv run python test_search_content_readonly.py

# webhook 생성·삭제 검증 (WEBHOOK_TEST_URL 설정 시만 동작)
uv run python test_webhooks.py
```

## 검증 항목 매트릭스

### `test_oauth2_tokens.py` (OAuth2 모드 전용) — 토큰 상태·갱신

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| O-1 | `GET /user` (`Authorization: Bearer`) | access_token 유효성 |
| O-2 | `POST /oauth/token` (`grant_type=refresh_token`) | 수동 refresh + rotate-on-use 동작 |
| O-3 | `GET /user` (새 access_token) | 갱신 후 토큰 유효성 재확인 |

> PAT 모드에서는 실행할 필요 없음. OAuth2 모드에서만 동작.
> O-2 성공 시 `.env` 의 `GITLAB_OAUTH_ACCESS_TOKEN`/`REFRESH_TOKEN` 이 자동 덮어쓰기됨.

### `test_p0_readonly.py` (P0, 읽기 전용)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 1-1 | `GET /user` | 토큰 정체·현재 사용자 확인 |
| 1-2 | `GET /projects?membership=true` | 접근 가능 프로젝트 + 대상 탐지 |
| 1-3 | `GET /projects/{id}` | 대상 프로젝트 상세 |
| 1-4 | `GET /projects/{id}/members/all` | 팀 멤버·역할(Maintainer/Developer 수) |
| 1-5 | `GET /groups` | 그룹 구조(반/팀) 존재 여부 |
| 2-1 | `GET /projects/{id}/merge_requests?state=opened` | 리뷰 대기 MR |
| 2-2 | `GET /issues?scope=all&state=opened` | 이슈 현황(사용자 단위) |
| 2-3 | `GET /projects/{id}/issues?state=opened` | 프로젝트 단위 이슈 |
| 2-4 | `GET /projects/{id}/pipelines` | 최근 파이프라인 상태 |
| 2-5 | `GET /events` | 사용자 활동 이벤트 |
| 2-6 | `GET /todos` | 할 일 |
| 2-7 | `GET /projects/{id}/hooks` | 기존 webhook 목록(조회만) |

### `test_p1_readonly.py` (P1, 읽기 전용)

모두 프로젝트 스코프(`/projects/{id}/...`). 타팀 데이터 노출 방지.

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 3-1 | `GET /projects/{id}/repository/branches` | 브랜치 목록·기본 브랜치·보호여부 |
| 3-2 | `GET /projects/{id}/protected_branches` | 보호 브랜치 규칙(push/merge 권한) |
| 3-3 | `GET /projects/{id}/repository/commits` | 최근 커밋 활동 |
| 4-1 | `GET /projects/{id}/labels` | 라벨(역할별 업무 분류) |
| 4-2 | `GET /projects/{id}/milestones` | 마일스톤(스프린트) |
| 5-1 | `GET /projects/{id}/releases` | 릴리스(배포 태그) |
| 5-2 | `GET /projects/{id}/environments` | 배포 환경(EC2 등 상태) |
| 6-1 | `GET /projects/{id}/integrations` | 활성 통합(Jenkins/Jira/Mattermost 연결 상태) |
| 6-2 | `GET /projects/{id}/hooks` | webhook 목록(폴링 vs webhook 비교, P1 관점) |

### `test_review_discussion_readonly.py` (읽기 전용) — 리뷰·토론 맥락 집계

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| R-1 | `GET /projects/{id}/merge_requests?state=opened` | 대상 MR iid 확보 |
| R-2 | `GET /projects/{id}/merge_requests/{iid}/participants` | MR 참여자 |
| R-3 | `GET /projects/{id}/merge_requests/{iid}/reviewers` | MR 리뷰어 (`{user, state}` 중첩 구조) |
| R-4 | `GET /projects/{id}/merge_requests/{iid}/approvals` | MR 승인 상태(요약: `approved_by`) |
| R-5 | `GET /projects/{id}/merge_requests/{iid}/discussions` | MR 토론 스레드 |
| R-6 | `GET /projects/{id}/merge_requests/{iid}/notes` | MR 댓글 |

> opened MR 이 없으면 R-2~R-6 을 "스킵" 으로 개별 기록. MR 이 있는 프로젝트로
> `GITLAB_TEST_PROJECT_ID` 변경 시 정상 동작.
> 문서상 주의: `approvals`(요약) 와 `approval_state`(상세·rules) 가 이름 반대.

### `test_security_readonly.py` (읽기 전용) — 보안·보호규칙 진단

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| S-1 | `GET /projects/{id}/protected_tags` | 보호 태그 (전 에디션) |
| S-2 | `GET /projects/{id}/protected_environments` | 보호 환경 (**Premium/Ultimate → 403 예상**) |
| S-3 | `GET /projects/{id}/push_rule` | push 규칙 (**단수형**, Premium/Ultimate → 403 예상) |

> 403 은 "에디션/권한 제약" 으로 해석해 summary 에 원인 명시. 자동 변경은 수행하지 않는다.
> 보호 브랜치는 `test_p1_readonly.py` 3-2 에서 이미 검증해 여기서는 제외.

### `test_cicd_readonly.py` (읽기 전용) — CI/CD 자동화 후보 진단

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| C-1 | `GET /projects/{id}/triggers` | CI 트리거 토큰 (**token 마스킹**) |
| C-2 | `GET /projects/{id}/pipeline_schedules` | 정기 실행 스케줄 |
| C-3 | `GET /projects/{id}/variables` | CI 변수 (**value 마스킹/생략**) |
| C-4 | `GET /projects/{id}/pipelines` | 최근 파이프라인 (대상 확보) |
| C-5 | `GET /projects/{id}/pipelines/{pipeline_id}` | 파이프라인 상세 (있을 때만) |
| C-6 | `GET /projects/{id}/pipelines/{pipeline_id}/jobs` | 파이프라인 잡 목록 (있을 때만) |

> **★ 비밀값 마스킹**: 트리거 `token` 과 변수 `value` 는 평문 비밀값. sample 에 절대
> 평문으로 담지 않고 메타데이터(id/key/protected/masked/environment_scope 등)만 기록.
> 잡 로그(trace)는 대용량·비밀값 노출 위험으로 이번 검증에서 의도적 제외.

### `test_search_content_readonly.py` (읽기 전용) — 검색·콘텐츠 조회

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| Q-1 | `GET /projects/{id}/search?scope=blobs&search=README` | 프로젝트 내 코드 검색 |
| Q-2 | `GET /projects/{id}/search?scope=merge_requests&search=test` | 프로젝트 내 MR 검색 |
| Q-3 | `GET /projects/{id}/repository/tree` | 저장소 트리(최상위 파일/디렉토리) |
| Q-4 | `GET /projects/{id}/repository/files/README.md/raw` | README 원문 (앞부분 미리보기만) |
| Q-5 | `GET /search?scope=projects&search={프로젝트명}` | 전역 프로젝트 검색 |

> 검색 결과 0건도 ok=True. README 원문은 전체 본문을 담지 않고 앞부분만 잘라 저장.
> 코드 검색은 `/projects/{id}/search?scope=blobs` 사용. `34-code-search/` 디렉터리는
> Zoekt 인덱스 관리(admin) 용도이므로 사용하지 않는다.

### `test_webhooks.py` (3단계, 쓰기)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| W-1 | `GET /projects/{id}/hooks` | 기존 webhook에서 동일 URL 탐색(중복 생성 방지) |
| W-2 | `POST /projects/{id}/hooks` | push/MR/이슈/pipeline/job/note 이벤트 webhook 생성 |
| W-3 | `GET /projects/{id}/hooks/{hook_id}` | 생성(또는 재사용) webhook 단건 확인 |
| W-4 | `DELETE /projects/{id}/hooks/{hook_id}` | 항상 삭제 시도(정리) |

## 결과 해석

- **터미널**: 단계별 `✓`/`✗` + 상태코드 + 핵심 요약(예: "MR opened: 3"). 마지막에 종합 요약.
- **JSON 리포트**: `results/gitlab_api_test_YYYYMMDD_HHMMSS.json` (`.gitignore` 됨, 로컬에서만 조회).

상태코드별 의미:

| 코드 | 의미 | 대응 |
| --- | --- | --- |
| `200` | 성공 | — |
| `401` | 토큰 무효/만료 | 토큰 재발급 |
| `403` | 권한 부족 | scope 또는 역할(Maintainer/Developer) 확인. 필터 문서의 "시도 가능 ≠ 권한 보장" 참고 |
| `404` | 리소스 없음 | 프로젝트 ID/경로 확인 |
| `NET` | 네트워크 오류 | URL/방화벽/VPN 확인 |

## 설계 참고

- HTTP 오류가 나도 예외로 중단하지 않고 `(status, error)` 로 기록한다. "어느 엔드포인트가
  권한 부족(403)으로 막히는지"가 검증의 핵심 정보이기 때문이다.
- 프로젝트 식별자가 경로 형식(`group/sub/project`)이면 슬래시를 `%2F` 로 인코딩해 URL path 에 넣는다.
- access_level 해석: `30` Developer, `40` Maintainer, `50` Owner. SSAFY 팀 구성
  가정(팀장 Maintainer 1 + 팀원 Developer N)을 1-4 요약에서 확인할 수 있다.

## 다음 조사 항목 (필터 문서 연계)

이 테스트 결과로 아래를 확인한다.

- `lab.ssafy.com` GitLab 버전·에디션
- PAT 허용 scope와 만료 정책
- Maintainer / Developer 별 실제 응답 차이
- 프로젝트 webhook 생성 권한, 수신 네트워크 제약, Secret Token 지원 여부
- 그룹이 SSAFY 관리자 소유인지, 팀장이 그룹 Owner인지
