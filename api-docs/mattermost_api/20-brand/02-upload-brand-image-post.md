# 02-Upload brand image [POST]

`POST /api/v4/brand/image`

Uploads a brand image.
##### Permissions
Must have `manage_system` permission.


### Request Body (multipart/form-data)

```json
{
  "image": string (required), // The image to be uploaded
}
```
### Responses

#### 201 - Brand image upload successful

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

