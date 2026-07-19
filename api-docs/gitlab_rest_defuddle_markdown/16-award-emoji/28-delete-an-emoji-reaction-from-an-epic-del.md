# 28-Delete an emoji reaction from an epic [DEL]

`DELETE /api/v4/groups/{id}/epics/{epic_iid}/award_emoji/{award_id}`

Deletes a specified emoji reaction from an epic. Only an administrator or the user who added the reaction can delete it.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of an emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of a group epic |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

