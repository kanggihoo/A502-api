# 02-Transfer purchased compute minutes packs to another namespace [PATCH]

`PATCH /api/v4/namespaces/{id}/minutes/move/{target_id}`

Deprecated in GitLab 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the namespace to transfer from |
| `target_id` | `string` | `path` | Yes | The ID of the namespace for the packs to transfer to |

### Responses

#### 202 - Accepted

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

