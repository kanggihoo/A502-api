# 18-Get a channel's pinned posts [GET]

`GET /api/v4/channels/{channel_id}/pinned`

Get a list of pinned posts for channel.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - The list of channel pinned posts

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

