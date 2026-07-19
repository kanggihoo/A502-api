# 03-Get all the Zoekt nodes [GET]

`GET /api/v4/admin/zoekt/shards`

Get all the Zoekt nodes

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "index_base_url": string,
  "search_base_url": string,
}
```

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

