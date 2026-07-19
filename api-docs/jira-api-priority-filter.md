# Jira Cloud v3 API 우선 검토 카테고리

## 분류 기준

`jira_v3_defuddle_markdown`의 디렉터리명만으로 작성한 1차 필터다. Jira의 프로젝트 권한, 앱 권한, 전역 관리자 권한은 구분이 엄격하므로 실제 토큰과 대상 프로젝트에서 읽기 호출부터 검증해야 한다.

## 우선 시도할 API 카테고리

### P0 — 업무 현황과 개인 할 일

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `57-myself`, `90-users`, `89-user-search`, `14-group-and-user-picker` | 현재 사용자와 사용자 검색 정보를 다룬다. | 연결 계정 확인, 담당자 표시, 팀원 매핑의 기반으로 사용한다. 전 사용자 관리 기능은 포함하지 않는다. |
| `76-projects` | 프로젝트를 조회하고 프로젝트 관련 작업을 다룬다. | 팀 Jira 프로젝트를 식별해 대시보드의 기준 링크와 데이터 범위를 결정한다. |
| `49-issues`, `38-issue-search`, `50-jql` | 이슈와 검색/JQL을 다룬다. | 내 할 일, 미배정 이슈, 마감 임박, 상태별 작업을 대시보드에 보여 주는 핵심 기능이다. |
| `83-status`, `95-workflow-status-categories`, `37-issue-resolutions` | 이슈 상태, 워크플로 상태 분류, 해결 상태를 다룬다. | 팀마다 이름이 다른 상태를 대시보드에서 `할 일`·`진행 중`·`완료` 같은 공통 진행 상태로 표시할 수 있는지 확인한다. 실제 상태 전환이나 워크플로 변경은 하지 않는다. |
| `19-issue-comments`, `16-issue-attachments`, `36-issue-remote-links`, `29-issue-links` | 이슈의 댓글·첨부·외부 링크·연결 관계를 다룬다. | GitLab MR·배포 URL을 Jira 이슈 맥락과 연결하고, 상세 내용은 Jira 원문으로 이동시킨다. |
| `46-issue-watchers`, `45-issue-votes`, `48-issue-worklogs`, `86-time-tracking` | 구독자·관심도·작업 기록·시간을 다룬다. | 개인 알림 대상, 업무량/진행 보조 지표를 만들 때 사용한다. 자동 기록은 팀 합의 후에만 검토한다. |

### P1 — 팀 운영과 자동화에 유용한 카테고리

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `13-filters`, `12-filter-sharing`, `09-dashboards` | 저장 필터와 대시보드를 다룬다. | 팀이 합의한 JQL을 재사용하고, 서비스 대시보드와 Jira 원문 대시보드를 연결한다. 공유·수정 권한은 확인이 필요하다. |
| `54-labels`, `65-project-components`, `75-project-versions` | 라벨·컴포넌트·버전 정보를 다룬다. | 기능 영역과 배포 버전을 일관되게 분류·표시한다. |
| `28-issue-link-types` | 이슈 연결의 유형을 다룬다. | `29-issue-links`로 수집한 연결을 단순 목록이 아니라 선행·차단·관련 작업처럼 구분해 사이드뷰와 병목 표시의 보조 정보로 쓴다. |
| `17-issue-bulk-operations`, `44-issue-types`, `33-issue-priorities`, `27-issue-fields` | 이슈 일괄 작업과 타입·우선순위·필드를 다룬다. | 프로젝트 시작 템플릿 또는 반복 업무 정리에 유용하다. 일괄 변경은 영향 범위가 크므로 POC에서는 조회/소규모 테스트만 한다. |
| `91-webhooks` | Jira 이벤트 전송을 위한 webhook을 다룬다. | 이슈 변경을 실시간으로 수신하는 후보이다. Jira 관리자 또는 앱 권한 요구 가능성이 높아 조기 검증이 필요하다. |
| `68-project-key-and-name-validation`, `70-project-properties`, `67-project-features` | 프로젝트 이름/키 검증, 프로젝트 속성, 기능 상태를 다룬다. | 팀 초기 설정 유효성 검사와 연동 상태 기록에 쓸 수 있다. 설정 변경 권한은 분리한다. |

## 관리자·전역 설정 영역으로 제외한 카테고리

