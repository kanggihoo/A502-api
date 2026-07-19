# 26-Remove the team icon [DELETE]

`DELETE /api/v4/teams/{team_id}/image`

Remove the team icon for the team.

__Minimum server version__: 4.10

##### Permissions
Must be authenticated and have the `manage_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Team icon successfully remove

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

