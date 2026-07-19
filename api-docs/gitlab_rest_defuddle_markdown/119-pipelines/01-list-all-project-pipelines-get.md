# 01-List all project pipelines [GET]

`GET /api/v4/projects/{id}/pipelines`

Lists all pipelines in a project. By default, child pipelines are not included in the results. To return child pipelines, set `source` to `parent_pipeline`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID or URL-encoded path |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `scope` | `string` | `query` | No | The scope of pipelines |
| `status` | `string` | `query` | No | The status of pipelines |
| `ref` | `string` | `query` | No | The ref of pipelines |
| `sha` | `string` | `query` | No | The sha of pipelines |
| `yaml_errors` | `boolean` | `query` | No | Returns pipelines with invalid configurations |
| `username` | `string` | `query` | No | The username of the user who triggered pipelines |
| `updated_before` | `string` | `query` | No | Return pipelines updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return pipelines updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `created_before` | `string` | `query` | No | Return pipelines created before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `created_after` | `string` | `query` | No | Return pipelines created after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `order_by` | `string` | `query` | No | Order pipelines |
| `sort` | `string` | `query` | No | Sort pipelines |
| `source` | `string` | `query` | No | The source of pipelines |
| `name` | `string` | `query` | No | Filter pipelines by name |

### Responses

#### 200 - OK

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
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

