# 06-Search access control policies [POST]

`POST /api/v4/access_control_policies/search`

Searches for access control policies based on given criteria.
##### Permissions
Must have the `manage_system` permission.


### Request Body (application/json)

```json
{
  "term": string, // The search term to match against policy names or display names.
  "type": string, // The type of policy (e.g., 'parent' or 'channel').
  "parent_id": string, // The ID of the parent policy to search within.
  "ids": [
    string
  ], // List of policy IDs to filter by.
  "active": boolean, // Filter policies by active status.
  "include_children": boolean, // Whether to include child policies in the result.
  "cursor": {
    "id": string, // The ID of the policy to start searching after.
  },
  "limit": integer, // The maximum number of policies to return.
}
```
### Responses

#### 200 - Search results for access control policies.

Schema (application/json):
```json
{
  "policies": [
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
  ],
  "total_count": integer, // The total number of policies.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

