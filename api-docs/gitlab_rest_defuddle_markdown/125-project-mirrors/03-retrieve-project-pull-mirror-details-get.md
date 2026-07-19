# 03-Retrieve project pull mirror details [GET]

`GET /api/v4/projects/{id}/mirror/pull`

Retrieves pull mirror details for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

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

#### 400 - The project is not mirrored

#### 404 - Not Found

