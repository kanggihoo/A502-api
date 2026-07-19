# 02-Update project security settings [PUT]

`PUT /api/v4/projects/{id}/security_settings`

Updates project security settings for a specified project. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "secret_push_protection_enabled": boolean, // Enable/disable secret push protection
  "pre_receive_secret_detection_enabled": boolean, // Enable/disable secret push protection
  "fast_dependency_paths_enabled": boolean, // Enable fast mode for dependency path graph builds. When enabled, records one path per dependency instead of all possible paths, reducing memory and processing time for large dependency graphs. Requires the dependency_paths feature flag to be enabled.
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

