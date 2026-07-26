# 07-Delete a command [DELETE]

`DELETE /api/v4/commands/{command_id}`

Delete a command based on command id string.
##### Permissions
Must have `manage_slash_commands` permission for the team the command is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `command_id` | `string` | `path` | Yes | ID of the command to delete |

### Responses

#### 200 - Command deletion successful

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

