# 02-Get current user's recaps [GET]

`GET /api/v4/recaps`

Get a paginated list of recaps created by the authenticated user.
##### Permissions
Must be authenticated.
__Minimum server version__: 11.2


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of recaps per page. |

### Responses

#### 200 - Recaps retrieval successful

Schema (application/json):
```json
[
  {
    "id": string, // Unique identifier for the recap
    "user_id": string, // ID of the user who created the recap
    "title": string, // AI-generated title for the recap (max 5 words)
    "create_at": integer, // The time in milliseconds the recap was created
    "update_at": integer, // The time in milliseconds the recap was last updated
    "delete_at": integer, // The time in milliseconds the recap was deleted
    "read_at": integer, // The time in milliseconds the recap was marked as read
    "viewed_at": integer, // The time in milliseconds the recap was marked as viewed (set in bulk when the recaps page is opened)
    "total_message_count": integer, // Total number of messages summarized across all channels
    "status": enum("pending" | "processing" | "completed" | "failed"), // Current status of the recap job
    "bot_id": string, // ID of the AI agent/bot used to generate this recap
    "channels": [
      {
        "id": string, // Unique identifier for the recap channel
        "recap_id": string, // ID of the parent recap
        "channel_id": string, // ID of the channel that was summarized
        "channel_name": string, // Display name of the channel
        "highlights": [
          string
        ], // Key discussion points and important information from the channel
        "action_items": [
          string
        ], // Tasks, todos, and action items mentioned in the channel
        "source_post_ids": [
          string
        ], // IDs of the posts used to generate this summary
        "create_at": integer, // The time in milliseconds the recap channel was created
      }
    ], // List of channel summaries included in this recap
  }
]
```

#### 400 - 

#### 401 - 

