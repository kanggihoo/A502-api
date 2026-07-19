# 27-List all webhooks for a project [GET]

`GET /api/v4/projects/{id}/hooks`

Lists all webhooks for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
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

#### 400 - Bad Request

#### 404 - Not Found

