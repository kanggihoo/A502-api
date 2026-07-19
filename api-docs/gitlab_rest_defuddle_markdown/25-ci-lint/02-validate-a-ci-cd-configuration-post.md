# 02-Validate a CI/CD configuration [POST]

`POST /api/v4/projects/{id}/ci/lint`

Validates a provided CI/CD configuration in the context of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "content": string (required), // Content of .gitlab-ci.yml
  "dry_run": boolean, // Run pipeline creation simulation, or only do static check. This is false by default
  "include_jobs": boolean, // If the list of jobs that would exist in a static check or pipeline         simulation should be included in the response. This is false by default
  "ref": string, // When dry_run is true, sets the branch or tag to use. Defaults to the project’s default branch when not set
}
```
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

#### 404 - Not Found

