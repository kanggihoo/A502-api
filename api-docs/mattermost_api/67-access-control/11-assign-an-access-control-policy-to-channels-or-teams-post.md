# 11-Assign an access control policy to channels or teams [POST]

`POST /api/v4/access_control_policies/{policy_id}/assign`

Assigns an access control policy to a list of channels and/or teams.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |

### Request Body (application/json)

```json
{
  "channel_ids": [
    string
  ], // The IDs of the channels to assign the policy to.
  "team_ids": [
    string
  ], // The IDs of the teams to assign the policy to. Requires the `manage_system` permission. Any unknown team ID is rejected with a 400. 
}
```
### Responses

#### 200 - Policy assigned to the channels and/or teams successfully.

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

#### 500 - 

