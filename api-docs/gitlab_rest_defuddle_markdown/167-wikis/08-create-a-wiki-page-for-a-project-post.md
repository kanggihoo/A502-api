# 08-Create a wiki page for a project [POST]

`POST /api/v4/projects/{id}/wikis`

Creates a wiki page for a specified project. Requests can define the title, slug, and content.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "title": string (required), // Title of a wiki page
  "front_matter": {
    "title": string, // Frontmatter title of a wiki page
  }, // Object that contains YAML frontmatter
  "content": string (required), // Content of a wiki page
  "format": enum("markdown" | "rdoc" | "asciidoc" | "org"), // Format of a wiki page. Available formats are markdown, rdoc, asciidoc and org
}
```
### Responses

#### 201 - Created

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

