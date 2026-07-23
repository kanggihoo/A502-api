# 69-Create/Edit Datadog integration [PUT]

`PUT /api/v4/projects/{id}/integrations/datadog`

Set Datadog integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "datadog_site": string, // Datadog site to send data to. Learn more about Datadog sites in the <a target="_blank" rel="noopener noreferrer" href="https://docs.datadoghq.com/getting_started/site/">documentation</a>.
  "api_url": string, // Full URL of your Datadog site. Only required if you do not use a standard Datadog site.
  "api_key": string (required), // <a target="_blank" rel="noopener noreferrer" href="https://docs.datadoghq.com/account_management/api-app-keys/">API key</a> used for authentication with Datadog.
  "datadog_ci_visibility": boolean, // Enable CI Visibility
  "archive_trace_events": boolean, // When enabled, job logs are collected by Datadog and displayed along with pipeline execution traces.
  "datadog_service": string, // Tag all pipeline data from this GitLab instance in Datadog. Can be used when managing several self-managed deployments.
  "datadog_env": string, // For self-managed deployments, `env` tag for all the data sent to Datadog.
  "datadog_tags": string, // Custom tags in Datadog. Specify one tag per line in the format `key:value\nkey2:value2`.
  "pipeline_events": boolean, // Trigger event when a pipeline status changes.
  "build_events": boolean, // Trigger event when a build is created.
  "push_events": boolean, // Trigger event for pushes to the repository.
  "merge_requests_events": boolean, // Trigger event when a merge request is created, updated, or merged.
  "note_events": boolean, // Trigger event for new comments.
  "tag_push_events": boolean, // Trigger event for new tags pushed to the repository.
  "subgroup_events": boolean,
  "project_events": boolean,
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

