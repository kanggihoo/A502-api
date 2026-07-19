# 03-Retrieve a release link [GET]

`GET /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`

Retrieves a specified asset as a link from a release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The tag associated with the release |
| `link_id` | `integer` | `path` | Yes | The ID of the link |

### Responses

#### 200 - OK

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

