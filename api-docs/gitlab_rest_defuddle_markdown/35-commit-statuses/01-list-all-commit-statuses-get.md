# 01-List all commit statuses [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/statuses`

Lists all commit statuses for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project. |
| `sha` | `string` | `path` | Yes | Hash of the commit. |
| `ref` | `string` | `query` | No | Name of the branch or tag. Default is the default branch. |
| `stage` | `string` | `query` | No | Filter statuses by build stage. |
| `name` | `string` | `query` | No | Filter statuses by job name. |
| `pipeline_id` | `integer` | `query` | No | Filter statuses by pipeline ID. |
| `all` | `boolean` | `query` | No | Include all statuses instead of latest only. Default is `false`. |
| `order_by` | `string` | `query` | No | Values for sorting statuses. Valid values are `id` and `pipeline_id`. Default is `id`. |
| `sort` | `string` | `query` | No | Sort statuses in ascending or descending order. Valid values are `asc` and `desc`. Default is `asc`. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

