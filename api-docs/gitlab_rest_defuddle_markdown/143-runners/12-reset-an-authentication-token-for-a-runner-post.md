# 12-Reset an authentication token for a runner [POST]

`POST /api/v4/runners/{id}/reset_authentication_token`

Resets the authentication token for a specified runner.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the runner |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "token": string,
  "token_expires_at": string,
}
```

#### 400 - Bad Request

#### 403 - No access granted

#### 404 - Runner not found

#### 422 - Unprocessable Entity

