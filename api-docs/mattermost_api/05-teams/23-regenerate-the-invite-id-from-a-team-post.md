# 23-Regenerate the Invite ID from a Team [POST]

`POST /api/v4/teams/{team_id}/regenerate_invite_id`

Regenerates the invite ID used in invite links of a team
##### Permissions
Must be authenticated and have the `manage_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team Invite ID regenerated

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

