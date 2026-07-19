# 01-Get the user's preferences [GET]

`GET /api/v4/users/{user_id}/preferences`

Get a list of the user's preferences.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User preferences retrieval successful

Schema (application/json):
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

#### 400 - 

#### 401 - 

#### 403 - 

