# 04-Invites a remote cluster to a channel. [POST]

`POST /api/v4/remotecluster/{remote_id}/channels/{channel_id}/invite`

Invites a remote cluster to a channel, sharing the channel if
needed. If the remote cluster was already invited to the
channel, calling this endpoint will have no effect.

##### Permissions
`manage_shared_channels`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | The remote cluster GUID |
| `channel_id` | `string` | `path` | Yes | The channel GUID to invite the remote cluster to |

### Responses

#### 200 - Remote cluster invited successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

