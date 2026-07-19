# GitLab REST API 우선 검토 카테고리

## 분류 기준

이 문서는 `gitlab_rest_defuddle_markdown`의 **디렉터리·파일명 구조만** 보고 작성한 1차 필터다. 개별 Markdown의 엔드포인트, 파라미터, 최소 권한은 아직 읽거나 검증하지 않았다.

단, 아래 OAuth2 행과 OAuth2 관련 후속 조사 항목은 `lab.ssafy.com`에서 별도로 확인한 사용자 수준 앱 등록 결과를 기록한 예외다. 해당 사실은 이 디렉터리 구조만으로 추론한 내용이 아니다.

- 대상 역할: 팀장 `Maintainer`, 팀원 `Developer`
- 목표: 팀 프로젝트 시작 지원, 통합 대시보드, 행동 가능한 알림, 반복 작업 자동화
- 원칙: 교육기관 GitLab 인스턴스 전체를 관리해야 하는 기능은 제외한다.
- 주의: 아래의 “시도 가능”은 권한 보장이 아니다. 실제 토큰으로 `GET`부터 호출해 확인한 뒤, 쓰기 작업은 별도 테스트 프로젝트에서 검증한다.

## 우선 시도할 API 카테고리

### P0 — 통합 대시보드와 알림의 핵심

| 카테고리(문서 디렉터리) | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `129-projects` | 접근 가능한 프로젝트의 기본 정보와 상태를 조회하고, 프로젝트 단위 설정을 다룬다. | 팀 프로젝트 식별·선택, 프로젝트 홈 링크, 대시보드의 기준 엔터티로 사용한다. |
| `67-groups` | 그룹과 그룹에 속한 프로젝트 정보를 다룬다. | SSAFY 반/팀 그룹 구조가 존재한다면 팀 리소스 자동 발견에 사용한다. |
| `91-members` | 프로젝트·그룹 멤버와 역할을 조회하고 멤버십을 다룬다. | 팀장과 팀원을 판별하고, 1명 Maintainer·5명 Developer 구성이 맞는지 확인한다. 쓰기 기능은 팀장 토큰으로만 별도 검증한다. |
| `162-users` | 현재 사용자와 사용자 정보를 조회한다. | 최초 연결 시 로그인 사용자를 확인하고, 팀장 여부를 판별하는 보조 정보로 사용한다. |
| `52-events`, `158-to-dos`, `139-resource-events` | 사용자 활동, 할 일, 리소스 이벤트를 조회한다. | 여러 GitLab 변화를 한 화면에 요약하고, 놓친 활동을 개인별로 보여 준다. |
| `74-issues` | 이슈, 참여자, 관련 MR, 시간 기록, 이슈 연결을 다룬다. | Jira 연동 전후의 개발 작업 맥락을 모으고, 이슈↔MR 연결과 진행 현황을 보여 준다. |
| `93-merge-requests` | MR 목록·상세·리뷰어·참여자·파이프라인·변경 사항을 다룬다. | 리뷰 대기, 병합 가능 여부, 담당자, 파이프라인 상태를 통합 대시보드와 Mattermost 알림의 핵심 정보로 사용한다. |
| `119-pipelines`, `24-ci-jobs`, `80-jobs`, `35-commit-statuses` | 파이프라인·잡·커밋 상태를 조회하고 일부 실행 흐름을 제어한다. | 빌드 실패/성공, 실패 잡, 재시도 필요 상태를 감지해 정확한 GitLab URL과 함께 알린다. |

### P1 — 프로젝트 시작과 팀 개발 흐름에 유용한 카테고리

