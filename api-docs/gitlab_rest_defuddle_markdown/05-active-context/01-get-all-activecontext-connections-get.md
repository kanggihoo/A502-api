# 01-Get all ActiveContext connections [GET]

`GET /api/v4/admin/active_context/connections`

Get all ActiveContext connections

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "adapter_class": string,
  "prefix": string,
  "active": boolean,
  "created_at": string,
  "updated_at": string,
}
```

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

