# 41-Retrieve your user status [GET]

`GET /api/v4/user/status`

Retrieves your user status.

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

#### 401 - Unauthorized

#### 403 - Forbidden

