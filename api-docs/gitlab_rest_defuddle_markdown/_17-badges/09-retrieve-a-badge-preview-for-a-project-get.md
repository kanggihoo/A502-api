# 09-Retrieve a badge preview for a project [GET]

`GET /api/v4/projects/{id}/badges/render`

Previews the final `link_url` and `image_url` for a specified project after resolving the placeholder interpolation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user. |
| `link_url` | `string` | `query` | Yes | URL of the badge link |
| `image_url` | `string` | `query` | Yes | URL of the badge image |

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
}
```

#### 400 - Bad Request

#### 404 - Not Found

