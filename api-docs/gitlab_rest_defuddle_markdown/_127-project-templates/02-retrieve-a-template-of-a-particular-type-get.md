# 02-Retrieve a template of a particular type [GET]

`GET /api/v4/projects/{id}/templates/{type}/{name}`

Retrieves a template of a specified type for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `type` | `string` | `path` | Yes | The type (dockerfiles|gitignores|gitlab_ci_ymls|licenses|issues|merge_requests) of the template |
| `name` | `string` | `path` | Yes | The key of the template, as obtained from the collection endpoint. |
| `source_template_project_id` | `integer` | `query` | No | The project id where a given template is being stored. This is useful when multiple templates from different projects have the same name |
| `project` | `string` | `query` | No | The project name to use when expanding placeholders in the template. Only affects licenses |
| `fullname` | `string` | `query` | No | The full name of the copyright holder to use when expanding placeholders in the template. Only affects licenses |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "name": string,
  "nickname": string,
  "html_url": string,
  "source_url": string,
  "popular": boolean,
  "description": string,
  "conditions": [
    string
  ],
  "permissions": [
    string
  ],
  "limitations": [
    string
  ],
  "content": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

