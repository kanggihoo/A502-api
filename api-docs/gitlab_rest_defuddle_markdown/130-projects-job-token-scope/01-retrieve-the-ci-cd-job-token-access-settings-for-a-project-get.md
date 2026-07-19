# 01-Retrieve the CI/CD job token access settings for a project [GET]

`GET /api/v4/projects/{id}/job_token_scope`

Retrieves the CI/CD job token access settings (job token scope) of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "inbound_enabled": boolean,
  "outbound_enabled": boolean,
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

