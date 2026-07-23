# 21-Get a team stats [GET]

`GET /api/v4/teams/{team_id}/stats`

Get a team stats on the system.
##### Permissions
Must be authenticated and have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team stats retrieval successful

Schema (application/json):
```json
{
  "team_id": string,
  "total_member_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

