# 01-List all release links [GET]

`GET /api/v4/projects/{id}/releases/{tag_name}/assets/links`

Lists all assets as links from a release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The tag associated with the release |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

