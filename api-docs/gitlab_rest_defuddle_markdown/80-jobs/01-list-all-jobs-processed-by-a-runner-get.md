# 01-List all jobs processed by a runner [GET]

`GET /api/v4/runners/{id}/jobs`

Lists all jobs that are being processed or were processed by a specified runner. The list of jobs is limited to projects where the user has the Reporter, Developer, Maintainer, or Owner role.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a runner |
| `system_id` | `string` | `query` | No | System ID associated with the runner manager |
| `status` | `string` | `query` | No | Status of the job |
| `order_by` | `string` | `query` | No | Order by `id` |
| `sort` | `string` | `query` | No | Sort by `asc` or `desc` order. Specify `order_by` as well, including for `id` |
| `cursor` | `string` | `query` | No | Cursor for obtaining the next set of records |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

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
  "project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - No access granted

#### 404 - Runner not found

