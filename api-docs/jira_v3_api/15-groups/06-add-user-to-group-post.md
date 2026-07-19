# 06-Add user to group [POST]

`POST /rest/api/3/group/user`

Adds a user to a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `groupname` | `string` | `query` | No | As a group's name can change, use of `groupId` is recommended to identify a group.  <br>The name of the group. This parameter cannot be used with the `groupId` parameter. |
| `groupId` | `string` | `query` | No | The ID of the group. This parameter cannot be used with the `groupName` parameter. |

### Request Body (application/json)

```json
{
  "accountId": string, // The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
  "name": string, // This property is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
}
```
### Responses

#### 201 - Returned if the request is successful.

Schema (application/json):
```json
{
  "expand": string, // Expand options that include additional group details in the response.
  "groupId": string, // The ID of the group, which uniquely identifies the group across all Atlassian products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.
  "name": string, // The name of group.
  "self": string, // The URL for these group details.
  "users": any, // A paginated list of the users that are members of the group. A maximum of 50 users is returned in the list, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 50 users, use`?expand=users[51:100]`.
}
```

#### 400 - Returned if:

 *  `groupname` is not provided.
 *  `accountId` is missing.

#### 401 - Returned if the authentication credentials are incorrect or missing from the request.

#### 403 - Returned if the calling user does not have the necessary permission.

#### 404 - Returned if the group or user are not found.

#### 429 - Returned if rate limiting is being enforced.

