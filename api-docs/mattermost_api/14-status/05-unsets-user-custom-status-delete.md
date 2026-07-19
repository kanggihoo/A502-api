# 05-Unsets user custom status [DELETE]

`DELETE /api/v4/users/{user_id}/status/custom`

Unsets a user's custom status by updating the user's props and updates the user
##### Permissions
Must be logged in as the user whose custom status is being removed.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |

### Responses

#### 200 - User custom status delete successful

#### 400 - 

#### 401 - 

