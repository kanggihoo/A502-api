# 37-Convert a user into a bot [POST]

`POST /api/v4/users/{user_id}/convert_to_bot`

Convert a user into a bot.

__Minimum server version__: 5.26

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User successfully converted

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

