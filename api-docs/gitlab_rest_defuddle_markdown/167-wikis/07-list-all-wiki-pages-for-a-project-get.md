# 07-List all wiki pages for a project [GET]

`GET /api/v4/projects/{id}/wikis`

Lists all wiki pages for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `with_content` | `boolean` | `query` | No | Include pages' content |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "format": string,
  "slug": string,
  "title": string,
  "wiki_page_meta_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not found

