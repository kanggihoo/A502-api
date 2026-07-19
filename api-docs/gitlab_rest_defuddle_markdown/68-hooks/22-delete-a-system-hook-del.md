# 22-Delete a system hook [DEL]

`DELETE /api/v4/hooks/{hook_id}`

Deletes a specified system hook. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the system hook |

### Responses

#### 204 - No Content

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

#### 404 - Not found

