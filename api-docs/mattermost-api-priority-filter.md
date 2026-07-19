# Mattermost API 우선 검토 카테고리

## 분류 기준

`mattermost_defuddle_markdown`의 디렉터리명만으로 만든 1차 필터다. 문서 본문·엔드포인트·최소 권한은 확인하지 않았다. 팀 채널 생성과 webhook 사용 가능성은 들은 정보가 있으나, 실제 self-hosted 인스턴스 정책과 팀 내 역할에 따라 달라질 수 있다.

단, 아래의 “확인된 제약”은 디렉터리 구조 추론이 아니라 실제 `meeting.ssafy.com` 호출 결과다.

## 우선 시도할 API 카테고리

### P0 — 팀 채널, 알림, 대화 맥락

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `03-users`, `05-teams`, `06-channels` | 현재 사용자·팀·채널 정보를 조회하고 팀/채널 단위 작업을 수행한다. | 연결한 사용자의 소속을 확인하고, 팀 전용 채널을 찾거나 생성 가능 여부를 검증한다. 팀 자체 생성은 권한을 전제로 하지 않는다. |
| `07-posts`, `49-threads`, `16-reactions` | 게시글·스레드·리액션을 조회·작성한다. | GitLab/Jira 이벤트를 하나의 스레드로 묶어 알리고, 팀 반응을 확인한다. |
| `17-webhooks` | 외부 시스템과 Mattermost 사이의 webhook 흐름을 구성한다. | GitLab/Jira/Jenkins 이벤트를 전용 채널에 전달하는 최우선 연동 수단이다. |

### P1 — 팀 운영 편의 기능

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `08-files`, `09-uploads` | 파일과 업로드 흐름을 다룬다. | 배포 결과·테스트 산출물의 공유를 보조한다. 대용량 파일 저장소로 쓰지는 않는다. |
| `18-commands`, `33-integration-actions` | 슬래시 명령과 외부 연동 액션을 다룬다. | `/project-status` 같은 빠른 상태 조회를 제공할 후보이다. 등록 권한과 보안 검토가 필요하다. |
| `65-scheduled-post`, `42-playbooks`, `43-playbookruns` | 예약 게시와 반복 운영 절차를 다룬다. | 데일리 체크, 마감 알림, 배포 체크리스트 자동화에 쓸 수 있다. 인스턴스 기능 활성화 여부를 확인한다. |
| `12-boards`, `40-recaps` | 보드와 대화 요약 기능을 다룬다. | Mattermost를 업무 보드로 함께 쓰는 팀에만 검토한다. Jira를 주 업무 도구로 쓸 경우 연동/링크 중심이 적절하다. |
| `52-search`, `15-emoji` | 검색과 사용자 표현 기능을 다룬다. | 과거 공지·배포 메시지 탐색과 알림 UX 개선에 보조적으로 사용한다. |

## 관리자·인스턴스 운영 영역으로 제외한 카테고리

| 제외 카테고리 | 제외 이유 |
| --- | --- |
| `19-system`, `54-root`, `26-cluster`, `55-remote-clusters`, `56-cloud` | Mattermost 인스턴스·클러스터·클라우드 운영 영역으로 교육생 권한 밖이다. |
| `23-ldap`, `22-saml`, `21-oauth`, `48-authentication`, `64-outgoing-oauth-connections` | 중앙 인증 및 OAuth 연결을 변경하며, 시스템 관리자 권한과 보안 검토가 필요하다. |
| `58-permissions`, `31-roles`, `32-schemes`, `67-access-control`, `24-groups` | 전역 권한 체계·역할·접근 제어를 변경할 수 있어 팀 운영 서비스가 대신 다루지 않는다. |
| `39-audit-logs`, `25-compliance`, `28-data-retention`, `37-exports`, `36-imports`, `47-migrate` | 감사·보존·내보내기·마이그레이션은 조직 데이터 관리 영역이다. |
| `20-brand`, `30-plugins`, `38-metrics`, `61-reports`, `62-logs`, `29-jobs`, `57-usage` | 브랜딩·플러그인·운영 지표·로그·백그라운드 작업은 시스템 운영자 영역이다. |
| `27-elasticsearch`, `59-ip`, `63-outgoing-connections`, `66-custom-profile-attributes`, `68-content-flagging`, `69-properties`, `70-conditions` | 검색 인프라·네트워크·전역 속성/정책에 영향을 줄 수 있어 초기 범위에서 제외한다. |

## 확인된 제약 및 초기 제품에서 제외할 사용자 영역

| 카테고리 | 확인 결과 또는 제외 이유 | 제품 결정 |
| --- | --- | --- |
| `04-bots` | `GET /bots`가 **403**(권한 부족)으로 실패했다. 봇 목록을 읽을 권한조차 확인되지 않았으므로 봇 계정 가용성을 전제할 수 없다. | 알림 발신은 허용된 incoming webhook 또는 연결 사용자의 권한으로만 설계한다. 봇 관련 기능은 필요한 권한이 확인되기 전까지 제외한다. |
| `10-bookmarks` | `GET /channels/{channel_id}/bookmarks`가 **501**로 실패했고, 응답은 현재 라이선스에서 채널 북마크를 지원하지 않는다고 명시했다. | 채널 북마크를 공통 링크 허브로 사용하지 않는다. 대시보드의 링크 모음과 고정 게시글 대안을 사용한다. |
| `13-preferences`, `11-views`, `60-filtering`, `50-drafts` | 개인 화면·환경설정·임시 작성 데이터는 개인 작업 공간에 해당한다. | 통합 서비스가 읽거나 변경하지 않는다. 알림 필터는 서비스 내부 설정으로 제공한다. |

## 첫 검증 순서

1. `03-users` → `05-teams` → `06-channels`로 토큰의 소속과 채널 생성/조회 범위를 확인한다.
2. `17-webhooks` 또는 허용된 incoming webhook으로 테스트 메시지를 전송한다.
3. `07-posts`와 `49-threads`로 GitLab 이벤트를 스레드 단위로 작성하고 원문 URL을 연결한다.
4. `18-commands`, `33-integration-actions`, `65-scheduled-post`의 사용 가능 여부를 확인해 빠른 조회와 스크럼 리마인더 기능으로 확장한다. `04-bots`와 `10-bookmarks`는 확인된 403/501 제약이 해소되기 전까지 검증 대상에서 제외한다.

## 다음 조사에서 확인할 항목

- incoming webhook 생성·조회·삭제 권한과, GitLab/Jira/Jenkins에서 `meeting.ssafy.com` 수신 주소로 전송 가능한 네트워크 조건
- 채널 생성·멤버 초대 권한이 팀 관리자에게 있는지와, 이미 제공된 팀/채널을 선택하는 대체 흐름
- 슬래시 명령·integration actions·scheduled post·playbooks의 라이선스와 팀 단위 등록 권한
- 서비스 알림용 webhook의 채널별 관리·회전·폐기 절차 및 Secret을 저장소에 남기지 않는 방식
