# 45-Get all channels from all teams [GET]

`GET /api/v4/users/{user_id}/channels`

Get all channels from all teams that a user is a member of.

__Minimum server version__: 6.1

##### Permissions

Logged in as the user, or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `last_delete_at` | `integer` | `query` | No | Filters the deleted channels by this time in epoch format. Does not have any effect if include_deleted is set to false. |
| `include_deleted` | `boolean` | `query` | No | Defines if deleted channels should be returned or not |

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

