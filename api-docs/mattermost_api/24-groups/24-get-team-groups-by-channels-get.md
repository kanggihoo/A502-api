# 24-Get team groups by channels [GET]

`GET /api/v4/teams/{team_id}/groups_by_channels`

Retrieve the set of groups associated with the channels in the given team grouped by channel.

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
| `paginate` | `boolean` | `query` | No | Boolean to determine whether the pagination should be applied or not |

### Responses

#### 200 - Group list retrieval successful

Schema (application/json):
```json
{
  "groups": {},
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

