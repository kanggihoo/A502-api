# 10-Delete a feature flag [DEL]

`DELETE /api/v4/projects/{id}/feature_flags/{feature_flag_name}`

Deletes a specified feature flag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `feature_flag_name` | `string` | `path` | Yes | The name of the feature flag |

### Responses

#### 204 - No Content

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

#### 403 - Forbidden

#### 404 - Not found

