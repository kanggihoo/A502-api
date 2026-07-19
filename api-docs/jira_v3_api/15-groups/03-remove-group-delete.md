# 03-Remove group [DELETE]

`DELETE /rest/api/3/group`

Deletes a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* strategic [group](https://confluence.atlassian.com/x/24xjL)).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `groupname` | `string` | `query` | No |  |
| `groupId` | `string` | `query` | No | The ID of the group. This parameter cannot be used with the `groupname` parameter. |
| `swapGroup` | `string` | `query` | No | As a group's name can change, use of `swapGroupId` is recommended to identify a group.  <br>The group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroupId` parameter. |
| `swapGroupId` | `string` | `query` | No | The ID of the group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroup` parameter. |

### Responses

#### 200 - Returned if the request is successful.

#### 400 - Returned if the group name is not specified.

#### 401 - Returned if the authentication credentials are incorrect or missing from the request.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the group is not found.

