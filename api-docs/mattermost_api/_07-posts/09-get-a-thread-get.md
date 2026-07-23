# 09-Get a thread [GET]

`GET /api/v4/posts/{post_id}/thread`

Get a post and the rest of the posts in the same thread.
##### Permissions
Must have `read_channel` permission for the channel the post is in or if the channel is public, have the `read_public_channels` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | ID of a post in the thread |
| `perPage` | `integer` | `query` | No | The number of posts per page |
| `fromPost` | `string` | `query` | No | The post_id to return the next page of posts from |
| `fromCreateAt` | `integer` | `query` | No | The create_at timestamp to return the next page of posts from |
| `fromUpdateAt` | `integer` | `query` | No | The update_at timestamp to return the next page of posts from. You cannot set this flag with direction=down. |
| `direction` | `string` | `query` | No | The direction to return the posts. Either up or down. |
| `skipFetchThreads` | `boolean` | `query` | No | Whether to skip fetching threads or not |
| `collapsedThreads` | `boolean` | `query` | No | Whether the client uses CRT or not |
| `collapsedThreadsExtended` | `boolean` | `query` | No | Whether to return the associated users as part of the response or not |
| `updatesOnly` | `boolean` | `query` | No | This flag is used to make the API work with the updateAt value. If you set this flag, you must set a value for fromUpdateAt. |

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

