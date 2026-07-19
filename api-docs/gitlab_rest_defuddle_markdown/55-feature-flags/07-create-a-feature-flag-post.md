# 07-Create a feature flag [POST]

`POST /api/v4/projects/{id}/feature_flags`

Creates a feature flag for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the feature flag
  "description": string, // The description of the feature flag
  "active": boolean, // The active state of the flag. Defaults to `true`. Supported in GitLab 13.3 and later
  "strategies": [
    {
      "name": string (required), // The strategy name. Can be `default`, `gradualRolloutUserId`, `userWithId`, or `gitlabUserList`. In GitLab 13.5 and later, can be `flexibleRollout`
      "parameters": {}, // The strategy parameters as a JSON-formatted string e.g. `{"userIds":"user1"}`
      "user_list_id": integer, // The ID of the feature flag user list. If strategy is `gitlabUserList`.
      "scopes": [
        {
          "environment_scope": string (required), // The environment scope of the scope
        }
      ], // Array of scopes for the strategy
    }
  ], // Array of feature flag strategies
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

