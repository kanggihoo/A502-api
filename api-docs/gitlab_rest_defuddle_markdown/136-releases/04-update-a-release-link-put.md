# 04-Update a release link [PUT]

`PUT /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`

Updates a specified asset link for a release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The tag associated with the release |
| `link_id` | `integer` | `path` | Yes | The ID of the link |

### Request Body (application/json)

```json
{
  "name": string, // The name of the link
  "url": string, // The URL of the link
  "direct_asset_path": string, // Optional path for a direct asset link
  "filepath": string, // Deprecated: optional path for a direct asset link
  "link_type": enum("other" | "runbook" | "image" | "package"), // The type of the link: `other`, `runbook`, `image`, or `package`. Defaults to `other`
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

