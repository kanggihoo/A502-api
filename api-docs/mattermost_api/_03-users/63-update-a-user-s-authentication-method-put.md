# 63-Update a user's authentication method [PUT]

`PUT /api/v4/users/{user_id}/auth`

Updates a user's authentication method. This can be used to change them to/from LDAP authentication for example.

For `auth_service` set to `email`, omit `auth_data`; this clears external authentication and switches the user to email authentication. For other authentication services, `auth_data` must be present and non-empty.

__Minimum server version__: 4.6
##### Permissions
Must have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "auth_data": string, // Service-specific authentication data. Required and must be non-empty for external authentication services. Omit this field when `auth_service` is `email`.
  "auth_service": string (required), // The authentication service such as "email", "gitlab", or "ldap". Use "email" with omitted `auth_data` to clear external authentication.
}
```
### Responses

#### 200 - User auth update successful

Schema (application/json):
```json
{
  "auth_data": string, // Service-specific authentication data. Required and must be non-empty for external authentication services. Omit this field when `auth_service` is `email`.
  "auth_service": string (required), // The authentication service such as "email", "gitlab", or "ldap". Use "email" with omitted `auth_data` to clear external authentication.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

