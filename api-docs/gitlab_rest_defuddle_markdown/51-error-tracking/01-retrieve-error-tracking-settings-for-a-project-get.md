# 01-Retrieve Error Tracking settings for a project [GET]

`GET /api/v4/projects/{id}/error_tracking/settings`

Retrieves the Error Tracking settings for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "active": boolean,
  "project_name": string,
  "sentry_external_url": string,
  "api_url": string,
  "integrated": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

