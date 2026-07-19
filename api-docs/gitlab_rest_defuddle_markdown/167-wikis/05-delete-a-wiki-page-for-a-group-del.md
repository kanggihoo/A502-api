# 05-Delete a wiki page for a group [DEL]

`DELETE /api/v4/groups/{id}/wikis/{slug}`

Deletes a specified wiki page from a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `slug` | `string` | `path` | Yes | The slug of a wiki page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 204 - No Content

#### 400 - Validation error

#### 404 - Not found

