# 03-Delete user's preferences [POST]

`POST /api/v4/users/{user_id}/preferences/delete`

Delete a list of the user's preferences.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
[
  {
    "user_id": string, // The ID of the user that owns this preference
    "category": string,
    "name": string,
    "value": string,
  }
]
```
### Responses

#### 200 - User preferences saved successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

