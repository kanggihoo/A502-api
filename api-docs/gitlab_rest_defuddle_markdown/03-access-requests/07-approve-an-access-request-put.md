# 07-Approve an access request [PUT]

`PUT /api/v4/projects/{id}/access_requests/{user_id}/approve`

Approves an access request for a specified user in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `user_id` | `integer` | `path` | Yes | The user ID of the access requester |

### Request Body (application/json)

```json
{
  "access_level": integer, // A valid access level (defaults: `30`, the Developer role)
}
```
### Responses

#### 201 - Created

Example (application/json):
```json
{
  "id": 1,
  "username": "raymond_smith",
  "name": "Raymond Smith",
  "state": "active",
  "created_at": "2012-10-22T14:13:35Z",
  "access_level": "20"
}
```

#### 400 - Bad Request

#### 404 - Not Found

