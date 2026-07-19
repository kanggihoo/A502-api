# 01-List all enterprise users [GET]

`GET /api/v4/groups/{id}/enterprise_users`

Lists all enterprise users for a specified top-level group. Use the `page` and `per_page` pagination parameters to filter the results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `username` | `string` | `query` | No | Return single user with a specific username. |
| `search` | `string` | `query` | No | Search users by name, email, username. |
| `active` | `boolean` | `query` | No | Return only active users. |
| `blocked` | `boolean` | `query` | No | Return only blocked users. |
| `created_after` | `string` | `query` | No | Return users created after the specified time. |
| `created_before` | `string` | `query` | No | Return users created before the specified time. |
| `two_factor` | `string` | `query` | No | Filter users by two-factor authentication (2FA). Filter values are `enabled` or `disabled`. By default it returns all users. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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
  "created_at": string,
  "bio": string,
  "location": string,
  "linkedin": string,
  "twitter": string,
  "discord": string,
  "website_url": string,
  "github": string,
  "job_title": string,
  "pronouns": string,
  "organization": string,
  "bot": boolean,
  "work_information": string,
  "followers": string,
  "following": string,
  "is_followed": string,
  "local_time": string,
  "last_sign_in_at": string,
  "confirmed_at": string,
  "last_activity_on": string,
  "email": string,
  "theme_id": integer,
  "color_scheme_id": integer,
  "projects_limit": integer,
  "current_sign_in_at": string,
  "identities": {
    "provider": string,
    "extern_uid": string,
    "saml_provider_id": string,
  },
  "can_create_group": boolean,
  "can_create_project": boolean,
  "two_factor_enabled": boolean,
  "external": boolean,
  "private_profile": boolean,
  "commit_email": string,
  "preferred_language": string,
  "shared_runners_minutes_limit": string,
  "extra_shared_runners_minutes_limit": string,
  "scim_identities": {
    "extern_uid": string,
    "group_id": string,
    "active": string,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

