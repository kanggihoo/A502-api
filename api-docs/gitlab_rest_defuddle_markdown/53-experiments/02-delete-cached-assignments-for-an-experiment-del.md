# 02-Delete cached assignments for an experiment [DEL]

`DELETE /api/v4/experiments/{name}/cache`

Removes all cached variant assignments for the experiment with the given cache key. Useful for cleaning up completed experiments whose code has been removed from the codebase.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `path` | Yes | Experiment cache key |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

