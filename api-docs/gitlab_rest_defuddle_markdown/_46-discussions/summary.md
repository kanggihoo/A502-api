# Discussions API 명세서 (관리자 권한 미필요 API)

본 문서는 `_46-discussions` 디렉토리 내의 GitLab Discussions (이슈, 머지 리퀘스트, 커밋, 스니펫, 에픽 대상 스레드형 토론 및 답글 관리) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 43개)

---


## 18 ~ 26. Merge Request Discussions (GET, POST, GET, PUT Resolve, GET Notes, POST Note, GET Note, PUT Note, DEL Note)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions`: MR 토론 스레드 목록 조회
  - `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions`: MR 토론 또는 특정 코드 라인 인라인 Diff 리뷰 스레드 생성 (`position` 객체 포함)
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}`: 단일 MR 스레드 조회
  - `PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}`: MR 코드 리뷰 스레드 해결 완료/미해결 처리 (`resolved: true/false`)
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}/notes`: MR 스레드 답글 목록 조회
  - `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}/notes`: MR 리뷰 답글 등록
  - `GET/PUT/DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}/notes/{note_id}`: MR 답글 상세 조회, 수정, 삭제
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)
- **설명:** SSAFY 팀의 핵심 코드 리뷰 기능으로, MR 상의 코드 리뷰 스레드 생성, 인라인 피드백 작성 및 스레드 해결(`resolved`) 관리에 활용됩니다.


