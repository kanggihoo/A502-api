# 11-Get user groups [GET]

`GET /rest/api/3/user/groups`

Returns the groups to which a user belongs.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `accountId` | `string` | `query` | Yes | The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. |
| `username` | `string` | `query` | No | This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `key` | `string` | `query` | No | This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-administrators\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the calling user does not have the *Browse users and groups* global permission.

#### 404 - Returned if the user is not found.

