# 05-Delete an existing software license policy from a project [DEL]

`DELETE /api/v4/projects/{id}/managed_licenses/{managed_license_id}`

Delete an existing software license policy from a project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `managed_license_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

