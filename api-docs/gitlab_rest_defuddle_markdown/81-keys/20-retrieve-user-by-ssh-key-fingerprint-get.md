# 20-Retrieve user by SSH key fingerprint [GET]

`GET /api/v4/keys`

Retrieves user by SSH key fingerprint. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fingerprint` | `string` | `query` | Yes | The fingerprint of an SSH key |

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

