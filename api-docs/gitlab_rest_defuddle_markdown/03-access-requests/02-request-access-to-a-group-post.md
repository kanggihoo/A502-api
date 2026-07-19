# 02-Request access to a group [POST]

`POST /api/v4/groups/{id}/access_requests`

Requests access to a specified group for the authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user |

### Responses

#### 200 - OK

Example (application/json):
```json
{
  "id": 1,
  "username": "raymond_smith",
  "name": "Raymond Smith",
  "state": "active",
  "requested_at": "2012-10-22T14:13:35Z"
}
```

#### 400 - Bad Request

#### 404 - Not Found

