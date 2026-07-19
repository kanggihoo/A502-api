# 42-Create a runner owned by currently authenticated user [POST]

`POST /api/v4/user/runners`

Create a new runner

### Request Body (application/json)

```json
{
  "runner_type": enum("instance_type" | "group_type" | "project_type") (required), // Specifies the scope of the runner
  "group_id": integer (required), // The ID of the group that the runner is created in
  "project_id": integer (required), // The ID of the project that the runner is created in
  "description": string, // Description of the runner
  "maintenance_note": string, // Free-form maintenance notes for the runner (1024 characters)
  "paused": boolean, // Specifies if the runner should ignore new jobs (defaults to false)
  "locked": boolean, // Specifies if the runner should be locked for the current project (defaults to false)
  "access_level": enum("not_protected" | "ref_protected"), // The access level of the runner
  "run_untagged": boolean, // Specifies if the runner should handle untagged jobs  (defaults to true)
  "tag_list": [
    string
  ], // A list of runner tags
  "maximum_timeout": integer, // Maximum timeout that limits the amount of time (in seconds) that runners can run jobs
  "token_expires_at": string, // The expiration time for the runner authentication token (ISO 8601 format). Must be between 5 minutes and 15 days in the future, and cannot exceed instance/group/project limits.
  "token_rotation_deadline": string, // The deadline for token rotation (ISO 8601 format). Must be specified with token_expires_at and be <= token_expires_at.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": string,
  "token": string,
  "token_expires_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

