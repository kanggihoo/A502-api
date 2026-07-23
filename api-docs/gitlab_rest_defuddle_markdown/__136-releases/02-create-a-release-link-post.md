# 02-Create a release link [POST]

`POST /api/v4/projects/{id}/releases/{tag_name}/assets/links`

Creates an asset link for a specified release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The tag associated with the release |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the link. Link names must be unique in the release
  "url": string (required), // The URL of the link. Link URLs must be unique in the release.
  "direct_asset_path": string, // Optional path for a direct asset link
  "filepath": string, // Deprecated: optional path for a direct asset link
  "link_type": enum("other" | "runbook" | "image" | "package"), // The type of the link: `other`, `runbook`, `image`, or `package`. Defaults to `other`
}
```
### Responses

#### 201 - Created

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

