# 01-Purge the dependency proxy for a group [DEL]

`DELETE /api/v4/groups/{id}/dependency_proxy/cache`

Purges the dependency proxy for a specified group and schedules the cached manifests and blobs for deletion. This endpoint requires the Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

