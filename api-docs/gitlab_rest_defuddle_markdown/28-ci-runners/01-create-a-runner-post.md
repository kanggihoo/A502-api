# 01-Create a runner [POST]

`POST /api/v4/runners`

Creates a runner.

### Request Body (application/json)

```json
{
  "token": string (required), // Registration token
  "description": string, // Description of the runner
  "maintainer_note": string, // Deprecated: see `maintenance_note`
  "maintenance_note": string, // Free-form maintenance notes for the runner (1024 characters)
  "info": {
    "name": string, // Runner's name
    "version": string, // Runner's version
    "revision": string, // Runner's revision
    "platform": string, // Runner's platform
    "architecture": string, // Runner's architecture
  }, // Runner's metadata
  "active": boolean, // Deprecated: Use `paused` instead. Specifies if the runner is allowed to receive new jobs
  "paused": boolean, // Specifies if the runner should ignore new jobs
  "locked": boolean, // Specifies if the runner should be locked for the current project
  "access_level": enum("not_protected" | "ref_protected"), // The access level of the runner
  "run_untagged": boolean, // Specifies if the runner should handle untagged jobs
  "tag_list": [
    string
  ], // A list of runner tags
  "maximum_timeout": integer, // Maximum timeout that limits the amount of time (in seconds) that runners can run jobs
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

#### 410 - Gone

