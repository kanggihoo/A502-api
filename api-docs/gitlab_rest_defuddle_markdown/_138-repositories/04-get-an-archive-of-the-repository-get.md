# 04-Get an archive of the repository [GET]

`GET /api/v4/projects/{id}/repository/archive`

Get an archive of the repository

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `query` | No | The commit sha of the archive to be downloaded |
| `ref_type` | `string` | `query` | No | Type of ref in sha, heads (branch) or tags (tag) |
| `format` | `string` | `query` | No | The archive format |
| `path` | `string` | `query` | No | Subfolder of the repository to be downloaded |
| `include_lfs_blobs` | `boolean` | `query` | No | Used to exclude LFS objects from archive |
| `exclude_paths` | `array` | `query` | No | Comma-separated list of paths to exclude from the archive |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

