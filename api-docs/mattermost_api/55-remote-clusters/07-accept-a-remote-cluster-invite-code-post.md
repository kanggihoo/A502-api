# 07-Accept a remote cluster invite code. [POST]

`POST /api/v4/remotecluster/accept_invite`

Accepts a remote cluster invite code.

##### Permissions
`manage_secure_connections`


### Request Body (application/json)

```json
{
  "invite": string (required),
  "name": string (required),
  "display_name": string,
  "default_team_id": string (required),
  "password": string (required), // The password to decrypt the invite code.
}
```
### Responses

#### 201 - Invite successfully accepted

Schema (application/json):
```json
{
  "remote_id": string,
  "remote_team_id": string,
  "name": string,
  "display_name": string,
  "site_url": string, // URL of the remote cluster
  "default_team_id": string, // The team where channels from invites are created
  "create_at": integer, // Time in milliseconds that the remote cluster was created
  "delete_at": integer, // Time in milliseconds that the remote cluster record was deleted
  "last_ping_at": integer, // Time in milliseconds when the last ping to the remote cluster was run
  "token": string,
  "remote_token": string,
  "topics": string,
  "creator_id": string,
  "plugin_id": string,
  "options": integer, // A bitmask with a set of option flags
}
```

#### 401 - 

#### 403 - 

