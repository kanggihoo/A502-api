# 07-Update teams's privacy [PUT]

`PUT /api/v4/teams/{team_id}/privacy`

Updates team's privacy allowing changing a team from Public (open) to Private (invitation only) and back.

__Minimum server version__: 5.24

##### Permissions
`manage_team` permission for the team of the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
{
  "privacy": string (required), // Team privacy setting: 'O' for a public (open) team, 'I' for a private (invitation only) team
}
```
### Responses

#### 200 - Team conversion successful

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

