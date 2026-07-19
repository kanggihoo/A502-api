# 04-Create a user [POST]

`POST /api/v4/users`

Creates a user. Administrators only.

### Request Body (multipart/form-data)

```json
{
  "email": string (required), // The email of the user
  "password": string, // The password of the new user
  "reset_password": boolean, // Flag indicating the user will be sent a password reset token
  "skip_confirmation": boolean, // Flag indicating the account is confirmed
  "force_random_password": boolean, // Flag indicating a random password will be set
  "name": string (required), // The name of the user
  "username": string (required), // The username of the user
  "linkedin": string, // The LinkedIn username
  "twitter": string, // The Twitter username
  "discord": string, // The Discord user ID
  "website_url": string, // The website of the user
  "github": string, // The GitHub username
  "organization": string, // The organization of the user. Empty string or nil clears the field.
  "projects_limit": integer, // The number of projects a user can create
  "extern_uid": string, // The external authentication provider UID
  "provider": string, // The external provider
  "bio": string, // The biography of the user
  "location": string, // The location of the user
  "pronouns": string, // The pronouns of the user
  "public_email": string, // The public email of the user
  "commit_email": string, // The commit email, _private for private commit email
  "admin": boolean, // Flag indicating the user is an administrator
  "can_create_group": boolean, // Flag indicating the user can create groups
  "external": boolean, // Flag indicating the user is an external user
  "avatar": string, // Avatar image for user
  "theme_id": integer, // The GitLab theme for the user
  "color_scheme_id": integer, // The color scheme for the file viewer
  "private_profile": boolean, // Flag indicating the user has a private profile
  "note": string, // Admin note for this user
  "view_diffs_file_by_file": boolean, // Flag indicating the user sees only one file diff per page
  "policy_advanced_editor": boolean, // Flag indicating that advanced editor is enabled
  "shared_runners_minutes_limit": integer, // Compute minutes quota for this user
  "extra_shared_runners_minutes_limit": integer, // (admin-only) Extra compute minutes quota for this user
  "group_id_for_saml": integer, // ID for group where SAML has been configured
  "auditor": boolean, // Flag indicating auditor status of the user
}
```
### Responses

#### 201 - Created

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
  "is_admin": string,
  "note": string,
  "namespace_id": string,
  "created_by": {
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
  },
  "using_license_seat": string,
  "is_auditor": string,
  "provisioned_by_group_id": string,
  "enterprise_group_id": string,
  "enterprise_group_associated_at": string,
}
```

#### 400 - Bad Request

