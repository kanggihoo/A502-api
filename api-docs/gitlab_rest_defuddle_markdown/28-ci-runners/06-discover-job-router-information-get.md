# 06-Discover Job Router information [GET]

`GET /api/v4/runners/router/discovery`

Discovers Job Router information for a runner. You must provide a valid runner authentication token.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "server_url": string,
}
```

#### 403 - 403 Forbidden

#### 501 - 501 Not Implemented

