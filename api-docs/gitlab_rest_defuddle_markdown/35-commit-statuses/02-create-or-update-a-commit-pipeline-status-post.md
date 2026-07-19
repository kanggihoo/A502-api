# 02-Create or update a commit pipeline status [POST]

`POST /api/v4/projects/{id}/statuses/{sha}`

Creates or updates the status of a commit represented by a job in an `external` stage. If the commit is associated with a merge request, target the commit in the merge request source branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project. |
| `sha` | `string` | `path` | Yes | The commit hash |

### Request Body (application/json)

```json
{
  "state": enum("pending" | "running" | "success" | "failed" | "canceled" | "skipped") (required), // The state of the status
  "ref": string, // The ref
  "target_url": string, // The target URL to associate with this status
  "description": string, // A short description of the status
  "name": string, // A string label to differentiate this status from the status of other systems
  "context": string, // A string label to differentiate this status from the status of other systems
  "coverage": number, // The total code coverage
  "pipeline_id": integer, // An existing pipeline ID, when multiple pipelines on the same commit SHA have been triggered
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "sha": string,
  "ref": string,
  "status": string,
  "name": string,
  "target_url": string,
  "description": string,
  "created_at": string,
  "started_at": string,
  "finished_at": string,
  "allow_failure": boolean,
  "coverage": number,
  "pipeline_id": integer,
  "author": {
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
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Another update to this commit status is in progress

