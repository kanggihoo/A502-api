# _42-issue-type-schemes API 요약

이 리소스 그룹은 클래식(classic) 프로젝트에서 사용하는 이슈 타입 스킴(issue type scheme)을 조회/생성/수정/삭제하고, 프로젝트에 할당하거나 스킴 내 이슈 타입의 구성·순서를 관리하는 API 모음이다.

## 제외된 API

- `01-get-all-issue-type-schemes-get.md`: "Administer Jira" 글로벌 권한(Jira 사이트 전체 관리자) 필요. 응답 예시에도 "Only Jira administrators can access issue type schemes." 에러 메시지가 명시되어 있어 프로젝트 관리자 권한으로는 호출 불가.
- `02-create-issue-type-scheme-post.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `03-get-issue-type-scheme-items-get.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `04-get-issue-type-schemes-for-projects-get.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `05-assign-issue-type-scheme-to-project-put.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `06-update-issue-type-scheme-put.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `07-delete-issue-type-scheme-delete.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `08-add-issue-types-to-issue-type-scheme-put.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `09-change-order-of-issue-types-put.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.
- `10-remove-issue-type-from-issue-type-scheme-delete.md`: 동일하게 "Administer Jira" 글로벌 권한 필요.

이 리소스 그룹의 10개 엔드포인트 모두 "Administer Jira" 글로벌 권한(사이트 전체 시스템 관리자)을 요구하며, 403 에러 응답 예시에 "Only Jira administrators can access issue type schemes."라는 메시지가 공통으로 명시되어 있다. SSAFY 교육생 계정은 프로젝트 관리자 수준 권한을 갖는 것이 일반적이므로, 이 그룹의 API는 실제 POC 환경에서 호출 가능성이 낮아 전부 제외했다. 따라서 채택된 API가 없어 별도의 API 섹션은 작성하지 않는다.
