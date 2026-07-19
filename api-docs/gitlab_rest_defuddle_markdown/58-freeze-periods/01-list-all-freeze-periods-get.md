# 01-List all freeze periods [GET]

`GET /api/v4/projects/{id}/freeze_periods`

Lists all freeze periods for a specified project.

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
  "freeze_start": string,
  "freeze_end": string,
  "cron_timezone": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

