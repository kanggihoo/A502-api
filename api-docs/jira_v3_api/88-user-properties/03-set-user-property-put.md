# 03-Set user property [PUT]

`PUT /rest/api/3/user/properties/{propertyKey}`

Sets the value of a user's property. Use this resource to store custom data against a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a property on any user.
 *  Access to Jira, to set a property on the calling user's record.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `accountId` | `string` | `query` | No | The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. |
| `userKey` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `username` | `string` | `query` | No | This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `propertyKey` | `string` | `path` | Yes | The key of the user's property. The maximum length is 255 characters. |

### Request Body (application/json)

```json
any
```
### Responses

#### 200 - Returned if the user property is updated.

Schema (application/json):
```json
any
```

#### 201 - Returned if the user property is created.

Schema (application/json):
```json
any
```

#### 400 - Returned if `accountId` is missing.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission or is not accessing their user record.

#### 404 - Returned if the user is not found.

#### 405 - Returned if the property key is not specified.

