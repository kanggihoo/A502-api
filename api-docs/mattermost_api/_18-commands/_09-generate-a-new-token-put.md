# 09-Generate a new token [PUT]

`PUT /api/v4/commands/{command_id}/regen_token`

Generate a new token for the command based on command id string.
##### Permissions
Must have `manage_slash_commands` permission for the team the command is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `command_id` | `string` | `path` | Yes | ID of the command to generate the new token |

### Responses

#### 200 - Token generation successful

Schema (application/json):
```json
{
  "token": string, // The new token
}
```

#### 400 - 

#### 401 - 

#### 403 - 

