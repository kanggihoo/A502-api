# 08-Get an access control policy [GET]

`GET /api/v4/access_control_policies/{policy_id}`

Gets a specific access control policy by its ID.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |

### Responses

#### 200 - Access control policy retrieved successfully.

Schema (application/json):
```json
{
  "id": string, // The unique identifier of the policy.
  "name": string, // The unique name for the policy.
  "display_name": string, // The human-readable name for the policy.
  "description": string, // A description of the policy.
  "expression": string, // The CEL expression defining the policy rules.
  "is_active": boolean, // Whether the policy is currently active and enforced.
  "create_at": integer, // The time in milliseconds the policy was created.
  "update_at": integer, // The time in milliseconds the policy was last updated.
  "delete_at": integer, // The time in milliseconds the policy was deleted.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

