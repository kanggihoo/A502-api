# 03-List all users [GET]

`GET /api/v4/users`

Lists all users on the instance. This endpoint supports keyset pagination. In GitLab 17.0 and later, keyset pagination is used by default.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `username` | `string` | `query` | No | Get a single user with a specific username |
| `extern_uid` | `string` | `query` | No | Get a single user with a specific external authentication provider UID |
| `public_email` | `string` | `query` | No | Get a single user with a specific public email |
| `provider` | `string` | `query` | No | The external provider |
| `search` | `string` | `query` | No | Search for a username |
| `active` | `boolean` | `query` | No | Filters only active users |
| `humans` | `boolean` | `query` | No | Filters only human users |
| `external` | `boolean` | `query` | No | Filters only external users |
| `blocked` | `boolean` | `query` | No | Filters only blocked users |
| `created_after` | `string` | `query` | No | Return users created after the specified time |
| `created_before` | `string` | `query` | No | Return users created before the specified time |
| `without_projects` | `boolean` | `query` | No | Filters only users without projects |
| `without_project_bots` | `boolean` | `query` | No | Filters users without project bots |
| `admins` | `boolean` | `query` | No | Filters only admin users |
| `two_factor` | `string` | `query` | No | Filter users by Two-factor authentication. |
| `exclude_active` | `boolean` | `query` | No | Filters only non active users |
| `exclude_external` | `boolean` | `query` | No | Filters only non external users |
| `exclude_humans` | `boolean` | `query` | No | Filters only non human users |
| `exclude_internal` | `boolean` | `query` | No | Filters only non internal users |
| `order_by` | `string` | `query` | No | Return users ordered by a field |
| `sort` | `string` | `query` | No | Return users sorted in ascending and descending order |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `with_custom_attributes` | `boolean` | `query` | No | Include custom attributes in the response |
| `custom_attributes` | `object` | `query` | No | Filter with custom attributes |
| `skip_ldap` | `boolean` | `query` | No | Skip LDAP users |
| `auditors` | `boolean` | `query` | No | Filters only auditor users |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "username": string,
  "public_email": string,
  "name": string,
  "state": string,
  "locked": boolean,
  "avatar_url": string,
  "avatar_path": string,
  "custom_attributes": [
    {
      "key": string,
      "value": string,
    }
  ],
  "web_url": string,
}
```

#### 400 - Bad Request

