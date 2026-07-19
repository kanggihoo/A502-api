# 01-Create a team [POST]

`POST /api/v4/teams`

Create a new team on the system.
##### Permissions
Must be authenticated and have the `create_team` permission.


### Request Body (application/json)

```json
{
  "name": string (required), // Unique handler for a team, will be present in the team URL
  "display_name": string (required), // Non-unique UI name for the team
  "type": string (required), // `'O'` for open, `'I'` for invite only
}
```
### Responses

#### 201 - Team creation successful

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

