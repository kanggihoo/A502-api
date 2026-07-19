# 08-Verify namespace availability [GET]

`GET /api/v4/namespaces/{id}/exists`

Verifies that a namespace is available for use.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | Namespace’s path |
| `parent_id` | `integer` | `query` | No | The ID of the parent namespace. If no ID is specified, only top-level namespaces are considered. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "exists": boolean,
  "suggests": [
    string
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

