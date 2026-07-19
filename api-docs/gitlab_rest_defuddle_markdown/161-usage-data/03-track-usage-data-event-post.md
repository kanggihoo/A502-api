# 03-Track usage data event [POST]

`POST /api/v4/usage_data/increment_counter`

This feature was introduced in GitLab 13.4.

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

