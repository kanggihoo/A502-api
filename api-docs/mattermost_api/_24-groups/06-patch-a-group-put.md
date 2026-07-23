# 06-Patch a group [PUT]

`PUT /api/v4/groups/{group_id}/patch`

Partially update a group by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |

### Request Body (application/json)

```json
{
  "name": string,
  "display_name": string,
  "description": string,
}
```
### Responses

#### 200 - Group patch successful

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

