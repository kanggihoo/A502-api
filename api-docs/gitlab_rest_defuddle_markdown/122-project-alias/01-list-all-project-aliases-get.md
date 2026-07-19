# 01-List all project aliases [GET]

`GET /api/v4/project_aliases`

Lists all project aliases for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "name": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

