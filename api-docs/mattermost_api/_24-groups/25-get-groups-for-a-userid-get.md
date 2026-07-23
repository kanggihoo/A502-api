# 25-Get groups for a userId [GET]

`GET /api/v4/users/{user_id}/groups`

Retrieve the list of groups associated to the user

__Minimum server version__: 5.24


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Group list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "name": string,
    "display_name": string,
    "description": string,
    "source": string,
    "remote_id": string,
    "create_at": integer,
    "update_at": integer,
    "delete_at": integer,
    "has_syncables": boolean,
  }
]
```

#### 400 - 

#### 501 - 

