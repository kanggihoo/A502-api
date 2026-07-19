# 80-Create/Edit Jenkins integration [PUT]

`PUT /api/v4/projects/{id}/integrations/jenkins`

Set Jenkins integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "enable_ssl_verification": boolean, // Enable SSL verification. Defaults to `true` (enabled).
  "jenkins_url": string (required), // URL of the Jenkins server.
  "project_name": string (required), // Name of the Jenkins project.
  "username": string, // Username of the Jenkins server.
  "password": string, // Password of the Jenkins server.
  "push_events": boolean, // Trigger event for pushes to the repository.
  "merge_requests_events": boolean, // Trigger event when a merge request is created, updated, or merged.
  "tag_push_events": boolean, // Trigger event for new tags pushed to the repository.
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

