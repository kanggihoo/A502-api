# 15-Get channel syncables for a group [GET]

`GET /api/v4/groups/{group_id}/channels`

Retrieve the list of channel syncables associated with the group.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 200 - Channel syncables retrieved

Schema (application/json):
```json
[
  {
    "channel_id": string,
    "channel_display_name": string,
    "channel_type": string,
    "team_id": string,
    "team_display_name": string,
    "team_type": string,
    "group_id": string,
    "auto_add": boolean,
    "create_at": integer,
    "delete_at": integer,
    "update_at": integer,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

