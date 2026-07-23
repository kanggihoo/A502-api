# 13-Get a channel syncable for a group [GET]

`GET /api/v4/groups/{group_id}/channels/{channel_id}`

Get the GroupSyncableChannel object with the provided group and channel identifiers.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `channel_id` | `string` | `path` | Yes | Channel GUID. |

### Responses

#### 200 - Channel syncable retrieved

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

#### 500 - 

#### 501 - 

