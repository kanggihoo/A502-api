# 18-Create a system hook [POST]

`POST /api/v4/hooks`

Creates a system hook.

### Request Body (application/json)

```json
{
  "url": string (required), // The URL to send the request to
  "name": string, // Name of the hook
  "description": string, // Description of the hook
  "token": string, // Secret token to validate received payloads; this isn't returned in the response
  "signing_token": string, // HMAC signing token used to compute the webhook-signature header. Must be in whsec_<base64> format encoding a 32-byte key. Not returned in the response
  "push_events": boolean, // When true, the hook fires on push events
  "tag_push_events": boolean, // When true, the hook fires on new tags being pushed
  "merge_requests_events": boolean, // Trigger hook on merge requests events
  "repository_update_events": boolean, // Trigger hook on repository update events
  "enable_ssl_verification": boolean, // Do SSL verification when triggering the hook
  "push_events_branch_filter": string, // Trigger hook on specified branch only
  "branch_filter_strategy": enum("wildcard" | "regex" | "all_branches"), // Filter push events by branch. Possible values are `wildcard` (default), `regex`, and `all_branches`
  "custom_webhook_template": string, // Custom template for the request payload
  "url_variables": [
    {
      "key": string (required), // Name of the variable
      "value": string (required), // Value of the variable
    }
  ], // URL variables for interpolation
  "custom_headers": [
    {
      "key": string (required), // Name of the header
      "value": string (required), // Value of the header
    }
  ], // Custom headers
}
```
### Responses

#### 201 - Created

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

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

