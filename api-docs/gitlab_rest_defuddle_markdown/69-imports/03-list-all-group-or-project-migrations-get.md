# 03-List all group or project migrations [GET]

`GET /api/v4/bulk_imports`

Lists all group or project migrations.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `sort` | `string` | `query` | No | Return GitLab Migrations sorted in created by `asc` or `desc` order. |
| `status` | `string` | `query` | No | Return GitLab Migrations with specified status |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "status": string,
  "source_type": string,
  "source_url": string,
  "created_at": string,
  "updated_at": string,
  "has_failures": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 503 - Service unavailable

