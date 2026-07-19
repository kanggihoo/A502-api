# 02-Create a scheme [POST]

`POST /api/v4/schemes`

Create a new scheme.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.0


### Request Body (application/json)

```json
{
  "name": string, // The name of the scheme
  "display_name": string (required), // The display name of the scheme
  "description": string, // The description of the scheme
  "scope": string (required), // The scope of the scheme ("team" or "channel")
}
```
### Responses

#### 201 - Scheme creation successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier of the scheme.
  "name": string, // The human readable name for the scheme.
  "description": string, // A human readable description of the scheme.
  "create_at": integer, // The time at which the scheme was created.
  "update_at": integer, // The time at which the scheme was last updated.
  "delete_at": integer, // The time at which the scheme was deleted.
  "scope": string, // The scope to which this scheme can be applied, either "team" or "channel".
  "default_team_admin_role": string, // The id of the default team admin role for this scheme.
  "default_team_user_role": string, // The id of the default team user role for this scheme.
  "default_channel_admin_role": string, // The id of the default channel admin role for this scheme.
  "default_channel_user_role": string, // The id of the default channel user role for this scheme.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

