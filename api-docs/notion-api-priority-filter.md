# Notion API 우선 검토 카테고리

## 분류 기준

`notion_defuddle_markdown`과 `notion_data_apis_defuddle_markdown`의 파일·디렉터리명만으로 만든 1차 필터다. Notion은 사용자가 연결한 Integration에 페이지·데이터 소스를 명시적으로 공유해야 하므로, 관리자 권한 여부보다 **공유 범위와 토큰 방식**이 핵심 제약이다.

## 우선 시도할 API 카테고리

### P0 — 팀 문서와 작업 데이터 연결

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `01-working-with-page-content` | 페이지 콘텐츠를 다룬다. | 프로젝트 개요, 회의록, 온보딩 문서의 링크와 핵심 메타데이터를 대시보드에 연결한다. 원문은 Notion으로 이동시킨다. |
| `02-working-with-databases` | 데이터베이스와 대량 데이터 소스를 다룬다. | 팀이 Notion DB로 일정·회의록·요구사항을 관리한다면 필요한 항목만 조회해 통합 대시보드에 표시한다. |
| `04-working-with-comments` | 페이지/데이터에 대한 댓글을 다룬다. | 문서 검토 요청이나 결정사항 논의를 GitLab/Jira 흐름과 연결하는 후보이다. 자동 댓글은 알림 중복을 검토한 후 도입한다. |
| `05-working-with-markdown-content` | Markdown 콘텐츠를 다룬다. | README·기술 문서·회고를 가져오거나 내보낼 때 형식 변환 비용을 줄인다. |
| `06-working-with-files-and-media` | 파일·미디어 업로드와 기존 파일 조회를 다룬다. | 와이어프레임, 회의 자료, 배포 증빙 등 문서에 포함된 파일 링크를 표시한다. 파일을 별도 저장소처럼 중복 보관하지 않는다. |

### P1 — 연결 방식과 배포 형태 검토

| 카테고리 | 할 수 있는 일 | 프로젝트 활용 |
| --- | --- | --- |
| `03-personal-access-tokens`, `04-internal-connections`, `06-authorization`, `07-handling-api-keys` | 개인 토큰, 내부 연결, 인증, API 키 관리를 다룬다. | 초기 POC는 팀이 공유한 내부 Integration으로 시작하고, 토큰을 사용자별로 안전하게 보관하는 방식을 결정한다. |
| `05-public-connections`, `08-preparing-for-users`, `09-list-on-the-marketplace` | 공개 연결과 다중 사용자 제품 배포 방식을 다룬다. | SSAFY 외부 팀까지 서비스 범위를 넓힐 때 검토한다. 현재 POC에는 필요하지 않다. |
| `03-working-with-views` | 데이터 보기(View)를 다룬다. | Notion DB의 팀별/상태별 보기와 서비스 대시보드 사이의 링크·표현을 맞출 때 검토한다. |

## 초기 범위에서 제외할 항목

Notion 문서 구조에는 Mattermost/Jira처럼 명확한 인스턴스 관리자 API 카테고리가 많지 않다. 따라서 제외 기준은 “관리자 전용”보다 “초기 POC에 불필요하거나 보안 범위가 넓은 연결 방식”이다.

| 제외 카테고리 | 제외 이유 |
| --- | --- |
| `05-public-connections`, `09-list-on-the-marketplace` | OAuth 공개 앱·마켓플레이스 배포는 다중 워크스페이스 동의, 심사, 보안 정책을 요구하므로 팀 내부 POC 범위를 벗어난다. |
| `08-preparing-for-users` | 일반 사용자 대상 제품화 단계의 운영 요구사항으로, 내부 팀 Integration을 검증한 뒤에 필요하다. |
| `03-personal-access-tokens`의 사용자 토큰 대리 관리 | 사용자 개인 토큰을 서비스가 수집·보관하는 방식은 유출 위험이 크다. 팀이 공유한 내부 Integration 토큰 또는 사용자 직접 연결을 우선한다. |

## 첫 검증 순서

1. 내부 Integration을 만들고, 테스트용 Notion 페이지와 데이터베이스를 해당 Integration에 공유한다.
2. 페이지 콘텐츠와 데이터베이스의 읽기 호출을 검증해 대시보드에 필요한 최소 메타데이터와 원문 URL을 정한다.
3. 댓글과 Markdown 변환을 테스트해 문서 검토·동기화 기능의 필요성을 판단한다.
4. 파일/미디어 처리와 사용자별 OAuth 연결은 실제 수요가 확인될 때 확장한다.

