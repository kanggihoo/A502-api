# 03-Retrieve an advanced search migration [GET]

`GET /api/v4/admin/search/migrations/{migration_id}`

Retrieves a specified advanced search migration by migration version or name.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `migration_id` | `any` | `path` | Yes | The version or name of the search migration |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "version": integer,
  "name": string,
  "started_at": string,
  "completed_at": string,
  "completed": boolean,
  "obsolete": boolean,
  "migration_state": {},
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

