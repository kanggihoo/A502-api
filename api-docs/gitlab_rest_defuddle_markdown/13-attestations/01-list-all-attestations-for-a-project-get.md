# 01-List all attestations for a project [GET]

`GET /api/v4/projects/{id}/attestations/{subject_digest}`

Lists all attestations for a specified project and artifact hash. This feature was introduced in GitLab 18.7.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `subject_digest` | `string` | `path` | Yes | The SHA-256 hash of the artifact |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "created_at": string,
  "updated_at": string,
  "expire_at": string,
  "project_id": integer,
  "build_id": integer,
  "status": string,
  "predicate_kind": string,
  "predicate_type": string,
  "subject_digest": string,
  "download_url": string,
}
```

#### 400 - Bad Request

#### 404 - Artifact SHA-256 not found

