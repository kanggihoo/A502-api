# 29-Get team unreads for a user [GET]

`GET /api/v4/users/{user_id}/teams/unread`

Get the count for unread messages and mentions in the teams the user is a member of.
##### Permissions
Must be logged in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `exclude_team` | `string` | `query` | Yes | Optional team id to be excluded from the results |
| `include_collapsed_threads` | `boolean` | `query` | No | Boolean to determine whether the collapsed threads should be included or not |

### Responses

#### 200 - Team unreads retrieval successful

Schema (application/json):
```json
[
  {
    "team_id": string,
    "msg_count": integer,
    "mention_count": integer,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

