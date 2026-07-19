# 02-List all packages for a group [GET]

`GET /api/v4/group/{id}/-/packages/composer/p/{sha}`

Lists all repository packages for a specified group. Composer V2 is recommended over V1.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of a group |
| `sha` | `string` | `path` | Yes | Shasum of current json |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

