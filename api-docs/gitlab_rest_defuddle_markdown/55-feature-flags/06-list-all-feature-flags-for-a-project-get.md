# 06-List all feature flags for a project [GET]

`GET /api/v4/projects/{id}/feature_flags`

Lists all feature flags of the requested project. Use the `page` and `per_page` pagination parameters to control the pagination of results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `scope` | `string` | `query` | No | The scope of feature flags, one of: `enabled`, `disabled` |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "description": string,
  "active": boolean,
  "version": string,
  "created_at": string,
  "updated_at": string,
  "scopes": [
    any
  ],
  "strategies": {
    "id": integer,
    "name": string,
    "parameters": string,
    "scopes": {
      "id": integer,
      "environment_scope": string,
    },
    "user_list": {
      "id": integer,
      "iid": integer,
      "name": string,
      "user_xids": string,
    },
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

