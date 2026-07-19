# Mattermost API 동작 테스트 (POC)

`api-docs/mattermost-api-priority-filter.md` 의 "첫 API 검증 순서"를 실제 PAT 로
호출해 보기 위한 Python 스크립트 모음. 완성도보다 **검증 가능성·재현성**을 우선한다.

> 이 도구는 **읽기 위주(P0/P1)** 와 **쓰기(webhook/posts)** 로 분리되어 있다.
> 실수로 채널에 메시지를 게시하거나 webhook을 생성하는 일을 막기 위해 쓰기 스크립트는
> 별도 파일이며, 실행을 명시적으로 선택해야 한다.

## 구성

| 파일 | 역할 | 쓰기 여부 |
| --- | --- | --- |
| `mattermost_client.py` | 공통: 설정 로드, HTTP 클라이언트, 결과 리포트 | — |
| `test_p0_readonly.py` | P0 1·3단계 GET 검증 (사용자·팀·채널·게시글·스레드·봇·상태·북마크) | 읽기 전용 |
| `test_p1_readonly.py` | P1 GET/POST 검색 (팀/채널/게시글 검색·슬래시 명령·플레이북 가용성) | 읽기 전용 |
| `test_webhooks.py` | incoming webhook 생성 + (옵션)전송 | **쓰기 (webhook 생성, 삭제 X)** |
| `test_posts_write.py` | 채널 게시글·스레드 답글 작성 | **쓰기 (채널에 메시지 게시)** |
| `test_team_channel_ops_readonly.py` | 팀·채널 운영 + 대시보드 집계 (멤버·stats·pinned·unread) | 읽기 전용 |
| `test_reactions_write.py` | 리액션 추가/조회/**삭제** (자체 정리) | **쓰기 (리액션 추가 후 삭제)** |
| `test_file_upload_write.py` | 파일 업로드/메타조회/삭제시도 (**삭제 API 없음**) | **쓰기 (파일 업로드, post 미첨부)** |

## 사전 준비

### 1. Personal Access Token 발급

Mattermost 프로필 > **Settings** > **Security** > **Personal Access Tokens** > Create.

- self-hosted 에서는 관리자가 **Enable Personal Access Tokens: true** 로 설정해야 한다.
- webhook 생성(`manage_webhooks`), 게시글 작성(`create_post`) 권한이 필요할 수 있다.

### 2. 환경변수 설정

```bash
cd mattermost-api-test
cp .env.example .env
# .env 를 열어 아래 값 입력
```

| 변수 | 필수 | 설명 |
| --- | --- | --- |
| `MATTERMOST_BASE_URL` | O | 인스턴스 URL (예: `https://meeting.ssafy.com`). 끝 슬래시 X |
| `MATTERMOST_TOKEN` | O | Personal Access Token |
| `MATTERMOST_TEST_TEAM_ID` | X | 대상 팀 ID. 비우면 소속 첫 팀 자동 탐지 |
| `MATTERMOST_TEST_CHANNEL_ID` | X | 대상 채널 ID. 비우면 일반 채널 자동 탐지. **쓰기 테스트는 전용 채널 권장** |
| `REQUEST_TIMEOUT` | X | 요청 타임아웃(초). 기본 30 |
| `PER_PAGE` | X | 페이지당 항목 수. 기본 60 (최대 200) |
| `MATTERMOST_WEBHOOK_URL` | X | incoming webhook 전체 URL. **설정 시에만** 전송(ping) 테스트 동작 |

> `.env` 는 `.gitignore` 로 커밋되지 않는다. 토큰 등 민감 정보는 절대 저장소에 올리지 말 것.

## 실행

```bash
# 의존성 설치 (최초 1회)
uv sync

# P0 읽기 전용 검증 (안전, GET만)
uv run python test_p0_readonly.py

# P1 검색·가용성 검증 (안전, GET/POST search)
uv run python test_p1_readonly.py

# webhook 생성 + (옵션)전송 (쓰기: webhook 생성, 남겨둠)
uv run python test_webhooks.py

# 게시글/스레드 작성 (쓰기: 채널에 메시지 게시)
uv run python test_posts_write.py

# 팀·채널 운영 + 대시보드 집계 (안전, GET만)
uv run python test_team_channel_ops_readonly.py

# 리액션 추가 후 삭제 (쓰기: 자체 정리, 흔적 남기지 않음)
uv run python test_reactions_write.py

# 파일 업로드 + 메타조회 (쓰기: 삭제 API 없어 post 미첨부 파일이 남음)
uv run python test_file_upload_write.py
```

## 검증 항목 매트릭스

### `test_p0_readonly.py` (P0, 읽기 전용) — 필터문서 "첫 검증 순서" 1·3단계

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 1-1 | `GET /users/me` | 토큰 정체·현재 사용자(id, username, roles) |
| 1-2 | `GET /users/me/teams` | 소속 팀 목록 + 대상 탐지 |
| 1-3 | `GET /teams/{team_id}` | 대상 팀 상세 |
| 1-4 | `GET /users/me/teams/{team_id}/channels` | 팀 채널 목록 (관리자 전용 `/channels` 회피) |
| 1-5 | `GET /channels/{channel_id}` | 대상 채널 상세 |
| 3-1 | `GET /channels/{channel_id}/posts` | 채널 최근 게시글 |
| 3-2 | `GET /posts/{post_id}/thread` | 스레드 조회 |
| 3-3 | `GET /users/me/status` | 현재 사용자 상태 |
| 3-4 | `GET /bots` | bot 계정 가용성 (`read_bots` 권한) |
| 3-5 | `GET /channels/{channel_id}/bookmarks` | 채널 북마크 (v9.5+, 비활성화 시 404) |

### `test_p1_readonly.py` (P1, 읽기 전용)

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| 4-1 | `POST /teams/search` | 팀 검색 권한 |
| 4-2 | `POST /teams/{team_id}/channels/search` | 채널 검색 (팀 스코프) |
| 4-3 | `POST /teams/{team_id}/posts/search` | 게시글 검색 |
| 5-1 | `GET /commands?team_id={team_id}` | 슬래시 명령 목록 |
| 5-2 | `GET /plugins/playbooks/api/v0/playbooks` | 플레이북 가용성 (플러그인, 404 예상 가능) |

### `test_webhooks.py` (쓰기) — incoming webhook 구성

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| W-1 | `GET /hooks/incoming?team_id={team_id}` | 기존 incoming webhook 목록 (`manage_webhooks` 권한) |
| W-2 | `POST /hooks/incoming` | **생성** (channel_id에 webhook). **삭제하지 않음** |
| W-3 | (옵션) `POST {webhook_url}` | `MATTERMOST_WEBHOOK_URL` 설정 시 테스트 메시지 전송(ping) |

> **webhook은 생성 후 삭제하지 않는다.** 통합 서비스가 실제로 사용할 webhook이므로.
> webhook 생성 응답에는 token이 없어 전체 URL을 자동 조립할 수 없다. W-3 전송 테스트는
> Mattermost UI(Integrations > Incoming Webhooks)에서 복사한 전체 URL이 필요하다.

### `test_posts_write.py` (쓰기) — 게시글·스레드 작성

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| P-1 | `POST /posts` | 채널에 테스트 메시지 작성 (`create_post` 권한) |
| P-2 | `POST /posts` (`root_id` 포함) | P-1 글에 대한 스레드 답글 |
| P-3 | `GET /posts/{root_id}/thread` | 작성한 스레드 확인 |

> 메시지는 `[POC-TEST]` 접두어로 식별 가능. 테스트 전용 채널 사용 권장.

### `test_team_channel_ops_readonly.py` (P1, 읽기 전용) — 팀·채널 운영/대시보드 집계

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| C-1 | `GET /channels/{channel_id}/stats` | 채널 멤버 수 (`read_channel`) |
| C-2 | `GET /channels/{channel_id}/members` | 채널 멤버 목록 (msg_count/mention_count 포함) |
| C-5 | `GET /channels/{channel_id}/pinned` | pinned posts (북마크 501 대안) |
| C-6 | `GET /users/me/channels/{channel_id}/unread` | 채널 unread/mention 카운트 |
| C-3 | `GET /teams/{team_id}/stats` | 팀 전체 멤버 수 (`view_team`) |
| C-4 | `GET /teams/{team_id}/members` | 팀 멤버 목록 |
| C-7 | `GET /users/me/teams/{team_id}/unread` | 팀 단위 unread/mention 집계 |

> 대시보드의 핵심 데이터 소스. 북마크(501) 우회용 pinned posts 도 함께 검증.

### `test_reactions_write.py` (쓰기, 자체 정리) — 사용자 상호작용: 리액션

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| R-1 | `GET /posts/{post_id}/reactions` | 사전 리액션 스냅샷 |
| R-2 | `POST /reactions` | 리액션 추가 (`:{white_check_mark}:`, `read_channel`) |
| R-3 | `GET /posts/{post_id}/reactions` | 추가 후 재조회 (반영 확인) |
| R-4 | `DELETE /users/me/posts/{post_id}/reactions/{emoji_name}` | **정리** (원 상태 복구) |

> **흔적을 남기지 않는다.** 추가한 리액션은 반드시 삭제.
> 대상 게시글은 채널의 기존 최근 게시글(새 글 생성 안 함).
> 문서상 정확한 경로: 추가는 `POST /reactions` (단일 엔드포인트 + JSON body),
> 삭제는 `DELETE /users/me/posts/{post_id}/reactions/{emoji_name}`.

### `test_file_upload_write.py` (쓰기) — 사용자 상호작용: 파일 업로드

| 단계 | 엔드포인트 | 검증 목적 |
| --- | --- | --- |
| F-1 | `POST /files` (multipart/form-data) | 작은 텍스트 파일 업로드 (`upload_file`) |
| F-2 | `GET /files/{file_id}/info` | 업로드한 파일 메타데이터 조회 |
| F-3 | `DELETE /files/{file_id}` | 삭제 시도 — **404 = 플랫폼 제약 확인됨** |

> **플랫폼 제약 (실제 호출로 확인):** Mattermost v4 API 는 파일 단독 삭제 엔드포인트를
> 제공하지 않는다. 파일은 post 에 첨부된 뒤 해당 post 가 삭제될 때 함께 삭제되거나,
> 시스템 관리자의 data retention 정책으로만 정리된다. 이 스크립트는 업로드 + 메타
> 조회까지만 수행한다. 업로드한 파일은 post 에 첨부하지 않았으므로 사용자에게 노출되지
> 않는다. 통합 서비스 설계 시 업로드 파일은 반드시 post 와 묶어 관리해야 한다.
> multipart 처리는 `mattermost_client.MattermostClient.upload_file()` 가 담당.

## 결과 해석

- **터미널**: 단계별 `✓`/`✗` + 상태코드 + 핵심 요약. 마지막에 종합 요약.
- **JSON 리포트**: `results/p0_..._YYYYMMDD_HHMMSS.json` (`.gitignore` 됨, 로컬만).

상태코드별 의미:

| 코드 | 의미 | 대응 |
| --- | --- | --- |
| `200/201` | 성공 | — |
| `401` | 토큰 무효·만료 | 토큰 재발급 |
| `403` | 권한 부족 | permission 확인 (`manage_webhooks`, `read_bots`, `create_post` 등) |
| `404` | 리소스 없음 / 기능 비활성화 | team/channel ID 확인, 북마크(버전<9.5)·플레이북(플러그인) 비활성화 가능 |
| `NET` | 네트워크 오류 | URL/방화벽/VPN 확인 |

## 설계 참고

- HTTP 오류가 나도 예외로 중단하지 않고 `(status, error)` 로 기록한다. "어느 엔드포인트가
  권한 부족(403)으로 막히는지"가 검증의 핵심 정보이기 때문이다.
- 인증: `Authorization: Bearer <PAT>`. user_id 자리에 `me` 리터럴 사용.
- 전체 채널 조회 `GET /channels`는 시스템 관리자 전용 → 사용자 스코프 `GET /users/me/teams/{team_id}/channels` 사용.
- posts 응답은 `{order: [post_ids], posts: {id: post}}` 구조.
- **webhook은 남겨둔다.** 통합 서비스의 실제 연동 수단.
- 원문 URL 매핑: 채널 `/{team}/channels/{channel}`, 스레드 `/{team}/pl/{post_id}`.

## 다음 조사 항목 (필터 문서 연계)

- PAT 계정의 실제 권한 범위 (`manage_webhooks`, `create_post`, `read_bots`)
- incoming webhook 으로 GitLab/Jira/Jenkins 이벤트를 전용 채널에 전달하는 payload 형식 확정
- 슬래시 명령(`/project-status` 등) 등록 권한과 보안 검토
- 플레이북/예약 게시 기능의 인스턴스 활성화 여부
- bot 계정을 통한 알림 발신자 분리 가능성
