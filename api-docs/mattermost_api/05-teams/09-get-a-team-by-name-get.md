# 09-Get a team by name [GET]

`GET /api/v4/teams/name/{team_name}`

Get a team based on provided name string
##### Permissions
Must be authenticated, team type is open and have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_name` | `string` | `path` | Yes | Team Name |

### Responses

#### 200 - Team retrieval successful

Schema (application/json):
```json
{
  "id": string,
  "create_at": integer, // The time in milliseconds a team was created
  "update_at": integer, // The time in milliseconds a team was last updated
  "delete_at": integer, // The time in milliseconds a team was deleted
  "display_name": string,
  "name": string,
  "description": string,
  "email": string,
  "type": string,
  "allowed_domains": string,
  "invite_id": string,
  "allow_open_invite": boolean,
  "policy_id": string, // The data retention policy to which this team has been assigned. If no such policy exists, or the caller does not have the `sysconsole_read_compliance_data_retention` permission, this field will be null.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

