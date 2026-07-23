# 08-Retrieve the status of a user [GET]

`GET /api/v4/users/{user_id}/status`

Retrieves the status of a user. You can access this endpoint without authentication.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID or username of the user |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "emoji": string,
  "message": string,
  "availability": string,
  "message_html": string,
  "clear_status_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

