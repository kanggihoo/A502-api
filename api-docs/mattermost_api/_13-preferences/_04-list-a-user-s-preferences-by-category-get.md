# 04-List a user's preferences by category [GET]

`GET /api/v4/users/{user_id}/preferences/{category}`

Lists the current user's stored preferences in the given category.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `category` | `string` | `path` | Yes | The category of a group of preferences |

### Responses

#### 200 - A list of all of the current user's preferences in the given category

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

