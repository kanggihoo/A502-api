# 04-Delete the push rules of a group [DEL]

`DELETE /api/v4/groups/{id}/push_rule`

Deletes all the push rules of a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |

### Responses

#### 204 - No Content

#### 400 - Validation error

#### 404 - Not found

