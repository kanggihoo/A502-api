# 01-Update group security settings [PUT]

`PUT /api/v4/groups/{id}/security_settings`

Updates group security settings for a specified group. You must have the Security Manager, Maintainer, or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "secret_push_protection_enabled": boolean (required), // Whether to enable the feature
  "projects_to_exclude": [
    integer
  ], // IDs of projects to exclude from the feature
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

