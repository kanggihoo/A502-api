# 05-Get a specific user preference [GET]

`GET /api/v4/users/{user_id}/preferences/{category}/name/{preference_name}`

Gets a single preference for the current user with the given category and name.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `category` | `string` | `path` | Yes | The category of a group of preferences |
| `preference_name` | `string` | `path` | Yes | The name of the preference |

### Responses

#### 200 - A single preference for the current user in the current categorylist of all of the current user's preferences in the given category.


Schema (application/json):
```json
{
  "user_id": string, // The ID of the user that owns this preference
  "category": string,
  "name": string,
  "value": string,
}
```

#### 400 - 

#### 401 - 

