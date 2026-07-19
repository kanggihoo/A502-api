# 17-Reset the runner registration token for the instance [POST]

`POST /api/v4/runners/reset_registration_token`

Resets the runner registration token for the GitLab instance.

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

