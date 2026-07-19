# 17-Activate or deactivate access control policies [PUT]

`PUT /api/v4/access_control_policies/activate`

Updates the active status of access control policies.

##### Permissions
Must have the `manage_system` permission. OR be a channel admin with manage_channel_access_rules permission for the specified channels.


### Request Body (application/json)

```json
{
  "entries": [
    {
      "id": string, // The ID of the policy.
      "active": boolean, // The active status of the policy.
    }
  ],
}
```
### Responses

#### 200 - Access control policies active status updated successfully.

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

#### 500 - 

#### 501 - 

