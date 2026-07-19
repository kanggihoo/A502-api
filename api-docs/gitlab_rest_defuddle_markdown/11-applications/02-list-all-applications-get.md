# 02-List all applications [GET]

`GET /api/v4/user/applications`

Lists all applications owned by the authenticated user.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "application_id": string,
  "application_name": string,
  "callback_url": string,
  "confidential": boolean,
  "scopes": [
    any
  ],
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

