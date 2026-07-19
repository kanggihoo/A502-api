# 04-Track usage data event for the current user [POST]

`POST /api/v4/usage_data/increment_unique_users`

Track usage data event for the current user

### Request Body (application/json)

```json
{
  "event": string (required), // The event name that should be tracked
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

