# 03-Delete current brand image [DELETE]

`DELETE /api/v4/brand/image`

Deletes the previously uploaded brand image. Returns 404 if no brand image has been uploaded.
##### Permissions
Must have `manage_system` permission.
__Minimum server version: 5.6__


### Responses

#### 200 - Brand image succesfully deleted

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 404 - 