| 제외 카테고리 | 제외 이유 |
| --- | --- |
| `01-announcement-banner`, `04-app-properties`, `05-application-roles`, `53-jira-settings`, `81-server-info`, `55-license-metrics` | Jira 인스턴스 전역 설정, 애플리케이션 역할, 라이선스/서버 정보 영역이다. |
| `06-audit-records`, `02-app-data-policies`, `03-app-migration`, `10-dynamic-modules`, `56-migration-of-connect-modules-to-forge`, `82-service-registry`, `87-ui-modifications-apps` | 감사, 앱 플랫폼, 마이그레이션, UI 확장 등록을 다루며 일반 프로젝트 사용자 범위를 벗어난다. |
| `15-groups`, `59-permissions`, `58-permission-schemes`, `69-project-permission-schemes` | 사용자 그룹과 권한 체계를 변경한다. 교육기관의 보안 정책 영역이므로 제외한다. |
| `11-field-schemes`, `26-issue-field-configurations`, `22-issue-custom-field-contexts`, `23-issue-custom-field-options`, `40-issue-security-schemes`, `42-issue-type-schemes`, `43-issue-type-screen-schemes`, `61-priority-schemes`, `94-workflow-schemes` | 여러 프로젝트에 영향을 줄 수 있는 전역/공유 구성 스키마다. |
| `77-screen-schemes`, `78-screen-tab-fields`, `79-screen-tabs`, `80-screens`, `92-workflow-scheme-drafts`, `93-workflow-scheme-project-associations`, `96-workflow-statuses`, `97-workflow-transition-rules`, `98-workflows` | 화면·워크플로 구성 자체를 관리하며 Jira 관리자 또는 프로젝트 관리자 권한이 필요할 가능성이 높다. |
| `60-plans`, `85-teams-in-plan`, `62-project-avatars`, `63-project-categories`, `64-project-classification-levels`, `66-project-email`, `71-project-role-actors`, `72-project-roles`, `73-project-templates`, `74-project-types` | 고급 계획·프로젝트 관리 체계·공용 분류를 다루므로 초기 통합 서비스의 범위에서 제외한다. |

## 초기 제품에서 의도적으로 다루지 않을 개인 설정·민감 정보 영역

사용자별 탐색 설정과 이슈의 보안·삭제 정책은 대시보드 편의 기능보다 권한과 프라이버시를 우선한다. 서비스는 Jira가 반환한 접근 가능한 데이터만 표시하고, 아래 설정을 읽거나 변경하지 않는다.

| 제외 카테고리 | 제외 이유 |
| --- | --- |
| `30-issue-navigator-settings`, `88-user-properties` | 개인별 탐색 화면·속성으로, 통합 서비스가 사용자 환경을 대신 구성할 대상이 아니다. |
| `31-issue-notification-schemes` | Jira 원본 알림 정책을 바꾸면 사용자의 수신 체계가 예측 불가능하게 변한다. 자체 알림 규칙과 분리한다. |
| `34-issue-properties`, `35-issue-redaction`, `39-issue-security-level` | 앱 메타데이터, 콘텐츠 삭제, 이슈 보안 수준은 데이터 보존·접근 통제와 직접 연결된다. 제품은 별도 저장소의 최소 메타데이터와 원문 링크만 사용한다. |

## 첫 검증 순서

1. `57-myself` → `76-projects`로 토큰과 접근 가능한 팀 프로젝트를 확인한다.
2. `50-jql`/`38-issue-search` → `49-issues`로 읽기 전용 대시보드 데이터를 수집하고 Jira 원문 URL을 매핑한다. `83-status`, `95-workflow-status-categories`, `37-issue-resolutions`으로 팀 워크플로를 공통 진행 상태로 표시할 수 있는지도 함께 확인한다.
3. `19-issue-comments`, `36-issue-remote-links`, `28-issue-link-types`를 테스트 이슈에서 검증해 GitLab MR/배포 링크와 이슈 간 의존 관계의 표시 방식을 결정한다.
4. `91-webhooks`와 `13-filters`의 권한을 확인한 뒤 실시간 알림과 저장 검색을 확장한다.

## 다음 조사에서 확인할 항목

- SSAFY Jira 프로젝트에서 상태 카테고리·해결 상태를 조회할 수 있는지와, 팀별 커스텀 워크플로를 공통 진행 상태로 매핑할 기준
- 이슈 링크 유형과 원격 링크의 생성·조회 권한, GitLab MR·Jenkins 배포 URL을 중복 저장 없이 연결할 수 있는지
- `91-webhooks`의 프로젝트 단위 설정 가능 여부와 Jira Cloud 앱/관리자 권한 요구 범위
