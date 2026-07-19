# 01-Get user status [GET]

`GET /api/v4/users/{user_id}/status`

Get user status by id from the server.
##### Permissions
Must be authenticated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User ID |

### Responses

#### 200 - User status retrieval successful

Schema (application/json):
```json
{
  "user_id": string,
  "status": string,
  "manual": boolean,
  "last_activity_at": integer,
}
```

#### 400 - 

#### 401 - 

