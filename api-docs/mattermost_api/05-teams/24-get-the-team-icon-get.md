# 24-Get the team icon [GET]

`GET /api/v4/teams/{team_id}/image`

Get the team icon of the team.

__Minimum server version__: 4.9

##### Permissions
User must be authenticated. In addition, team must be open or the user must have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team icon retrieval successful

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

