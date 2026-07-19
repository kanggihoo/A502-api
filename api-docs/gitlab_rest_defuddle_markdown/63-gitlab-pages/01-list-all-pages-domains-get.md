# 01-List all Pages domains [GET]

`GET /api/v4/pages/domains`

Lists all Pages domains on the instance. You must have administrator access to the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `domain` | `string` | `query` | No | The domain of the GitLab Pages site to filter on. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "domain": string,
  "url": string,
  "project_id": string,
  "verified": string,
  "verification_code": string,
  "enabled_until": string,
  "auto_ssl_enabled": string,
  "certificate_expiration": {
    "expired": string,
    "expiration": string,
  },
}
```

#### 400 - Bad Request

