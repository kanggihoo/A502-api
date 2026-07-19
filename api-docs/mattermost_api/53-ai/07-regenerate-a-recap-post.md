# 07-Regenerate a recap [POST]

`POST /api/v4/recaps/{recap_id}/regenerate`

Regenerate a recap by its ID. This creates a new background job to regenerate the AI-powered recap with the latest messages from the specified channels.
##### Permissions
Must be authenticated. Can only regenerate recaps created by the current user.
__Minimum server version__: 11.2


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `recap_id` | `string` | `path` | Yes | Recap GUID |

### Responses

#### 200 - Recap regeneration initiated successfully

Schema (application/json):
```json
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
```

#### 401 - 

#### 403 - 

#### 404 - 

