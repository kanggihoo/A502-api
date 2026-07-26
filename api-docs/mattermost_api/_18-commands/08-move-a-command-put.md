# 08-Move a command [PUT]

`PUT /api/v4/commands/{command_id}/move`

Move a command to a different team based on command id string.
##### Permissions
Must have `manage_slash_commands` permission for the team the command is currently in and the destination team.

__Minimum server version__: 5.22


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `command_id` | `string` | `path` | Yes | ID of the command to move |

### Request Body (application/json)

```json
{
  "team_id": string, // Destination teamId
}
```
### Responses

#### 200 - Command move successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

