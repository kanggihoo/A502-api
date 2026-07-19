# 04-Retrieve a badge for a group [GET]

`GET /api/v4/groups/{id}/badges/{badge_id}`

Retrieves a specified badge for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user. |
| `badge_id` | `integer` | `path` | Yes | The badge ID |

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

