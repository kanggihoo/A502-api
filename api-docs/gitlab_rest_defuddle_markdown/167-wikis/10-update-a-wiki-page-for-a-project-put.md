# 10-Update a wiki page for a project [PUT]

`PUT /api/v4/projects/{id}/wikis/{slug}`

Updates a specified wiki page for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `slug` | `string` | `path` | Yes | The slug of a wiki page |

### Request Body (application/json)

```json
{
  "title": string, // Title of a wiki page
  "front_matter": {
    "title": string, // Frontmatter title of a wiki page
  }, // Object that contains YAML frontmatter
  "content": string, // Content of a wiki page
  "format": enum("markdown" | "rdoc" | "asciidoc" | "org"), // Format of a wiki page. Available formats are markdown, rdoc, asciidoc and org
}
```
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

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

