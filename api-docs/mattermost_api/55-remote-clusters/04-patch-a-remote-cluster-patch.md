# 04-Patch a remote cluster. [PATCH]

`PATCH /api/v4/remotecluster/{remote_id}`

Partially update a Remote Cluster by providing only the fields you want to update. Ommited fields will not be updated.

##### Permissions
`manage_secure_connections`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | Remote Cluster GUID |

### Request Body (application/json)

```json
{
  "display_name": string,
  "default_team_id": string, // The team where channels from invites are created
}
```
### Responses

#### 200 - Remote Cluster patch successful

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

#### 404 - 

