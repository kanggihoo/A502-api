# 04-Verify authentication for a registered runner [POST]

`POST /api/v4/runners/verify`

Verifies authentication for a registered runner.

### Request Body (application/json)

```json
{
  "token": string (required), // The runner's authentication token
  "system_id": string, // The runner's system identifier
}
```
### Responses

#### 200 - Credentials are valid

Schema (application/json):
```json
{
  "id": string,
  "token": string,
  "token_expires_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 422 - Runner is orphaned

