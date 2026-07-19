# 06-Create a personal access token [POST]

`POST /api/v4/user/personal_access_tokens`

Creates a personal access token for the currently authenticated user. For security purposes, the token is limited to the `k8s_proxy` and `self_rotate` scope. Token values are included with the response, but cannot be retrieved later. This feature was introduced in GitLab 16.5.

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the access token
  "description": string, // The description of the access token
  "expires_at": string, // Expiration date of the access token in ISO format (YYYY-MM-DD). If undefined, the date is set to the maximum allowable lifetime limit.
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
  "scopes": [
    string
  ], // The array of scopes of the personal access token
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
  "token": string,
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
}
```

#### 400 - Bad Request

