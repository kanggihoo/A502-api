# 08-Get an outgoing webhook [GET]

`GET /api/v4/hooks/outgoing/{hook_id}`

Get an outgoing webhook given the hook id.
##### Permissions
`manage_webhooks` for system or `manage_webhooks` for the specific team or `manage_webhooks` for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `string` | `path` | Yes | Outgoing webhook GUID |

### Responses

#### 200 - Outgoing webhook retrieval successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier for this outgoing webhook
  "create_at": integer, // The time in milliseconds a outgoing webhook was created
  "update_at": integer, // The time in milliseconds a outgoing webhook was last updated
  "delete_at": integer, // The time in milliseconds a outgoing webhook was deleted
  "creator_id": string, // The Id of the user who created the webhook
  "team_id": string, // The ID of the team that the webhook watchs
  "channel_id": string, // The ID of a public channel that the webhook watchs
  "description": string, // The description for this outgoing webhook
  "display_name": string, // The display name for this outgoing webhook
  "trigger_words": [
    string
  ], // List of words for the webhook to trigger on
  "trigger_when": integer, // When to trigger the webhook, `0` when a trigger word is present at all and `1` if the message starts with a trigger word
  "callback_urls": [
    string
  ], // The URLs to POST the payloads to when the webhook is triggered
  "content_type": string, // The format to POST the data in, either `application/json` or `application/x-www-form-urlencoded`
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

