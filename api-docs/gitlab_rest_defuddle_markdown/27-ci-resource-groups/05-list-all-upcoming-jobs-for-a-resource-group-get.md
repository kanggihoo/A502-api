# 05-List all upcoming jobs for a resource group [GET]

`GET /api/v4/projects/{id}/resource_groups/{key}/upcoming_jobs`

Lists all upcoming jobs for a specified resource group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key` | `string` | `path` | Yes | The key of the resource group |
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
  "project": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

