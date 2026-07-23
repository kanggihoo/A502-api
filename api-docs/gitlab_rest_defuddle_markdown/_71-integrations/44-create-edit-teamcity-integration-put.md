# 44-Create/Edit Teamcity integration [PUT]

`PUT /api/v4/projects/{id}/services/teamcity`

Set Teamcity integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "enable_ssl_verification": boolean, // Enable SSL verification. Defaults to `true` (enabled).
  "teamcity_url": string (required), // TeamCity root URL (for example, `https://teamcity.example.com`).
  "build_type": string (required), // The build configuration ID of the TeamCity project.
  "username": string (required), // A user with permissions to trigger a manual build.
  "password": string (required), // The password of the user.
  "push_events": boolean, // Trigger event for pushes to the repository.
  "merge_requests_events": boolean, // Trigger event when a merge request is created, updated, or merged.
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

