# 10-Get a list of flagged posts [GET]

`GET /api/v4/users/{user_id}/posts/flagged`

Get a page of flagged posts of a user provided user id string. Selects from a channel, team, or all flagged posts by a user. Will only return posts from channels in which the user is member.
##### Permissions
Must be user or have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | ID of the user |
| `team_id` | `string` | `query` | No | Team ID |
| `channel_id` | `string` | `query` | No | Channel ID |
| `page` | `integer` | `query` | No | The page to select |
| `per_page` | `integer` | `query` | No | The number of posts per page |

### Responses

#### 200 - Post list retrieval successful

Schema (application/json):
```json
[
  {
    "order": [
      string
    ],
    "posts": {},
    "next_post_id": string, // The ID of next post. Not omitted when empty or not relevant.
    "prev_post_id": string, // The ID of previous post. Not omitted when empty or not relevant.
    "has_next": boolean, // Whether there are more items after this page.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

