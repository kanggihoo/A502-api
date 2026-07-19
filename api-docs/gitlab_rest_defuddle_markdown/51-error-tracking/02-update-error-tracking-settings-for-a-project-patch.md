# 02-Update Error Tracking settings for a project [PATCH]

`PATCH /api/v4/projects/{id}/error_tracking/settings`

Updates Error Tracking settings for a specified project. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "active": boolean (required), // Pass true to enable the already configured Error Tracking settings or false to disable it.
  "integrated": boolean, // Pass true to enable the integrated Error Tracking backend. Available in GitLab 14.2 and later.
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

