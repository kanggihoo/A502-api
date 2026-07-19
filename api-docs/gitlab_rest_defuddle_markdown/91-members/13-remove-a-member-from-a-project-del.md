# 13-Remove a member from a project [DEL]

`DELETE /api/v4/projects/{id}/members/{user_id}`

Removes a specified user from a project. The user must be a direct member.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `user_id` | `integer` | `path` | Yes | The user ID of the member |
| `skip_subresources` | `boolean` | `query` | No | If `true`, the member retains any direct memberships in subgroups or projects. |
| `unassign_issuables` | `boolean` | `query` | No | If `true`, unassigns the member from any issues or merge requests in the project. |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

