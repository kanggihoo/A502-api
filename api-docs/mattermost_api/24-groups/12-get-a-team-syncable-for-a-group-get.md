# 12-Get a team syncable for a group [GET]

`GET /api/v4/groups/{group_id}/teams/{team_id}`

Get the GroupSyncableTeam object with the provided group and team identifiers.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `team_id` | `string` | `path` | Yes | Team GUID. |

### Responses

#### 200 - Team syncable retrieved

Schema (application/json):
```json
{
  "team_id": string,
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

