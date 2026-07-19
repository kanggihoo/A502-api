# 07-Verify Pages domain [PUT]

`PUT /api/v4/projects/{id}/pages/domains/{domain}/verify`

Verifies a specified Pages domain in a project. You must have permissions to update Pages domains.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `domain` | `string` | `path` | Yes | The domain to verify |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "domain": string,
  "url": string,
  "verified": string,
  "verification_code": string,
  "enabled_until": string,
  "auto_ssl_enabled": string,
  "certificate": {
    "subject": string,
    "expired": string,
    "certificate": string,
    "certificate_text": string,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

