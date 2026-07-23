# 20-Reject access to a user [POST]

`POST /api/v4/users/{id}/reject`

Rejects access to a specified user account that is pending approval. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

