# Hooks

Operations related to hooks.
  ### 2. Hooks API (Webhooks)

  • 유용성: P0 (핵심 / 가장 중요 - 실시간 이벤트 수신 및 Mattermost 알림 수단).
      • Project webhooks (27~31번, 33번): Push, MR, 이슈, 댓글 등 파이프라인 이벤트를 통합 서버/Mattermost로 즉시 수신하는 핵심 수단.
      (폴링 방식 대체).
      • Test webhook (33번): Webhook 연동 정상 작동 테스트용.
  • 제약 사항 (일부 기능 제한):
      • System hooks (17~26번): 인스턴스 최고 관리자(Admin) 전용 (전역 시스템 훅 - 사용 불가).
      • Project webhooks (27~31번): 프로젝트 Maintainer 이상 권한 필요 (팀장 토큰으로 생성).
  • 결론: 프로젝트 Webhook(27~31, 33번)은 P0 필수 활용. (System hooks는 관리자 권한 부족으로 제외).
## Endpoints

- [01-List all group hooks [GET]](./01-list-all-group-hooks-get.md)
- [02-Create a group hook [POST]](./02-create-a-group-hook-post.md)
- [03-Retrieve a group hook [GET]](./03-retrieve-a-group-hook-get.md)
- [04-Update a group hook [PUT]](./04-update-a-group-hook-put.md)
- [05-Delete a group hook [DEL]](./05-delete-a-group-hook-del.md)
- [06-List all events [GET]](./06-list-all-events-get.md)
- [07-Update a URL variable [PUT]](./07-update-a-url-variable-put.md)
- [08-Delete a URL variable [DEL]](./08-delete-a-url-variable-del.md)
- [09-Update a custom header [PUT]](./09-update-a-custom-header-put.md)
- [10-Delete a custom header [DEL]](./10-delete-a-custom-header-del.md)
- [11-Trigger a test webhook [POST]](./11-trigger-a-test-webhook-post.md)
- [12-Resend a webhook event [POST]](./12-resend-a-webhook-event-post.md)
- [13-Update a URL variable [PUT]](./13-update-a-url-variable-put.md)
- [14-Delete a URL variable [DEL]](./14-delete-a-url-variable-del.md)
- [15-Update a custom header [PUT]](./15-update-a-custom-header-put.md)
- [16-Delete a custom header [DEL]](./16-delete-a-custom-header-del.md)
- [17-List all system hooks [GET]](./17-list-all-system-hooks-get.md)
- [18-Create a system hook [POST]](./18-create-a-system-hook-post.md)
- [19-Retrieve a system hook [GET]](./19-retrieve-a-system-hook-get.md)
- [20-Update a system hook [PUT]](./20-update-a-system-hook-put.md)
- [21-Create a test run [POST]](./21-create-a-test-run-post.md)
- [22-Delete a system hook [DEL]](./22-delete-a-system-hook-del.md)
- [23-Update a URL variable [PUT]](./23-update-a-url-variable-put.md)
- [24-Delete a URL variable [DEL]](./24-delete-a-url-variable-del.md)
- [25-Update a custom header [PUT]](./25-update-a-custom-header-put.md)
- [26-Delete a custom header [DEL]](./26-delete-a-custom-header-del.md)
- [27-List all webhooks for a project [GET]](./27-list-all-webhooks-for-a-project-get.md)
- [28-Add a webhook to a project [POST]](./28-add-a-webhook-to-a-project-post.md)
- [29-Retrieve a project webhook [GET]](./29-retrieve-a-project-webhook-get.md)
- [30-Update a project webhook [PUT]](./30-update-a-project-webhook-put.md)
- [31-Delete a project webhook [DEL]](./31-delete-a-project-webhook-del.md)
- [32-List all events [GET]](./32-list-all-events-get.md)
- [33-Trigger a test webhook [POST]](./33-trigger-a-test-webhook-post.md)
- [34-Resend a webhook event [POST]](./34-resend-a-webhook-event-post.md)
