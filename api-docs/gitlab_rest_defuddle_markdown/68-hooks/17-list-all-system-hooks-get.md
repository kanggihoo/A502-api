# 17-List all system hooks [GET]

`GET /api/v4/hooks`

Lists all system hooks for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "url": string,
  "name": string,
  "description": string,
  "created_at": string,
  "push_events": boolean,
  "tag_push_events": boolean,
  "merge_requests_events": boolean,
  "repository_update_events": boolean,
  "enable_ssl_verification": boolean,
  "organization_id": integer,
  "alert_status": string,
  "disabled_until": string,
  "url_variables": [
    {}
  ],
  "push_events_branch_filter": string,
  "branch_filter_strategy": string,
  "custom_webhook_template": string,
  "custom_headers": [
    {}
  ],
  "token_present": boolean, // Whether a secret token is configured
  "signing_token_present": boolean, // Whether an HMAC signing token is configured
}
```

#### 400 - Bad Request

