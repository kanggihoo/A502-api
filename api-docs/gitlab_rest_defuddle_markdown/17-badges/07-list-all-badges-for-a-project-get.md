# 07-List all badges for a project [GET]

`GET /api/v4/projects/{id}/badges`

Lists all badges for a specified project, including group badges.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `name` | `string` | `query` | No | Name for the badge |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "link_url": string,
  "image_url": string,
  "rendered_link_url": string,
  "rendered_image_url": string,
  "id": integer,
  "kind": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

