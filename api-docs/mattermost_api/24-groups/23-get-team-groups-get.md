# 23-Get team groups [GET]

`GET /api/v4/teams/{team_id}/groups`

Retrieve the list of groups associated with a given team.

##### Permissions
Must have the `list_team_channels` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of groups per page. |
| `filter_allow_reference` | `boolean` | `query` | No | Boolean which filters in the group entries with the `allow_reference` attribute set. |
| `include_member_count` | `boolean` | `query` | No | Boolean which adds a `member_count` field to each group object. |
| `include_timezones` | `boolean` | `query` | No | Boolean which adds timezone information for group members. |
| `include_total_count` | `boolean` | `query` | No | Boolean which adds total count of groups in the response. |
| `include_archived` | `boolean` | `query` | No | Boolean which includes archived groups in the response. |
| `filter_archived` | `boolean` | `query` | No | Boolean which filters out archived groups from the response. |
| `filter_parent_team_permitted` | `boolean` | `query` | No | Boolean which filters groups based on parent team permissions. |
| `filter_has_member` | `string` | `query` | No | User ID to filter groups that have this member. |
| `include_member_ids` | `boolean` | `query` | No | Boolean which adds member IDs to the group objects. |
| `only_syncable_sources` | `boolean` | `query` | No | Boolean which includes groups from syncable sources. |

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

