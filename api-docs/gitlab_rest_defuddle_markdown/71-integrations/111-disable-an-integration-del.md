# 111-Disable an integration [DEL]

`DELETE /api/v4/projects/{id}/integrations/{slug}`

Disable the integration. Integration settings are preserved.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `slug` | `string` | `path` | Yes | The name of the integration |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

