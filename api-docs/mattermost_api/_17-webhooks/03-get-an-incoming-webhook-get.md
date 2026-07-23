# 03-Get an incoming webhook [GET]

`GET /api/v4/hooks/incoming/{hook_id}`

Get an incoming webhook given the hook id.
##### Permissions
`manage_webhooks` for system or `manage_webhooks` for the specific team or `manage_webhooks` for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `string` | `path` | Yes | Incoming Webhook GUID |

### Responses

#### 200 - Webhook retrieval successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier for this incoming webhook
  "create_at": integer, // The time in milliseconds a incoming webhook was created
  "update_at": integer, // The time in milliseconds a incoming webhook was last updated
  "delete_at": integer, // The time in milliseconds a incoming webhook was deleted
  "last_used": integer, // The time in milliseconds this incoming webhook was last used to post a message
  "channel_id": string, // The ID of a public channel or private group that receives the webhook payloads
  "description": string, // The description for this incoming webhook
  "display_name": string, // The display name for this incoming webhook
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

