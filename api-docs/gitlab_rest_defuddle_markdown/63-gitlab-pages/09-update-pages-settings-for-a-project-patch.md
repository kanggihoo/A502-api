# 09-Update Pages settings for a project [PATCH]

`PATCH /api/v4/projects/{id}/pages`

Updates Pages settings for a specified project. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "pages_unique_domain_enabled": boolean, // Whether to use unique domain
  "pages_https_only": boolean, // Whether to force HTTPS
  "pages_primary_domain": string, // Set pages primary domain
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

