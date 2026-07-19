# 05-Removes a storage limit exclusion for a Namespace [DEL]

`DELETE /api/v4/namespaces/{id}/storage/limit_exclusion`

Removes a Namespaces::Storage::LimitExclusion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable entity

