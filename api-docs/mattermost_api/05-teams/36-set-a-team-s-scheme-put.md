# 36-Set a team's scheme [PUT]

`PUT /api/v4/teams/{team_id}/scheme`

Set a team's scheme, more specifically sets the scheme_id value of a team record.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
{
  "scheme_id": string (required), // The ID of the scheme.
}
```
### Responses

#### 200 - Update team scheme successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

