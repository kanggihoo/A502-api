# 20-Update group membership state for a user [PUT]

`PUT /api/v4/groups/{id}/members/{user_id}/state`

Updates the membership state for a specified user in a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `user_id` | `integer` | `path` | Yes | The user ID of the user |

### Request Body (application/json)

```json
{
  "state": enum("awaiting" | "active") (required), // The new state for the memberships of the user
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

