# 09-Retrieve a wiki page for a project [GET]

`GET /api/v4/projects/{id}/wikis/{slug}`

Retrieves a specified wiki page for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `slug` | `string` | `path` | Yes | The slug of a wiki page |
| `version` | `string` | `query` | No | The version hash of a wiki page |
| `render_html` | `boolean` | `query` | No | Render content to HTML |
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
  "content": string,
  "encoding": string,
  "front_matter": {},
}
```

#### 400 - Bad Request

#### 404 - Not found

