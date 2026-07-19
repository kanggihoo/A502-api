# 02-Create a group hook [POST]

`POST /api/v4/groups/{id}/hooks`

Creates a hook for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "url": string (required), // The URL to send the request to
  "name": string, // Name of the hook
  "description": string, // Description of the hook
  "push_events": boolean, // Trigger hook on push events
  "push_events_branch_filter": string, // Respond to push events only on branches that match this filter
  "issues_events": boolean, // Trigger hook on issues events
  "confidential_issues_events": boolean, // Trigger hook on confidential issues events
  "merge_requests_events": boolean, // Trigger hook on merge request events
  "tag_push_events": boolean, // Trigger hook on tag push events
  "note_events": boolean, // Trigger hook on note(comment) events
  "confidential_note_events": boolean, // Trigger hook on confidential note(comment) events
  "job_events": boolean, // Trigger hook on job events
  "pipeline_events": boolean, // Trigger hook on pipeline events
  "project_events": boolean, // Trigger hook on project events
  "wiki_page_events": boolean, // Trigger hook on wiki events
  "deployment_events": boolean, // Trigger hook on deployment events
  "feature_flag_events": boolean, // Trigger hook on feature flag events
  "releases_events": boolean, // Trigger hook on release events
  "milestone_events": boolean, // Trigger hook on milestone events
  "subgroup_events": boolean, // Trigger hook on subgroup events
  "emoji_events": boolean, // Trigger hook on emoji events
  "resource_access_token_events": boolean, // Trigger hook on group access token expiry events
  "member_events": boolean, // Trigger hook on member events
  "vulnerability_events": boolean, // Trigger hook on vulnerability events
  "enable_ssl_verification": boolean, // Do SSL verification when triggering the hook
  "token": string, // Secret token to validate received payloads; this will not be returned in the response
  "signing_token": string, // HMAC signing token used to compute the webhook-signature header. Must be in whsec_<base64> format encoding a 32-byte key. Not returned in the response
  "custom_webhook_template": string, // Custom template for the request payload
  "branch_filter_strategy": enum("wildcard" | "regex" | "all_branches"), // Filter push events by branch. Possible values are `wildcard` (default), `regex`, and `all_branches`
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
  "group_id": integer,
  "issues_events": boolean,
  "confidential_issues_events": boolean,
  "note_events": boolean,
  "confidential_note_events": boolean,
  "pipeline_events": boolean,
  "wiki_page_events": boolean,
  "job_events": boolean,
  "deployment_events": boolean,
  "feature_flag_events": boolean,
  "releases_events": boolean,
  "milestone_events": boolean,
  "subgroup_events": boolean,
  "emoji_events": boolean,
  "resource_access_token_events": boolean,
  "member_events": boolean,
  "vulnerability_events": boolean,
  "project_events": boolean,
}
```

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

