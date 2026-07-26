# A502 API 분석·POC 워크스페이스

## 기본 작업 지침

- 응답과 문서는 정확하고 명확하게 작성한다.
- 셸 명령은 `/Users/kkh/.codex/RTK.md`의 지침에 따라 `rtk`를 우선 사용한다.

## 이 공간의 목적

이 저장소는 실제 SSAFY 프로젝트를 시작하기 전에 다음을 빠르게 검증하기 위한 작업 공간이다.

- SSAFY가 제공하는 API와 외부 도구의 연동 가능성 분석
- 프로젝트 아이디어와 사용자 흐름 구체화
- 핵심 가설을 확인하기 위한 작은 POC 구현

여기서 만든 분석 결과와 POC는 본 프로젝트의 기술·제품 의사결정에 활용한다. 완성도보다 검증 가능성, 재현성, 그리고 다음 단계로 옮기기 쉬운 문서화를 우선한다.

## 문제 배경

SSAFY 교육생은 팀 프로젝트를 진행하며 여러 도구를 함께 사용한다.

- Windows 노트북
- AWS EC2 인스턴스 1대 (`t3.xlarge`)
- Mattermost: 공지와 팀 대화용, self-hosted
- GitLab: `https://lab.ssafy.com/`에 self-hosted
- Jira: `https://ssafy.atlassian.net/`
- Jenkins
- Notion: 팀 공용 문서 저장소로 주로 사용

도구가 분산되어 있어 프로젝트 시작 시 반복 설정 비용이 발생하고, 진행 중에는 여러 알림과 정보를 각각의 서비스에서 찾아야 한다. 필요한 정보의 맥락과 원문 링크도 쉽게 놓칠 수 있다.

## 제품 비전

SSAFY 팀 프로젝트에 필요한 도구와 정보를 한곳에서 연결하는 통합 워크스페이스를 만든다. 초기 설정을 자동화하고, 팀원이 실제로 즉시 확인해야 할 정보만 대시보드와 알림으로 제공한다. 상세 내용은 임의로 복제하지 않고, 해당 도구의 정확한 원문 URL로 자연스럽게 이동할 수 있어야 한다.

## 우선 검증할 기능 가설

1. **팀 생성 자동화**
   - 팀이 확정되면 Mattermost 전용 채널 생성과 webhook 설정을 지원한다.
   - GitLab, Jira, Jenkins, Notion 등 필요한 도구 연결을 빠르게 구성한다.

2. **통합 알림과 대시보드**
   - 여러 도구의 이벤트 중 팀에 중요한 정보만 선별해 한곳에서 확인하게 한다.
   - 알림과 요약에는 원문을 확인할 수 있는 정확한 연관 URL을 제공한다.

3. **프로젝트 운영 지원**
   - 반복되는 팀 활동을 커스텀하거나 자동화하는 기능을 제공한다.
   - 프로젝트 진행에 필요한 핵심 상태와 정보를 빠르게 파악하게 한다.

## 설계 원칙

- 연동 전 API 권한, 인증 방식, webhook 지원 여부, self-hosted 환경의 제약을 먼저 확인한다.
- 외부 서비스의 원문과 권한 체계를 존중한다. 데이터 중복 저장은 꼭 필요한 경우에만 한다.
- 알림은 많이 보내는 것보다 행동 가능한 정보만 정확한 링크와 함께 전달하는 것을 우선한다.
- POC는 작은 단위로 만들고, 가설·제약·검증 결과·후속 결정 사항을 함께 남긴다.
- 실제 SSAFY 제공 인프라와 정책이 달라질 수 있으므로, 확인하지 않은 API 동작이나 권한을 사실처럼 가정하지 않는다.

## 협업 및 문서화

- Notion은 팀의 주 문서 저장소로 사용될 수 있으나, 이 저장소의 분석·POC 결과도 재현 가능하도록 README 또는 관련 문서에 핵심 내용을 기록한다.
- 외부 서비스 주소, 토큰, webhook URL, 사용자 식별 정보 등 민감 정보는 저장소에 커밋하지 않는다.
- 구현이나 연동 제안 시에는 대상 도구, 필요한 권한, 예상 데이터 흐름, 실패·권한 부족 시 동작을 명확히 적는다.

## Mattermost 계정 실효 권한 지도 (실측: 2026-07-25)

> **중요**: Mattermost 권한은 시스템/팀/채널 3계층 역할(role)의 **합집합**이다. 아래는 `GET /api/v4/roles/name/{role}` 실측 결과. 특정 API의 사용 가능 여부는 한 계층 목록이 아니라 세 계층 전체와 대조해 판정할 것. (과거 `system_user` 12개만 보고 웹훅·발송을 "불가"로 오판한 사례 있음 — 실제 UI/API로 웹훅 생성 가능함을 실증으로 확인)

