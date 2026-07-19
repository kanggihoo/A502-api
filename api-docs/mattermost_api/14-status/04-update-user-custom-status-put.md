# 04-Update user custom status [PUT]

`PUT /api/v4/users/{user_id}/status/custom`

Updates a user's custom status by setting the value in the user's props and updates the user. Also save the given custom status to the recent custom statuses in the user's props
##### Permissions
Must be logged in as the user whose custom status is being updated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |

### Request Body (application/json)

```json
{
  "emoji": string (required), // Any emoji
  "text": string (required), // Any custom status text
  "duration": string, // Duration of custom status, can be `thirty_minutes`, `one_hour`, `four_hours`, `today`, `this_week` or `date_and_time`
  "expires_at": string, // The time at which custom status should be expired. It should be in ISO format.
}
```
### Responses

#### 200 - User custom status update successful

#### 400 - 

#### 401 - 

