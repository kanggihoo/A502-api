# 12-Unassign an access control policy from channels or teams [DELETE]

`DELETE /api/v4/access_control_policies/{policy_id}/unassign`

Unassigns an access control policy from a list of channels and/or teams.
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
  ], // The IDs of the channels to unassign the policy from.
  "team_ids": [
    string
  ], // The IDs of the teams to unassign the policy from. Requires the `manage_system` permission. Any unknown team ID is rejected with a 400. 
}
```
### Responses

#### 200 - Policy unassigned from the channels and/or teams successfully.

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

