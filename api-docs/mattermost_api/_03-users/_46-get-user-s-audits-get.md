# 46-Get user's audits [GET]

`GET /api/v4/users/{user_id}/audits`

Get a list of audit by providing the user GUID.
##### Permissions
Must be logged in as the user or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User audits retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a audit was created
    "user_id": string,
    "action": string,
    "extra_info": string,
    "ip_address": string,
    "session_id": string,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