| 카테고리(문서 디렉터리) | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `68-hooks` | 프로젝트 또는 그룹 이벤트를 외부 HTTP 엔드포인트로 전달하도록 연결한다. | 폴링 대신 push, MR, 이슈, 파이프라인 이벤트를 수신하는 핵심 수단이다. 우선 프로젝트 webhook부터 검증한다. |
| `73-invitations` | 그룹·프로젝트 초대의 대기·수락 전 단계를 다룬다. | 팀 생성 흐름에서 초대 발송 후의 상태를 확인하고, 미수락 팀원을 팀장에게 안내하는 후보로 검토한다. 기존 계정·멤버십이 제공되는 SSAFY 운영 방식이면 사용하지 않는다. |
| `71-integrations` | GitLab 프로젝트와 Jenkins, Jira, Mattermost 등 외부 서비스의 통합 설정을 다룬다. | 각 도구를 직접 수집할지, GitLab 내장 통합을 활용할지 비교할 때 우선 확인한다. 설정 권한·인스턴스 정책 때문에 실패할 가능성을 전제로 둔다. |
| `127-project-templates`, `156-templates` | 프로젝트·일반 템플릿 후보를 제공한다. | 팀 시작 시 빈 저장소 대신 공통 README, CI, 브랜치 전략 문서를 포함한 시작점을 제공할 수 있는지 검토한다. 템플릿을 강제하거나 기존 저장소를 덮어쓰지 않는다. |
| `29-ci-triggers`, `118-pipeline-schedules`, `30-ci-variables`, `25-ci-lint` | 외부에서 파이프라인을 시작하거나, 정기 실행·변수·CI 설정 검증을 다룬다. | 배포 전 점검, 정기 상태 수집, 팀 운영 자동화를 지원한다. 변수 조회·수정은 비밀값 노출 위험이 있어 최소 권한과 마스킹을 먼저 확인한다. |
| `21-branches`, `131-protected-branches`, `132-protected-environments`, `133-protected-tags`, `135-push-rules`, `155-tags` | 브랜치·환경·태그의 보호 규칙과 push 규칙을 다룬다. | 기본 브랜치·배포 환경·배포 태그의 보호 상태를 점검하고, 누락 가능성을 팀장에게 알리는 보안 진단의 기반으로 쓴다. 자동 변경은 하지 않고, 확인된 규칙만 원문 링크와 함께 제안한다. |
| `36-commits`, `57-files`, `138-repositories`, `166-web-commits` | 커밋·파일·저장소 내용을 조회하고 일부 파일 기반 작업을 수행한다. | 최근 코드 활동, README/배포 문서 바로가기, 변경 이력 확인 기능의 기반이 된다. 파일 쓰기·웹 커밋은 POC에서 자동 실행하지 않는다. |
| `46-discussions`, `101-notes`, `154-suggestions` | MR·이슈 토론, 댓글, 코드 제안을 다룬다. | 미해결 토론이나 리뷰 피드백을 대시보드에서 집계하고 원문으로 연결한다. 자동 댓글 작성은 스팸 위험 때문에 후순위다. |
| `84-labels`, `99-milestones`, `75-iterations`, `20-boards` | 라벨·마일스톤·이터레이션·보드를 관리한다. | 스프린트, 역할별 업무, 마감 임박 작업을 통일된 방식으로 보여 준다. Jira를 주 업무 도구로 쓸 경우에는 읽기/링크 중심으로 시작한다. |
| `136-releases`, `49-environments`, `45-deploy-resources`, `79-job-artifacts` | 릴리스·배포 환경·배포 리소스·CI 산출물을 다룬다. | EC2 배포 상태, 최근 릴리스, 테스트/빌드 산출물 링크를 모아 배포 가시성을 높인다. |
| `145-search`, `34-code-search`, `89-markdown` | 프로젝트·코드 검색과 Markdown 렌더링을 지원한다. | 대시보드에서 GitLab 원문으로 빠르게 이동하는 검색·미리보기 보조 기능에 쓸 수 있다. |
| `11-applications`, `103-oauth-applications`, `159-token-exchange` | 사용자 수준 OAuth2 애플리케이션을 등록하고 토큰 교환 흐름을 다룬다. | `https://lab.ssafy.com/-/user_settings/applications`에서 사용자 계정으로 앱 등록이 확인됨. `read_api`/`api`/`read_user`/`openid` scope로 세분화 권한 부여 가능. refresh_token 자동 갱신으로 PAT 만료(최대 365일 강제)보다 장기 운영 유리. **POC는 처음부터 OAuth2(Authorization Code + PKCE)로 시작.** 백엔드 서버(EC2)에서 client_secret 안전 보관 가능하므로 Confidential 앱 사용. |

### P2 — 유용하지만 팀의 실제 사용 방식이 확인된 뒤 검토할 카테고리

