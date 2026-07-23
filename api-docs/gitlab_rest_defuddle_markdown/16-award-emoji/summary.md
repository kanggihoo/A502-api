# Award Emoji API 명세서 (관리자 권한 미필요 API)

본 문서는 `_16-award-emoji` 디렉토리 내의 GitLab Award Emoji (이슈, 머지 리퀘스트, 스니펫, 에픽 및 댓글 대상 이모지 리액션) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 32개)

---


## 09 ~ 12. Merge Request Award Emoji (GET, POST, GET, DEL)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/award_emoji`
  - `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/award_emoji`
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/award_emoji/{award_id}`
  - `DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/award_emoji/{award_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 13 ~ 16. Merge Request Comment Award Emoji (GET, POST, GET, DEL)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji`
  - `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji`
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji/{award_id}`
  - `DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji/{award_id}`

---

