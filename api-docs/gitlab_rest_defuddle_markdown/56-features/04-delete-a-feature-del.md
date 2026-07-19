# 04-Delete a feature [DEL]

`DELETE /api/v4/features/{name}`

Deletes a feature gate. Returns the same response if the feature gate does not exist.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `any` | `path` | Yes |  |

### Responses

#### 204 - Resource deleted

#### 404 - Not Found

