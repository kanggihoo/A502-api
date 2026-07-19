# 01-Get user property keys [GET]

`GET /rest/api/3/user/properties`

Returns the keys of all properties for a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user.
 *  Access to Jira, to access the calling user's property keys.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `accountId` | `string` | `query` | No | The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. |
| `userKey` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `username` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"keys\":[{\"key\":\"issue.support\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support\"}]}"
```

#### 400 - Returned if `accountId` is missing.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission or is not accessing their user record.

#### 404 - Returned if the user is not found.

