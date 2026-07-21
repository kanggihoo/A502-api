제공 문서 기준 프로젝트 웹훅 API 목록.

1. **조회 및 모니터링**
   - 웹훅 목록 조회: `GET /projects/:id/hooks`
   - 웹훅 단건 상세: `GET /projects/:id/hooks/:hook_id`
   - 최근 7일 이벤트 목록: `GET /projects/:id/hooks/:hook_id/events`

2. **생성·수정·삭제**
   - 웹훅 추가: `POST /projects/:id/hooks`
   - 웹훅 수정: `PUT /projects/:id/hooks/:hook_id`
   - 웹훅 삭제: `DELETE /projects/:id/hooks/:hook_id`

3. **이벤트 제어 및 테스트**
   - 특정 이벤트 재전송: `POST /projects/:id/hooks/:hook_id/events/:hook_event_id/resend`
   - 테스트 웹훅 트리거 (즉시 전송): `POST /projects/:id/hooks/:hook_id/test/:trigger`

4. **부가 기능**
   - 커스텀 헤더 설정: `PUT /projects/:id/hooks/:hook_id/custom_headers/:key`
   - 커스텀 헤더 삭제: `DELETE /projects/:id/hooks/:hook_id/custom_headers/:key`
   - URL 변수 설정: `PUT /projects/:id/hooks/:hook_id/url_variables/:key`
   - URL 변수 삭제: `DELETE /projects/:id/hooks/:hook_id/url_variables/:key`


