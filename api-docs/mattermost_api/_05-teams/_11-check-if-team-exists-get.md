# 11-Check if team exists [GET]

`GET /api/v4/teams/name/{team_name}/exists`

Check if the team exists based on a team name.
##### Permissions
Must be authenticated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_name` | `string` | `path` | Yes | Team Name |

### Responses

#### 200 - Team retrieval successful

Schema (application/json):
```json
{
  "exists": boolean,
}
```

#### 400 - 

#### 401 - 

#### 404 - 

