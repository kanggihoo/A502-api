# 04-Add a merge request to a merge train [POST]

`POST /api/v4/projects/{id}/merge_trains/merge_requests/{merge_request_iid}`

Adds a specified merge request to a merge train.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "sha": string, // If present, then the SHA must match the HEAD of the source branch, otherwise the merge fails.
  "squash": boolean, // When true, the commits will be squashed into a single commit on merge
  "when_pipeline_succeeds": boolean, // Deprecated. Use the auto_merge parameter instead.
  "auto_merge": boolean, // When true, this merge request will be set to auto merge
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "merge_request": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "user": {
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
  "pipeline": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "sha": string,
    "ref": string,
    "status": string,
    "source": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "created_at": string,
  "updated_at": string,
  "target_branch": string,
  "status": string,
  "merged_at": string,
  "duration": integer, // Time spent in seconds
}
```

#### 202 - Accepted

Schema (application/json):
```json
{
  "id": integer,
  "merge_request": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "user": {
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
  "pipeline": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "sha": string,
    "ref": string,
    "status": string,
    "source": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "created_at": string,
  "updated_at": string,
  "target_branch": string,
  "status": string,
  "merged_at": string,
  "duration": integer, // Time spent in seconds
}
```

#### 400 - Failed to merge

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

