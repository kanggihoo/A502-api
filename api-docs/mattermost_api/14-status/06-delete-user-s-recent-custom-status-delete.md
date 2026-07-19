# 06-Delete user's recent custom status [DELETE]

`DELETE /api/v4/users/{user_id}/status/custom/recent`

Deletes a user's recent custom status by removing the specific status from the recentCustomStatuses in the user's props and updates the user.
##### Permissions
Must be logged in as the user whose recent custom status is being deleted.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |

### Request Body (application/json)

```json
{
  "emoji": string (required), // Any emoji
  "text": string (required), // Any custom status text
  "duration": string (required), // Duration of custom status, can be `thirty_minutes`, `one_hour`, `four_hours`, `today`, `this_week` or `date_and_time`
  "expires_at": string (required), // The time at which custom status should be expired. It should be in ISO format.
}
```
### Responses

#### 200 - User recent custom status delete successful

#### 400 - 

#### 401 - 

