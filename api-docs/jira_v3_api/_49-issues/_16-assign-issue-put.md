# 16-Assign issue [PUT]

`PUT /rest/api/3/issue/{issueIdOrKey}/assignee`

Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues* permission but has the *Assign issue* permission for the project that the issue is in.

If `name` or `accountId` is set to:

 *  `"-1"`, the issue is assigned to the default assignee for the project.
 *  `null`, the issue is set to unassigned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse Projects* and *Assign Issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue to be assigned. |

### Request Body (application/json)

```json
{
  "accountId": string, // The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required in requests.
  "accountType": enum("atlassian" | "app" | "customer" | "unknown"), // The user account type. Can take the following values:   *  `atlassian` regular Atlassian user account  *  `app` system account used for Connect applications and OAuth to represent external systems  *  `customer` Jira Service Desk account representing an external service desk
  "active": boolean, // Whether the user is active.
  "appType": string, // The app type of the user account when accountType is 'app'. Can take the following values:   *  `service` Service Account  *  `agent` Rovo Agent Account  *  `unknown` Unknown app type
  "applicationRoles": any, // The application roles the user is assigned to.
  "avatarUrls": any, // The avatars of the user.
  "displayName": string, // The display name of the user. Depending on the user’s privacy setting, this may return an alternative value.
  "emailAddress": string, // The email address of the user. Depending on the user’s privacy setting, this may be returned as null.
  "expand": string, // Expand options that include additional user details in the response.
  "groups": any, // The groups that the user belongs to.
  "guest": boolean, // Whether the user is a guest.
  "key": string, // This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
  "locale": string, // The locale of the user. Depending on the user’s privacy setting, this may be returned as null.
  "name": string, // This property is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
  "self": string, // The URL of the user.
  "timeZone": string, // The time zone specified in the user's profile. If the user's time zone is not visible to the current user (due to user's profile setting), or if a time zone has not been set, the instance's default time zone will be returned.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if:

 *  the user is not found.
 *  `name`, `key`, or `accountId` is missing.
 *  more than one of `name`, `key`, and `accountId` are provided.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the issue is not found.

