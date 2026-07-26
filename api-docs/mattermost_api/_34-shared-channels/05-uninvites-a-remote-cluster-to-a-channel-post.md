# 05-Uninvites a remote cluster to a channel. [POST]

`POST /api/v4/remotecluster/{remote_id}/channels/{channel_id}/uninvite`

Stops sharing a channel with a remote cluster. If the channel
was not shared with the remote, calling this endpoint will
have no effect.

##### Permissions
`manage_shared_channels`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | The remote cluster GUID |
| `channel_id` | `string` | `path` | Yes | The channel GUID to uninvite the remote cluster to |

### Responses

#### 200 - Remote cluster uninvited successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 204 - Channel was not shared with the remote cluster. No action needed.

#### 401 - 

#### 403 - 