| 카테고리(문서 디렉터리) | 할 수 있는 일 | 보류 이유 |
| --- | --- | --- |
| `12-approval-rules`, `92-merge-request-approvals`, `123-project-approvals` | MR 승인 규칙과 승인 상태를 다룬다. | 코드 리뷰 규칙을 실제로 운영한다면 매우 유용하다. GitLab 에디션·인스턴스 정책 지원 여부를 먼저 확인한다. |
| `54-external-status-checks` | 외부 도구의 MR 상태 확인 후보다. | AI 사전 코드 리뷰의 결과를 MR 흐름에 표시해야 할 때 검토한다. 사람의 최종 승인 원칙을 바꾸거나, 검증 전 병합을 차단하는 용도로 사용하지 않는다. |
| `94-merge-trains` | 병합 대기열을 관리한다. | 팀 규모가 작고 병합 충돌이 적다면 초기 POC의 우선순위가 낮다. |
| `107-packages`, `38-container-registry` | 패키지·컨테이너 이미지를 관리한다. | GitLab Registry를 실제 배포 흐름에 쓸 때만 배포 대시보드에 포함한다. |
| `137-remote-mirrors`, `125-project-mirrors`, `153-submodules` | 외부 저장소 미러링과 서브모듈을 다룬다. | 외부 공개 저장소 동기화가 필요한 팀에만 유용하다. |
| `50-epics`, `76-jira-connect-subscriptions`, `77-jira-forge-installation`, `78-jira-forge-subscriptions` | 상위 기획 단위와 Jira 관련 연결을 다룬다. | Jira가 주 업무 관리 도구이므로 연동 가치는 높지만, SaaS Jira 권한·설치 방식·인스턴스 설정을 먼저 확인해야 한다. |
| `40-dora-metrics`, `10-analytics`, `33-code-review-analytics` | 배포·리뷰·개발 활동 지표를 제공한다. | 데이터가 충분히 쌓인 뒤 회고/팀 건강도 기능으로 검토한다. 일부 기능은 플랜 또는 인스턴스 설정에 좌우될 수 있다. |
| `03-access-requests`, `58-freeze-periods`, `167-wikis` | 접근 요청, 배포 동결 기간, GitLab Wiki를 다룬다. | 각각 팀 접근 예외 처리, 배포 일정 표시, 문서 사이드뷰의 보조 후보이다. 다만 SSAFY의 실제 접근 부여 방식·배포 관행·Notion 사용 여부가 확인된 팀에서만 검토한다. |

## 관리자 권한 또는 인스턴스 운영 영역으로 제외한 카테고리

아래는 교육생의 팀장/팀원 토큰으로 운영하기 어렵거나, 교육기관 전체에 영향을 줄 수 있어 초기 제품 범위에서 제외한다. 같은 디렉터리에 팀 수준 기능과 관리자 기능이 섞인 경우에는 관리자 작업만 제외하고 읽기 가능 기능을 별도로 확인한다.

| 제외 카테고리(문서 디렉터리) | 제외 이유 |
| --- | --- |
| `70-instance`, `95-metadata`, `56-features`, `120-plan-limits`, `64-gitlab-subscriptions`, `161-usage-data` | GitLab 인스턴스의 설정·기능 플래그·요금제·전역 사용량을 다루는 운영자 영역이다. |
| `04-access-tokens`, `148-service-accounts` | impersonation, 서비스 계정, 프로젝트/그룹 접근 토큰의 발급·회전·폐기는 보안 민감도가 높다. 사용자의 개인 토큰은 사용자가 직접 발급하고, 서비스용 비밀값은 제품이 대신 관리하지 않는다. |
| `14-audit-events`, `22-broadcast-messages`, `48-enterprise-users`, `106-organizations`, `90-member-roles` | 감사, 전역 공지, 엔터프라이즈 사용자·조직·인스턴스 역할은 교육기관 관리 범위다. |
| `83-ldap`, `144-saml-group-links`, `134-provider-identities` | 중앙 인증 체계와 외부 IdP 연결을 변경하는 관리자 영역이다. |
| `18-batched-background-migrations`, `19-batched-background-operations`, `41-data-management`, `42-database-dictionary`, `98-migrations`, `149-sidekiq`, `72-internal-operations`, `60-geo` | 데이터베이스·백그라운드 작업·복제·내부 운영 API로, 제품 연동 대상이 아니다. |
| `28-ci-runners`, `142-runner-controllers`, `143-runners`, `141-runner-controller-tokens`, `26-ci-minutes` | 공용 Runner 및 실행 인프라를 관리하거나 사용량 정책에 영향을 준다. 팀 프로젝트 전용 Runner가 허용될 때만 별도 검토한다. |
| `32-clusters`, `31-cluster-agents`, `08-agents`, `169-workspaces` | Kubernetes/에이전트/원격 개발 환경의 인프라 운영 범주다. SSAFY EC2 기반 흐름의 초기 POC에서는 제외한다. |
| `37-compliance-policy-settings`, `85-licenses`, `151-software-composition-analysis`, `147-security-scans`, `165-vulnerabilities` | 전사 보안·컴플라이언스 정책 또는 유료 보안 기능과 관련돼 있고, 권한과 플랜 제약 가능성이 높다. |
| `06-add-on-purchases`, `61-gitlab-duo`, `62-gitlab-duo-workflows`, `88-mlops`, `82-knowledge-graph`, `05-active-context` | 구매·AI/ML·내부 지식 기능으로, 팀 협업 통합의 초기 목적과 맞지 않거나 인스턴스 기능 활성화가 필요하다. |

