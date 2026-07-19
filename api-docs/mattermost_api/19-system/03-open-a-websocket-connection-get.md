# 03-Open a WebSocket connection [GET]

`GET /api/v4/websocket`

Upgrades the HTTP connection to a WebSocket connection used for real-time events and websocket actions.

##### Permissions
No permission required to connect. Authentication can be performed via standard API auth (cookie/header)
or by sending an `authentication_challenge` action after connecting.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `connection_id` | `string` | `query` | No | Existing connection identifier for reconnect flows. |
| `sequence_number` | `string` | `query` | No | Last received sequence number for reconnect flows. |
| `posted_ack` | `boolean` | `query` | No | Whether post acknowledgement events are enabled for this connection. |
| `disconnect_err_code` | `string` | `query` | No | Optional close code used by clients to indicate disconnect reason. |

### Responses

#### 101 - Switching Protocols

#### 400 - 

