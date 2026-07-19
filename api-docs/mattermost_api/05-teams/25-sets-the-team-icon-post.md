# 25-Sets the team icon [POST]

`POST /api/v4/teams/{team_id}/image`

Sets the team icon for the team.

__Minimum server version__: 4.9

##### Permissions
Must be authenticated and have the `manage_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (multipart/form-data)

```json
{
  "image": string (required), // The image to be uploaded
}
```
### Responses

#### 200 - Team icon successfully set

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

