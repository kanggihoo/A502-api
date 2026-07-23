# 14-Get posts for a channel [GET]

`GET /api/v4/channels/{channel_id}/posts`

Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint. The parameter `since` must not be used with any of `before`, `after`, `page`, and `per_page` parameters.
If `since` is used, it will always return all posts modified since that time, ordered by their create time limited till 1000. A caveat with this parameter is that there is no guarantee that the returned posts will be consecutive. It is left to the clients to maintain state and fill any missing holes in the post order.
##### Permissions
Must have `read_channel` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | The channel ID to get the posts for |
| `page` | `integer` | `query` | No | The page to select |
| `per_page` | `integer` | `query` | No | The number of posts per page |
| `since` | `integer` | `query` | No | Provide a non-zero value in Unix time milliseconds to select posts modified after that time |
| `before` | `string` | `query` | No | A post id to select the posts that came before this one |
| `after` | `string` | `query` | No | A post id to select the posts that came after this one |
| `include_deleted` | `boolean` | `query` | No | Whether to include deleted posts or not. Must have system admin permissions. |
| `type` | `string` | `query` | No | Filter posts by type. |

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

