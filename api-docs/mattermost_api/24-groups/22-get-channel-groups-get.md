# 22-Get channel groups [GET]

`GET /api/v4/channels/{channel_id}/groups`

Retrieve the list of groups associated with a given channel.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of groups per page. |
| `filter_allow_reference` | `boolean` | `query` | No | Boolean which filters the group entries with the `allow_reference` attribute set. |

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

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

