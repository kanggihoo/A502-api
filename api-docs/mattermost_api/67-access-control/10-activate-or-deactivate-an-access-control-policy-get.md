# 10-Activate or deactivate an access control policy [GET]

`GET /api/v4/access_control_policies/{policy_id}/activate`

Updates the active status of an access control policy.

**Deprecated:** This endpoint will be removed in a future release. Use the dedicated access control policy update endpoint instead.
Link: </api/v4/access_control_policies/activate>; rel="successor-version"

##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |
| `active` | `boolean` | `query` | Yes | Set to "true" to activate, "false" to deactivate. |

### Responses

#### 200 - Policy active status updated successfully.

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

