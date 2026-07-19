# 05-Update Pages domain [PUT]

`PUT /api/v4/projects/{id}/pages/domains/{domain}`

Updates a specified Pages domain in a project. You must have permissions to change an existing Pages domain.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `domain` | `string` | `path` | Yes | The domain |

### Request Body (application/json)

```json
{
  "certificate": any,
  "key": any,
  "auto_ssl_enabled": boolean, // Enables automatic generation of SSL certificates issued by Let's Encrypt for custom domains.
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

