# 15-Destroy an epic [DEL]

`DELETE /api/v4/groups/{id}/(-/)epics/{epic_iid}`

Deletes an epic

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of an epic |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

