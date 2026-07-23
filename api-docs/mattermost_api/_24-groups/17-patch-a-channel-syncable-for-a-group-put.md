# 17-Patch a channel syncable for a group [PUT]

`PUT /api/v4/groups/{group_id}/channels/{channel_id}/patch`

Partially update a GroupSyncableChannel by providing only the fields you want to update. Omitted fields will not be updated.
##### Permissions Must have `manage_system` permission.
__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `channel_id` | `string` | `path` | Yes | Channel GUID. |

### Request Body (application/json)

```json
{
  "auto_add": boolean,
}
```
### Responses

#### 200 - Channel syncable patched

Schema (application/json):
```json
{
  "channel_id": string,
  "group_id": string,
  "auto_add": boolean,
  "create_at": integer,
  "delete_at": integer,
  "update_at": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

