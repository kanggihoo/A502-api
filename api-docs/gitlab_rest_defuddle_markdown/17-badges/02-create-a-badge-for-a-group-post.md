# 02-Create a badge for a group [POST]

`POST /api/v4/groups/{id}/badges`

Creates a badge for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user. |

### Request Body (application/json)

```json
{
  "link_url": string (required), // URL of the badge link
  "image_url": string (required), // URL of the badge image
  "name": string, // Name for the badge
}
```
### Responses

#### 201 - Created

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

