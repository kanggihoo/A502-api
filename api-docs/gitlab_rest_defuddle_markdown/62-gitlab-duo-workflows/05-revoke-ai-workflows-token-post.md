# 05-Revoke ai_workflows token [POST]

`POST /api/v4/ai/duo_workflows/revoke_token`

Revoke ai_workflows token

### Request Body (application/json)

```json
{
  "token": string (required), // The access token to revoke
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