## 초기 제품에서 의도적으로 다루지 않을 민감 사용자 영역

아래는 관리자 API가 아니더라도 개인 설정이나 비밀값에 직접 닿는다. 제품이 조회·변경·보관하지 않으며, 필요하면 사용자가 원본 GitLab에서 직접 관리한다.

| 제외 카테고리(문서 디렉터리) | 제외 이유 |
| --- | --- |
| `102-notification-settings` | GitLab 자체 알림 수준은 개인 작업 방식에 해당한다. 통합 워크스페이스의 알림 정책과 독립적으로 두며, 사용자 설정을 일괄 변경하지 않는다. |
| `81-keys`, `146-secure-files`, `65-group-credentials-inventory` | SSH/GPG 키, CI 보안 파일, 자격 증명 목록은 노출·보관 자체가 보안 위험이다. AI 진단도 원문 비밀값을 수집하지 않는 방식으로 설계한다. |
| `47-draft-notes` | 개인 초안은 협업 대시보드·사이드뷰의 수집 대상이 아니다. |

## 첫 API 검증 순서

1. **현재 사용자·프로젝트·멤버 조회**: `162-users` → `129-projects` → `91-members` 순서로 토큰의 정체와 팀 역할을 확인한다.
2. **읽기 전용 대시보드 데이터**: `93-merge-requests`, `74-issues`, `119-pipelines`, `52-events`, `158-to-dos`를 조회하고 각 결과의 원문 URL을 매핑한다.
3. **팀 시작 자동화 후보**: 테스트 프로젝트에서 `127-project-templates`, `156-templates`, `73-invitations`을 확인한다. 템플릿 적용 가능 여부와 초대 상태 조회 권한을 분리해 기록한다.
4. **이벤트 수신**: `68-hooks`의 프로젝트 webhook 생성·삭제·전송 여부를 테스트 프로젝트에서 검증한다.
5. **자동화 후보**: `71-integrations`, `29-ci-triggers`, `118-pipeline-schedules`를 팀장 토큰으로 검증한다.
6. **보안·리뷰 보조**: `132-protected-environments`, `135-push-rules`, `54-external-status-checks`는 먼저 조회 가능 여부와 에디션·권한 제약을 확인한다. 자동 변경·병합 차단은 하지 않는다.
7. **쓰기 작업 확장**: 멤버, 라벨, 마일스톤, 브랜치 보호 규칙처럼 팀 운영에 영향을 주는 변경은 성공·실패·권한 부족 응답을 기록한 후에만 제품 흐름에 넣는다.

## 다음 조사에서 확인할 항목

- `lab.ssafy.com`의 GitLab 버전과 에디션
- Personal Access Token의 허용 scope와 만료 정책
- 팀장 Maintainer / 팀원 Developer별 실제 API 응답 차이
- 프로젝트 webhook 생성 권한, 수신 네트워크 제약, Secret Token 지원 여부
- GitLab의 Jenkins·Jira·Mattermost 통합 설정을 Maintainer가 변경할 수 있는지
- 그룹이 SSAFY 관리자 소유인지, 팀장이 그룹 Owner인지
- 프로젝트 템플릿을 팀 프로젝트 생성에 적용할 수 있는지와, 기존 저장소에 영향을 주지 않는 시작 흐름
- 프로젝트·그룹 초대의 생성·조회 권한과, SSAFY가 사전에 멤버십을 부여하는지
- protected environments·push rules·external status checks의 GitLab 에디션 및 Maintainer 권한 지원 여부

### OAuth2 관련 (POC 기본 인증 방식, 사용자 수준 앱 등록 확인됨)

- 사용자 수준 OAuth 앱(`/user_settings/applications`) 등록 가능 확인 완료. 인스턴스 관리자 권한 아님.
- OAuth2 access_token·refresh_token 만료 정책 (`lab.ssafy.com` 설정값)
- Authorization Code + PKCE flow 백엔드(EC2) 구현 시 redirect URI 네트워크 제약
- Confidential 앱 client_secret 서버 저장 방식, 평문 저장 금지
- scope 최소화 전략: `read_api`(읽기 대시보드) → `api`(쓰기, 팀장만) 분리
- 토큰 만료/갱신 실패 시 제품 UX(재인증 안내) 설계
- PAT는 긴급 디버그·1회성 스크립트 용도로만 보관 (제품 인증 흐름엔 미사용)
