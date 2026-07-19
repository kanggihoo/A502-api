# 21-Verify authentication credentials [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/users/check_credentials`

Verifies authentication credentials for a Conan package registry.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

