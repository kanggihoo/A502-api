# 03-Retrieve a project alias [GET]

`GET /api/v4/project_aliases/{name}`

Retrieves details of a specified project alias.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "name": string,
}
```

#### 403 - Forbidden

#### 404 - Not found

