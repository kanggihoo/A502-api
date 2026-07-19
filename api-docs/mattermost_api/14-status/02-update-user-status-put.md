# 02-Update user status [PUT]

`PUT /api/v4/users/{user_id}/status`

Manually set a user's status. When setting a user's status, the status will remain that value until set "online" again, which will return the status to being automatically updated based on user activity.
##### Permissions
Must have `edit_other_users` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |

### Request Body (application/json)

```json
{
  "user_id": string (required), // User ID
  "status": string (required), // User status, can be `online`, `away`, `offline` and `dnd`
  "dnd_end_time": integer, // Time in epoch seconds at which a dnd status would be unset.
}
```
### Responses

#### 200 - User status update successful

Schema (application/json):
```json
{
  "user_id": string,
  "status": string,
  "manual": boolean,
  "last_activity_at": integer,
}
```

#### 400 - 

#### 401 - 

