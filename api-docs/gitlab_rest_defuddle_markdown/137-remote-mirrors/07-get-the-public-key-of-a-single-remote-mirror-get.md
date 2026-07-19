# 07-Get the public key of a single remote mirror [GET]

`GET /api/v4/projects/{id}/remote_mirrors/{mirror_id}/public_key`

Get the public key of a single remote mirror

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `mirror_id` | `string` | `path` | Yes | The ID of a remote mirror |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

