# 04-Get a group [GET]

`GET /api/v4/groups/{group_id}`

Get group from the provided group id string

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 200 - Group retrieval successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

