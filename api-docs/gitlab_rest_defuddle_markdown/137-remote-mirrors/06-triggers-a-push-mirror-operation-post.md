# 06-Triggers a push mirror operation [POST]

`POST /api/v4/projects/{id}/remote_mirrors/{mirror_id}/sync`

Triggers a push mirror operation

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `mirror_id` | `string` | `path` | Yes | The ID of a remote mirror |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

