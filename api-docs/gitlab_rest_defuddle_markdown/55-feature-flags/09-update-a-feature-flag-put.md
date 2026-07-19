# 09-Update a feature flag [PUT]

`PUT /api/v4/projects/{id}/feature_flags/{feature_flag_name}`

Updates a specified feature flag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `feature_flag_name` | `string` | `path` | Yes | The name of the feature flag |

### Request Body (application/json)

```json
{
  "name": string, // The new name of the feature flag. Supported in GitLab 13.3 and later
  "description": string, // The description of the feature flag
  "active": boolean, // The active state of the flag. Supported in GitLab 13.3 and later
  "strategies": [
    {
      "id": integer, // The feature flag strategy ID
      "name": string, // The strategy name
      "parameters": {}, // The strategy parameters as a JSON-formatted string e.g. `{"userIds":"user1"}`
      "user_list_id": integer, // The ID of the feature flag user list
      "_destroy": boolean, // Delete the strategy when true
      "scopes": [
        {
          "id": integer, // The scope id
          "environment_scope": string, // The environment scope of the scope
          "_destroy": boolean, // Delete the scope when true
        }
      ], // Array of scopes for the strategy
    }
  ], // Array of feature flag strategies
}
```
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

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

