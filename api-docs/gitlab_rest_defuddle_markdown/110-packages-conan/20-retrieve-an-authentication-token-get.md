# 20-Retrieve an authentication token [GET]

`GET /api/v4/projects/{id}/packages/conan/v1/users/authenticate`

Retrieves an authentication token. Creates a JSON Web Token (JWT) for use as a Bearer header in other requests to the package registry.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

