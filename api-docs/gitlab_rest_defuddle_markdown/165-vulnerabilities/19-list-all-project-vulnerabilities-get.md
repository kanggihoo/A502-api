# 19-List all project vulnerabilities [GET]

`GET /api/v4/projects/{id}/vulnerabilities`

Lists all vulnerabilities for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "description": string,
  "state": string,
  "severity": string,
  "report_type": string,
  "project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
  "finding": {},
  "resolved_on_default_branch": boolean,
  "project_default_branch": string,
  "author_id": integer,
  "resolved_by_id": integer,
  "dismissed_by_id": integer,
  "confirmed_by_id": integer,
  "created_at": string,
  "updated_at": string,
  "resolved_at": string,
  "dismissed_at": string,
  "confirmed_at": string,
  "last_edited_at": string,
  "start_date": string,
  "updated_by_id": integer,
  "last_edited_by_id": integer,
  "due_date": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

