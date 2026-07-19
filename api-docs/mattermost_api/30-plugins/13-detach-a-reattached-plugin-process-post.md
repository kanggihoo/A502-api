# 13-Detach a reattached plugin process [POST]

`POST /api/v4/plugins/{plugin_id}/detach`

Detaches a previously reattached plugin from the server.
This endpoint is only exposed over a local socket.

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `plugin_id` | `string` | `path` | Yes | The ID of the plugin to detach. |

### Responses

#### 200 - Plugin detached successfully

#### 401 - 

#### 403 - 

#### 404 - 

