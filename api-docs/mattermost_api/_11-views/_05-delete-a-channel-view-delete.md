# 05-Delete a channel view [DELETE]

`DELETE /api/v4/channels/{channel_id}/views/{view_id}`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Soft-deletes a channel view. Sets `delete_at` to current timestamp.

__Minimum server version__: 11.6

##### Permissions
Must have `create_post` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `view_id` | `string` | `path` | Yes | View GUID |

### Responses

#### 200 - Channel view deletion successful

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

#### 500 - 

