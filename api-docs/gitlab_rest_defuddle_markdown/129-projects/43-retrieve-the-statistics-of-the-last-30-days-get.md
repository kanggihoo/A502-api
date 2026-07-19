# 43-Retrieve the statistics of the last 30 days [GET]

`GET /api/v4/projects/{id}/statistics`

Retrieves the clone and pull statistics for the last 30 days from a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "fetches": {},
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 Project Not Found

