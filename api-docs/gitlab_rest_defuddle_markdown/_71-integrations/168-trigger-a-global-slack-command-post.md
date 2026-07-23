# 168-Trigger a global slack command [POST]

`POST /api/v4/slack/trigger`

Added in GitLab 9.4

### Request Body (application/json)

```json
{
  "text": string (required), // Text of the slack command
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

