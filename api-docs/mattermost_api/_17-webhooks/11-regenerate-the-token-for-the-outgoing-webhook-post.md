# 11-Regenerate the token for the outgoing webhook. [POST]

`POST /api/v4/hooks/outgoing/{hook_id}/regen_token`

Regenerate the token for the outgoing webhook.
##### Permissions
`manage_webhooks` for system or `manage_webhooks` for the specific team or `manage_webhooks` for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `string` | `path` | Yes | Outgoing webhook GUID |

### Responses

#### 200 - Webhook token regenerate successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

