# 69-Get all channel members from all teams for a user [GET]

`GET /api/v4/users/{user_id}/channel_members`

Get all channel members from all teams for a user.

__Minimum server version__: 6.2.0

##### Permissions
Logged in as the user, or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `page` | `integer` | `query` | No | Page specifies which part of the results to return, by perPage. |
| `per_page` | `integer` | `query` | No | The size of the returned chunk of results. |

### Responses

#### 200 - User's uploads retrieval successful

Schema (application/json):
```json
[
  any
]
```

#### 400 - 

#### 401 - 

#### 404 - 

