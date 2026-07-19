# 06-Retrieve dependencies [GET]

`GET /api/v4/projects/{id}/packages/rubygems/api/v1/dependencies`

Retrieves a list of dependencies for specified gems. The response is a marshalled array of hashes for all versions of the requested gems. Because the response is marshalled, you can store it in a file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `gems` | `array` | `query` | No | Comma delimited gem names |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

