# 31-Create a merge request pipeline [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/pipelines`

Creates a merge request pipeline. Pipelines created with this operation must configure `.gitlab-ci.yml` with `only: [merge_requests]` to create jobs.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "async": boolean, // Indicates if the merge request pipeline creation should be performed asynchronously. If set to `true`, the pipeline will be created outside of the API request and the endpoint will return an empty response with a `202` status code. When the response is `202`, the creation can still fail outside of this request.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
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
  "before_sha": string,
  "tag": boolean,
  "yaml_errors": string,
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
  "started_at": string,
  "finished_at": string,
  "committed_at": string,
  "duration": integer, // Time spent running in seconds
  "queued_duration": integer, // Time spent enqueued in seconds
  "coverage": number,
  "detailed_status": {
    "icon": string,
    "text": string,
    "label": string,
    "group": string,
    "tooltip": string,
    "has_details": boolean,
    "details_path": string,
    "illustration": {},
    "favicon": string,
    "action": string,
  },
  "archived": boolean,
}
```

#### 400 - Bad request

#### 404 - Not found

#### 405 - Method not allowed

