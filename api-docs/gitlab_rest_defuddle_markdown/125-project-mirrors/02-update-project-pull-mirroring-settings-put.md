# 02-Update project pull mirroring settings [PUT]

`PUT /api/v4/projects/{id}/mirror/pull`

Updates pull mirroring settings for a specified project. This feature was introduced in GitLab 17.5.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "enabled": boolean, // Enables pull mirroring in a project
  "url": string, // URL of the project to pull mirror
  "auth_user": string, // The username used for authentication of a project to pull mirror
  "auth_password": string, // The password used for authentication of a project to pull mirror or a personal access token with the api scope enabled.
  "mirror_trigger_builds": boolean, // Pull mirroring triggers builds
  "only_mirror_protected_branches": boolean, // Only mirror protected branches
  "mirror_overwrites_diverged_branches": boolean, // Pull mirror overwrites diverged branches
  "mirror_branch_regex": string, // Only mirror branches with names that match this regex
  "only_protected_branches": string,
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "update_status": string,
  "url": string,
  "last_error": string,
  "last_update_at": string,
  "last_update_started_at": string,
  "last_successful_update_at": string,
  "enabled": boolean,
  "mirror_trigger_builds": boolean,
  "only_mirror_protected_branches": boolean,
  "mirror_overwrites_diverged_branches": boolean,
  "mirror_branch_regex": string,
}
```

#### 400 - Url is blocked: Only allowed schemes are http, https, ssh, git

#### 404 - Not Found

