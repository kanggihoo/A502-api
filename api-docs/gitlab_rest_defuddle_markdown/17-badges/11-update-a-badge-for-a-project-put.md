# 11-Update a badge for a project [PUT]

`PUT /api/v4/projects/{id}/badges/{badge_id}`

Updates a specified badge for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user. |
| `badge_id` | `integer` | `path` | Yes | The badge ID |

### Request Body (application/json)

```json
{
  "link_url": string, // URL of the badge link
  "image_url": string, // URL of the badge image
  "name": string, // Name for the badge
}
```
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

