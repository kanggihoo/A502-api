# 22-Search for a Conan package [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/conans/search`

Searches the instance for a specified Conan package.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `q` | `string` | `query` | Yes | Search query |
| `ignorecase` | `boolean` | `query` | No | Ignore case when searching (case-insensitive search) |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

