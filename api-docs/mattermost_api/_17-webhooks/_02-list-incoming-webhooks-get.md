# 02-List incoming webhooks [GET]

`GET /api/v4/hooks/incoming`

Get a page of a list of incoming webhooks. Optionally filter for a specific team using query parameters.
##### Permissions
`manage_webhooks` for the system or `manage_webhooks` for the specific team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of hooks per page. |
| `team_id` | `string` | `query` | No | The ID of the team to get hooks for. |
| `include_total_count` | `boolean` | `query` | No | Appends a total count of returned hooks inside the response object - ex: `{ "incoming_webhooks": [], "total_count": 0 }`. |

### Responses

#### 200 - Incoming webhooks retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

