# 01-List all secure files for a project [GET]

`GET /api/v4/projects/{id}/secure_files`

Lists all secure files for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the<br>        authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "checksum": string,
  "checksum_algorithm": string,
  "created_at": string,
  "expires_at": string,
  "metadata": {},
  "file_extension": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

