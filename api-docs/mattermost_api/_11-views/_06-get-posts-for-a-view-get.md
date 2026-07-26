# 06-Get posts for a view [GET]

`GET /api/v4/channels/{channel_id}/views/{view_id}/posts`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Get a paginated list of posts that belong to a specific view.

__Minimum server version__: 11.6

##### Permissions
Must have `read_channel_content` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `view_id` | `string` | `path` | Yes | View GUID |
| `page` | `integer` | `query` | No | The 0-based page number for pagination (default 0) |
| `per_page` | `integer` | `query` | No | The number of posts per page (default 60, max 200) |

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

#### 404 - 

#### 500 - 

