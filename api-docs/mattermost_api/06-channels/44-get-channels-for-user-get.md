# 44-Get channels for user [GET]

`GET /api/v4/users/{user_id}/teams/{team_id}/channels`

Get all the channels on a team for a user.
##### Permissions
Logged in as the user, or have `edit_other_users` permission, and `view_team` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `include_deleted` | `boolean` | `query` | No | Defines if deleted channels should be returned or not |
| `last_delete_at` | `integer` | `query` | No | Filters the deleted channels by this time in epoch format. Does not have any effect if include_deleted is set to false. |

### Responses

#### 200 - Channels retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a channel was created
    "update_at": integer, // The time in milliseconds a channel was last updated
    "delete_at": integer, // The time in milliseconds a channel was deleted
    "team_id": string,
    "type": string,
    "display_name": string,
    "name": string,
    "header": string,
    "purpose": string,
    "last_post_at": integer, // The time in milliseconds of the last post of a channel
    "total_msg_count": integer,
    "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
    "creator_id": string,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

