# 28-Add a webhook to a project [POST]

`POST /api/v4/projects/{id}/hooks`

Adds a webhook to a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "url": string (required), // The URL to send the request to
  "name": string, // Name of the hook
  "description": string, // Description of the hook
  "push_events": boolean, // Trigger hook on push events
  "issues_events": boolean, // Trigger hook on issues events
  "confidential_issues_events": boolean, // Trigger hook on confidential issues events
  "merge_requests_events": boolean, // Trigger hook on merge request events
  "tag_push_events": boolean, // Trigger hook on tag push events
  "note_events": boolean, // Trigger hook on note (comment) events
  "confidential_note_events": boolean, // Trigger hook on confidential note (comment) events
  "job_events": boolean, // Trigger hook on job events
  "pipeline_events": boolean, // Trigger hook on pipeline events
  "wiki_page_events": boolean, // Trigger hook on wiki events
  "deployment_events": boolean, // Trigger hook on deployment events
  "feature_flag_events": boolean, // Trigger hook on feature flag events
  "releases_events": boolean, // Trigger hook on release events
  "milestone_events": boolean, // Trigger hook on milestone events
  "emoji_events": boolean, // Trigger hook on emoji events
  "resource_access_token_events": boolean, // Trigger hook on project access token expiry events
  "resource_deploy_token_events": boolean, // Trigger hook on deploy token expiry events
  "enable_ssl_verification": boolean, // Do SSL verification when triggering the hook
  "token": string, // Secret token to validate received payloads; this will not be returned in the response
  "signing_token": string, // HMAC signing token used to compute the webhook-signature header. Must be in whsec_<base64> format encoding a 32-byte key. Not returned in the response
  "push_events_branch_filter": string, // Trigger hook on specified branch only
  "custom_webhook_template": string, // Custom template for the request payload
  "branch_filter_strategy": enum("wildcard" | "regex" | "all_branches"), // Filter push events by branch. Possible values are `wildcard` (default), `regex`, and `all_branches`
  "vulnerability_events": boolean, // Trigger hook on vulnerability events
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
  "project_id": integer,
  "issues_events": boolean,
  "confidential_issues_events": boolean,
  "note_events": boolean,
  "confidential_note_events": boolean,
  "pipeline_events": boolean,
  "wiki_page_events": boolean,
  "deployment_events": boolean,
  "feature_flag_events": boolean,
  "job_events": boolean,
  "releases_events": boolean,
  "milestone_events": boolean,
  "emoji_events": boolean,
  "resource_access_token_events": boolean,
  "resource_deploy_token_events": boolean,
  "vulnerability_events": boolean,
}
```

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

