# 01-Upload plugin [POST]

`POST /api/v4/plugins`

Upload a plugin that is contained within a compressed .tar.gz file. Plugins and plugin uploads must be enabled in the server's config settings.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 4.4


### Request Body (multipart/form-data)

```json
{
  "plugin": string (required), // The plugin image to be uploaded
  "force": string, // Set to 'true' to overwrite a previously installed plugin with the same ID, if any
}
```
### Responses

#### 201 - Plugin upload successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

#### 501 - 

