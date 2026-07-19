# 25-Upload license file [POST]

`POST /api/v4/license`

Upload a license to enable enterprise features.

__Minimum server version__: 4.0

##### Permissions
Must have `manage_system` permission.


### Request Body (multipart/form-data)

```json
{
  "license": string (required), // The license to be uploaded
}
```
### Responses

#### 201 - License file upload successful

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

