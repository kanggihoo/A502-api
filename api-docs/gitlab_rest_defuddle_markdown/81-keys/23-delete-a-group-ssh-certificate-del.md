# 23-Delete a group SSH certificate [DEL]

`DELETE /api/v4/groups/{id}/ssh_certificates/{ssh_certificates_id}`

Deletes a specified group SSH certificate.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `ssh_certificates_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable entity

