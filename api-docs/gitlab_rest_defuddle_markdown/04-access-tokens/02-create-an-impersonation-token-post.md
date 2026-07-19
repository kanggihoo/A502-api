# 02-Create an impersonation token [POST]

`POST /api/v4/users/{user_id}/impersonation_tokens`

Creates an impersonation token. These tokens are used to act on behalf of a user and can perform API calls as well as Git read and write actions. These tokens are not visible to the associated user on their profile settings page. Token values are included with the response, but cannot be retrieved later. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the user |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the impersonation token
  "description": string, // The description of the personal access token
  "expires_at": string, // The expiration date in the format YEAR-MONTH-DAY of the impersonation token
  "scopes": [
    string
  ], // The array of scopes of the impersonation token
  "granular_scopes": [
    {
      "access": enum("personal_projects" | "all_memberships" | "selected_memberships" | "user" | "instance") (required), // Access to configure for the granular scope.
      "permissions": [
        string
      ] (required), // List of permissions for the granular scope
      "project_ids": [
        integer
      ], // IDs of projects to associate with the granular scope, when access is `selected_memberships`
      "group_ids": [
        integer
      ], // IDs of groups to associate with the granular scope, when access is `selected_memberships`
    }
  ], // List of granular scopes to assign to the token
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "revoked": boolean,
  "created_at": string,
  "description": string,
  "scopes": [
    any
  ],
  "user_id": integer,
  "last_used_at": string,
  "active": boolean,
  "granular": boolean,
  "expires_at": string,
  "last_used_ips": [
    string
  ], // The five most recent unique IP addresses that have authenticated with this token. When the limit is reached, the oldest IP address is removed. The list updates once per minute per token.
  "granular_scopes": [
    {
      "access": string,
      "permissions": [
        any
      ],
      "project_id": integer,
      "group_id": integer,
    }
  ],
  "impersonation": string,
  "token": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

