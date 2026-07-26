# 03-Install plugin from url [POST]

`POST /api/v4/plugins/install_from_url`

Supply a URL to a plugin compressed in a .tar.gz file. Plugins must be enabled in the server's config settings.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.14


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `plugin_download_url` | `string` | `query` | Yes | URL used to download the plugin |
| `force` | `string` | `query` | No | Set to 'true' to overwrite a previously installed plugin with the same ID, if any |

### Responses

#### 201 - Plugin install successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 403 - 

#### 501 - 

