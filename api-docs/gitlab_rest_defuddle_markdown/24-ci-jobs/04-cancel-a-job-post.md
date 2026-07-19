# 04-Cancel a job [POST]

`POST /api/v4/projects/{id}/jobs/{job_id}/cancel`

Cancels a specified job in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `integer` | `path` | Yes | The ID of a job |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "force": boolean, // Force cancellation for a job with a state of `canceling`
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "status": string,
  "stage": string,
  "name": string,
  "ref": string,
  "tag": boolean,
  "coverage": number,
  "allow_failure": boolean,
  "created_at": string,
  "started_at": string,
  "finished_at": string,
  "erased_at": string,
  "duration": number, // Time spent running
  "queued_duration": number, // Time spent enqueued
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
  },
  "commit": {
    "id": string,
    "short_id": string,
    "created_at": string,
    "parent_ids": [
      string
    ],
    "title": string,
    "message": string,
    "author_name": string,
    "author_email": string,
    "authored_date": string,
    "committer_name": string,
    "committer_email": string,
    "committed_date": string,
    "trailers": {},
    "extended_trailers": {},
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
  "failure_reason": string,
  "web_url": string,
  "project": string,
  "artifacts_file": {
    "filename": string,
    "size": integer,
  },
  "artifacts": [
    {
      "file_type": string,
      "size": integer,
      "filename": string,
      "file_format": string,
    }
  ],
  "runner": {
    "id": integer,
    "description": string,
    "ip_address": string,
    "active": boolean,
    "paused": boolean,
    "is_shared": boolean,
    "runner_type": string,
    "name": string,
    "online": boolean,
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
    "created_at": string,
    "status": string,
    "job_execution_status": string,
  },
  "runner_manager": {
    "id": integer,
    "system_id": string,
    "version": string,
    "revision": string,
    "platform": string,
    "architecture": string,
    "created_at": string,
    "contacted_at": string,
    "ip_address": string,
    "status": string,
    "job_execution_status": string,
  },
  "artifacts_expire_at": string,
  "archived": boolean,
  "tag_list": [
    string
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

