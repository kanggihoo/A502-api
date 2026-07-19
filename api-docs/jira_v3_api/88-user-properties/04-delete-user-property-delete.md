# 04-Delete user property [DELETE]

`DELETE /rest/api/3/user/properties/{propertyKey}`

Deletes a property from a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to delete a property from any user.
 *  Access to Jira, to delete a property from the calling user's record.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `accountId` | `string` | `query` | No | The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. |
| `userKey` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `username` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `propertyKey` | `string` | `path` | Yes | The key of the user's property. |

### Responses

#### 204 - Returned if the user property is deleted.

#### 400 - Returned if `accountId` is missing.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission or is not accessing their user record.

#### 404 - Returned if the user or the property is not found.

