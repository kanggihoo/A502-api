# 06-Disable plugin [POST]

`POST /api/v4/plugins/{plugin_id}/disable`

Disable a previously enabled plugin. Plugins must be enabled in the server's config settings.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 4.4


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `plugin_id` | `string` | `path` | Yes | Id of the plugin to be disabled |

### Responses

#### 200 - Plugin disabled successfully

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

#### 501 - 

