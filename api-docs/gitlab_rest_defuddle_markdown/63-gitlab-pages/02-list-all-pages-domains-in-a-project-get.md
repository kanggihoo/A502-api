# 02-List all Pages domains in a project [GET]

`GET /api/v4/projects/{id}/pages/domains`

Lists all Pages domains in a specified project. You must have permissions to view Pages domains.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

