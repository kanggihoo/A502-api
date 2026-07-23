# 22-Get the access control policy for a team [GET]

`GET /api/v4/teams/{team_id}/access_control/policy`

Get the attribute-based access control policy assigned to a team, along
with whether the team currently enforces a membership policy. `policy` is
null when no policy is assigned or attribute-based access control is not
available on the server.
##### Permissions
Must have the `manage_system` permission or the `manage_team_access_rules`
permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team access control policy retrieval successful

Schema (application/json):
```json
{
  "policy": any,
  "enforced": boolean, // Whether the team currently enforces a membership access control policy.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

