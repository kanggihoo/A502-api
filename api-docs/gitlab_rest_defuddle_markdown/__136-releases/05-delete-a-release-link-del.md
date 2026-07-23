# 05-Delete a release link [DEL]

`DELETE /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`

Deletes a specified asset link from a release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The tag associated with the release |
| `link_id` | `integer` | `path` | Yes | The ID of the link |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "url": string,
  "direct_asset_url": string,
  "link_type": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

