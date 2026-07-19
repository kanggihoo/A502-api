# 04-Delete an application [DEL]

`DELETE /api/v4/user/applications/{id}`

Deletes a specified application owned by the authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the application. Differs from the `application_id`. |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

