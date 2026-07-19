# 23-Remove a billable member from a group [DEL]

`DELETE /api/v4/groups/{id}/billable_members/{user_id}`

Removes a specified billable member from a group and its subgroups and projects. The user does not need to be a group member to qualify for removal. For example, if the user was added directly to a project in the group, you can still remove them using this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `user_id` | `integer` | `path` | Yes | The user ID of the member |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

