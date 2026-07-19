# 05-Reset a runner authentication token with the current token [POST]

`POST /api/v4/runners/reset_authentication_token`

Resets a runner authentication token with the token used to authenticate the request.

### Request Body (application/json)

```json
{
  "token": string (required), // The current authentication token of the runner
}
```
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

#### 403 - Forbidden

#### 422 - Unprocessable Entity

