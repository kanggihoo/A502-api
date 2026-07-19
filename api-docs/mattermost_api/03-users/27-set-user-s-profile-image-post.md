# 27-Set user's profile image [POST]

`POST /api/v4/users/{user_id}/image`

Set a user's profile image based on user_id string parameter.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (multipart/form-data)

```json
{
  "image": string (required), // The image to be uploaded
}
```
### Responses

#### 200 - Profile image set successful

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

