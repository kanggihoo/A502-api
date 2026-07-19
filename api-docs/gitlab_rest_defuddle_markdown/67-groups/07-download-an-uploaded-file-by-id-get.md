# 07-Download an uploaded file by ID [GET]

`GET /api/v4/groups/{id}/uploads/{upload_id}`

Downloads an uploaded file with a specified ID. You must have the Maintainer or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `integer` | `path` | Yes | The ID of a group upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

