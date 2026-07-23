# 26-Get user's profile image [GET]

`GET /api/v4/users/{user_id}/image`

Get a user's profile image based on user_id string parameter.
##### Permissions
Must be logged in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `_` | `number` | `query` | No | Not used by the server. Clients can pass in the last picture update time of the user to potentially take advantage of caching |

### Responses

#### 200 - User's profile image

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

