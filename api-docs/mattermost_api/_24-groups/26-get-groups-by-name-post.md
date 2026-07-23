# 26-Get groups by name [POST]

`POST /api/v4/groups/names`

Get a list of groups based on a provided list of names.

##### Permissions
Requires an active session but no other permissions.

__Minimum server version__: 11.0


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Group list retrieval successfully

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

#### 401 - 

#### 501 - 

