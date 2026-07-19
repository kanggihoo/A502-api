# 28-Delete user's profile image [DELETE]

`DELETE /api/v4/users/{user_id}/image`

Delete user's profile image and reset to default image based on user_id string parameter.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.
__Minimum server version__: 5.5


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Profile image reset successful

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