### `system_user` — 시스템 레벨 (계정 자체에 부여)

- `manage_oauth` — OAuth 앱 등록/관리 (본인 생성 앱 한정) → **SSAGY를 MM OAuth 클라이언트로 등록 가능**
- `create_direct_channel` — DM 채널 생성 → 개인 알림 경로
- `create_group_channel` — 그룹 메시지(GM) 채널 생성
- `create_custom_group` / `edit_custom_group` / `delete_custom_group` / `restore_custom_group` / `manage_custom_group_members` — 커스텀 멘션 그룹(`@a502`) 생성·관리
- `view_members` — 멤버 조회
- `join_public_teams` / `list_public_teams` — 공개 팀 목록 조회·가입
- `manage_own_agent` — 본인 AI 에이전트 관리

### `team_user` — 팀 레벨 (팀 가입 시 자동 부여)

- `manage_own_incoming_webhooks` — **Incoming Webhook 생성/관리 (본인 생성분)** → 팀 채널 알림 발송 경로
- `manage_own_outgoing_webhooks` — Outgoing Webhook 생성/관리 (본인 생성분)
- `bypass_incoming_webhook_channel_lock` — 웹훅 발송 시 `channel` 필드로 기본 채널 외 발송 허용 → **웹훅 1개로 여러 채널 커버**
- `manage_own_slash_commands` — 슬래시 명령어(`/ssagy`) 등록/관리 (본인 생성분)
- `create_public_channel` / `create_private_channel` — **채널 자동 생성 가능** (알림 전용 채널)
- `view_team` / `list_team_channels` / `read_public_channel` / `join_public_channels` — 팀·채널 탐색
- `playbook_public_create` / `playbook_private_create` — 플레이북 생성
- `create_emojis` / `delete_emojis` — 커스텀 이모지

### `channel_user` — 채널 레벨 (채널 멤버 시 자동 부여)

- `create_post` — **메시지 발송** (봇/연동 계정의 알림 발송 성립 근거)
- `manage_public_channel_members` / `manage_private_channel_members` — **채널에 팀원 추가/제거** (같은 팀 소속이면 가능)
- `manage_public_channel_properties` / `manage_private_channel_properties` — 채널 이름·헤더·목적 수정
- `use_channel_mentions` / `use_group_mentions` — `@channel`, `@a502` 등 멘션 사용
- `upload_file` / `edit_file_attachment` — 파일 첨부 (리포트 이미지 등)
- `edit_post` / `delete_post` — 본인 게시물 수정·삭제 (발송 알림 갱신에 활용 가능)
- `add_reaction` / `remove_reaction` — 리액션
- `use_slash_commands` — 슬래시 명령어 실행
- `read_channel` / `read_channel_content` / `read_public_channel_groups` / `read_private_channel_groups` — 채널 읽기
- 북마크 관리: `add/edit/delete/order_bookmark_public_channel`, `add/edit/delete/order_bookmark_private_channel`

### 설계에 미치는 결론

- **가능**: 채널 생성(공개/비공개) + 채널 멤버 추가 + incoming/outgoing webhook 생성(own) + 슬래시 명령어(own) + 메시지 발송(`create_post`) + DM/GM 채널 + 커스텀 그룹(@멘션) + OAuth 앱 등록 → **MM 팀 채널·웹훅·알림 초기 세팅 전체를 API로 자동화 가능**
- **불가(여전히)**: 팀 생성(`create_team`), 타인을 팀에 추가(`add_user_to_team`), 타인 웹훅 관리(`manage_others_*`), 타 유저 조작(`edit_other_users`), 시스템 관리(`manage_system`)
- **재검증 필요**: 예약 발송(scheduled post)은 `create_post` 확보로 가능성 있음 — POC에서 확인
- `manage_own_*`은 자기가 만든 리소스만 관리 가능하다는 의미 — 자동화 리소스는 연동 계정 명의로 생성되므로 문제 없으나, **생성자 계정을 DB에 기록**해 연동 계정 교체 시 잔여 리소스 정리가 가능하게 할 것

## GitLab 인스턴스 정보 (`GET /api/v4/metadata` 확인)

- SSAFY GitLab(`lab.ssafy.com`)은 **Community Edition** (`enterprise: false`) 기반이다.
- Enterprise 전용 기능(고급 승인 규칙, Advanced Security 스캔 등)은 이 인스턴스에서 지원되지 않을 수 있으므로, 연동 설계 시 CE 범위 내 기능인지 먼저 확인해야 한다.
