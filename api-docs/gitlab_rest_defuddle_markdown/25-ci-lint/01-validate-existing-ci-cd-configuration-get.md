# 01-Validate existing CI/CD configuration [GET]

`GET /api/v4/projects/{id}/ci/lint`

Validates the `.gitlab-ci.yml` configuration for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `sha` | `string` | `query` | No | Deprecated: Use content_ref instead |
| `content_ref` | `string` | `query` | No | The CI/CD configuration content is taken from this commit SHA, branch or tag. Defaults to the HEAD of the project's default branch |
| `dry_run` | `boolean` | `query` | No | Run pipeline creation simulation, or only do static check. This is false by default |
| `include_jobs` | `boolean` | `query` | No | If the list of jobs that would exist in a static check or pipeline<br>        simulation should be included in the response. This is false by default |
| `ref` | `string` | `query` | No | Deprecated: Use dry_run_ref instead |
| `dry_run_ref` | `string` | `query` | No | Branch or tag used as context when executing a dry run. Defaults to the default branch of the project. Only used when dry_run is true |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "valid": boolean,
  "errors": [
    string
  ],
  "warnings": [
    string
  ],
  "merged_yaml": string,
  "includes": [
    {
      "type": string,
      "location": string,
      "blob": string,
      "raw": string,
      "extra": {},
      "context_project": string,
      "context_sha": string,
    }
  ],
  "jobs": [
    {}
  ],
}
```

#### 400 - Bad Request

#### 404 - Not found

