# 01-Get group [GET]

`GET /rest/api/3/group`

This operation is deprecated, use [`group/member`](#api-rest-api-3-group-member-get).

Returns all users in a group.

**[Permissions](#permissions) required:** either of:

 *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `groupname` | `string` | `query` | No | As a group's name can change, use of `groupId` is recommended to identify a group.  <br>The name of the group. This parameter cannot be used with the `groupId` parameter. |
| `groupId` | `string` | `query` | No | The ID of the group. This parameter cannot be used with the `groupName` parameter. |
| `expand` | `string` | `query` | No | List of fields to expand. |

### Responses

#### 200 - Returned if the request is successful.

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

#### 400 - Returned if the group name is not specified.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the calling user does not have the Administer Jira global permission.

#### 404 - Returned if the group is not found.

