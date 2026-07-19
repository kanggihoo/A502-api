# 06-Rotate a group or project access token for a group [POST]

`POST /api/v4/groups/{id}/manage/resource_access_tokens/{prat_id}/rotate`

Rotates a specified group or project access token associated with a top-level group. This revokes the previous token and creates a new token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `prat_id` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "expires_at": string, // The expiration date of the token
}
```
### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

