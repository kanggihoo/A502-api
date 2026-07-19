# 01-Render Markdown content [POST]

`POST /api/v4/markdown`

Renders Markdown content as HTML.

### Request Body (application/json)

```json
{
  "text": string (required), // The Markdown text to render
  "gfm": boolean, // Render text using GitLab Flavored Markdown. Default is false
  "project": string, // Use project as a context when creating references using GitLab Flavored Markdown
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "html": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

