# 40-Update a user status [PATCH]

`PATCH /api/v4/user/status`

Sets the status of the currently authenticated user. Any parameters that are not passed are ignored. This operation is similar but distinct from the Set a user status operation.

### Request Body (application/json)

```json
{
  "emoji": string, // The emoji to set on the status
  "message": string, // The status message to set
  "availability": string, // The availability of user to set
  "clear_status_after": enum("30_minutes" | "3_hours" | "8_hours" | "1_day" | "3_days" | "7_days" | "30_days"), // Automatically clear emoji, message and availability fields after a certain time
}
```
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

