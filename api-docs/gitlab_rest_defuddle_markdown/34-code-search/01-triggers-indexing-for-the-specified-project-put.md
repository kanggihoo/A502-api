# 01-Triggers indexing for the specified project [PUT]

`PUT /api/v4/admin/zoekt/projects/{project_id}/index`

Triggers indexing for the specified project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `integer` | `path` | Yes | The id of the project you want to index |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "job_id": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

