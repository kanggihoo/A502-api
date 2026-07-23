# 15-Get posts around oldest unread [GET]

`GET /api/v4/users/{user_id}/channels/{channel_id}/posts/unread`

Get the oldest unread post in the channel for the given user as well as the posts around it. The returned list is sorted in descending order (most recent post first).
##### Permissions
Must be logged in as the user or have `edit_other_users` permission, and must have `read_channel` permission for the channel.
__Minimum server version__: 5.14


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | ID of the user |
| `channel_id` | `string` | `path` | Yes | The channel ID to get the posts for |
| `limit_before` | `integer` | `query` | No | Number of posts before the oldest unread posts. Maximum is 200 posts if limit is set greater than that. |
| `limit_after` | `integer` | `query` | No | Number of posts after and including the oldest unread post. Maximum is 200 posts if limit is set greater than that. |
| `skipFetchThreads` | `boolean` | `query` | No | Whether to skip fetching threads or not |
| `collapsedThreads` | `boolean` | `query` | No | Whether the client uses CRT or not |
| `collapsedThreadsExtended` | `boolean` | `query` | No | Whether to return the associated users as part of the response or not |

### Responses

#### 200 - Post list retrieval successful

Schema (application/json):
```json
{
  "order": [
    string
  ],
  "posts": {},
  "next_post_id": string, // The ID of next post. Not omitted when empty or not relevant.
  "prev_post_id": string, // The ID of previous post. Not omitted when empty or not relevant.
  "has_next": boolean, // Whether there are more items after this page.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

