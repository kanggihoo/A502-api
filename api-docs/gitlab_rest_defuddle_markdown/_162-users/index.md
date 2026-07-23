# Users

  ### 1. Users API

  • 유용성: P0 (최우선 핵심 - 사용자 식별 및 인증/프로필).
      • Current user details (28번): 로그인한 사용자 토큰 정체성 확인 및 기본 정보 조회.
      • List/Retrieve users (03, 05번): 팀원 검색 및 프로필 정보 표시.
      • User memberships (26번): 현재 유저가 속한 모든 프로젝트 및 그룹 식별.
      • User status (39, 41번): 상태 메시지/이모지 설정 및 조회.
  • 제약 사항 (관리자 권한 필수):
      • Create/Update/Delete user (04, 06, 07번), Block/Ban/2FA 해제 (13, 18~25번): 인스턴스 최고
      관리자(Admin) 전용 권한.
  • 티어/권한: 일반 사용자 조회/상태 설정은 Free / CE 지원.

## Endpoints

- [01-Retrieve a Support PIN for a user [GET]](./01-retrieve-a-support-pin-for-a-user-get.md)
- [02-Revoke a Support PIN for a user [POST]](./02-revoke-a-support-pin-for-a-user-post.md)
- [03-List all users [GET]](./03-list-all-users-get.md)
- [04-Create a user [POST]](./04-create-a-user-post.md)
- [05-Retrieve a user as a regular user [GET]](./05-retrieve-a-user-as-a-regular-user-get.md)
- [06-Update a user [PUT]](./06-update-a-user-put.md)
- [07-Delete a user [DEL]](./07-delete-a-user-del.md)
- [08-Retrieve the status of a user [GET]](./08-retrieve-the-status-of-a-user-get.md)
- [09-Follow a user [POST]](./09-follow-a-user-post.md)
- [10-Unfollow a user [POST]](./10-unfollow-a-user-post.md)
- [11-List all accounts followed by a user [GET]](./11-list-all-accounts-followed-by-a-user-get.md)
- [12-List all accounts that follow a user [GET]](./12-list-all-accounts-that-follow-a-user-get.md)
- [13-Disable two-factor authentication for a user [PATCH]](./13-disable-two-factor-authentication-for-a-user-patch.md)
- [14-Delete authentication identity from a user [DEL]](./14-delete-authentication-identity-from-a-user-del.md)
- [15-Add an email address for a user [POST]](./15-add-an-email-address-for-a-user-post.md)
- [16-List all email addresses for a user [GET]](./16-list-all-email-addresses-for-a-user-get.md)
- [17-Delete an email address for a user [DEL]](./17-delete-an-email-address-for-a-user-del.md)
- [18-Reactivate a user [POST]](./18-reactivate-a-user-post.md)
- [19-Approve access to a user [POST]](./19-approve-access-to-a-user-post.md)
- [20-Reject access to a user [POST]](./20-reject-access-to-a-user-post.md)
- [21-Deactivate a user [POST]](./21-deactivate-a-user-post.md)
- [22-Block access to a user [POST]](./22-block-access-to-a-user-post.md)
- [23-Unblock access to a user [POST]](./23-unblock-access-to-a-user-post.md)
- [24-Ban a user [POST]](./24-ban-a-user-post.md)
- [25-Unban a user [POST]](./25-unban-a-user-post.md)
- [26-List all project and group memberships for a user [GET]](./26-list-all-project-and-group-memberships-for-a-user-get.md)
- [27-Retrieve association counts for a user [GET]](./27-retrieve-association-counts-for-a-user-get.md)
- [28-Retrieve current user details [GET]](./28-retrieve-current-user-details-get.md)
- [29-List all email addresses for a user [GET]](./29-list-all-email-addresses-for-a-user-get.md)
- [30-Add an email address [POST]](./30-add-an-email-address-post.md)
- [31-Update a user's credit_card_validation [PUT]](./31-update-a-user-s-credit-card-validation-put.md)
- [32-Create a Support PIN [POST]](./32-create-a-support-pin-post.md)
- [33-Retrieve Support PIN [GET]](./33-retrieve-support-pin-get.md)
- [34-Update your user preferences [PUT]](./34-update-your-user-preferences-put.md)
- [35-Retrieve your user preferences [GET]](./35-retrieve-your-user-preferences-get.md)
- [36-Retrieve details on an email address [GET]](./36-retrieve-details-on-an-email-address-get.md)
- [37-Delete an email address [DEL]](./37-delete-an-email-address-del.md)
- [38-List all activity for a user [GET]](./38-list-all-activity-for-a-user-get.md)
- [39-Set a user status [PUT]](./39-set-a-user-status-put.md)
- [40-Update a user status [PATCH]](./40-update-a-user-status-patch.md)
- [41-Retrieve your user status [GET]](./41-retrieve-your-user-status-get.md)
- [42-Create a runner owned by currently authenticated user [POST]](./42-create-a-runner-owned-by-currently-authenticated-user-post.md)
- [43-Return the user specific counts [GET]](./43-return-the-user-specific-counts-get.md)
