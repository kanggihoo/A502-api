# 82-Create/Edit Jira Cloud App integration [PUT]

`PUT /api/v4/projects/{id}/integrations/jira-cloud-app`

Set Jira Cloud App integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "jira_cloud_app_service_ids": string, // Copy and paste your JSM Service ID here. Use comma (,) to separate multiple IDs.
  "jira_cloud_app_enable_deployment_gating": boolean, // Enable to approve or reject blocked GitLab deployments from Jira Service Management.
  "jira_cloud_app_deployment_gating_environments": string, // Enter the environment (production,staging,testing,development) where you want to enable deployment gating. Use comma (,) to separate multiple environments.
  "use_inherited_settings": boolean, // Indicates whether to inherit the default settings. Defaults to `false`.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "slug": string,
  "created_at": string,
  "updated_at": string,
  "active": boolean,
  "commit_events": boolean,
  "push_events": boolean,
  "issues_events": boolean,
  "incident_events": boolean,
  "alert_events": boolean,
  "confidential_issues_events": boolean,
  "merge_requests_events": boolean,
  "tag_push_events": boolean,
  "deployment_events": boolean,
  "note_events": boolean,
  "confidential_note_events": boolean,
  "pipeline_events": boolean,
  "wiki_page_events": boolean,
  "job_events": boolean,
  "comment_on_event_enabled": boolean,
  "inherited": boolean,
  "vulnerability_events": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

#### 422 - Unprocessable entity

