# 20-Create/Edit Gitlab Slack Application integration [PUT]

`PUT /api/v4/projects/{id}/services/gitlab-slack-application`

Set Gitlab Slack Application integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "channel": string, // Default channel to use if no other channel is configured.
  "notify_only_broken_pipelines": boolean, // Send notifications for broken pipelines.
  "notify_only_when_pipeline_status_changes": boolean, // Send notifications only when the pipeline status changes.
  "branches_to_be_notified": string, // Branches to send notifications for. Valid options are `all`, `default`, `protected`, and `default_and_protected`. The default value is `default`.
  "labels_to_be_notified": string, // Labels to send notifications for. Leave blank to receive notifications for all events.
  "labels_to_be_notified_behavior": string, // Labels to be notified for. Valid options are `match_any` and `match_all`. The default value is `match_any`.
  "push_channel": string, // The name of the channel to receive push_events notifications
  "issue_channel": string, // The name of the channel to receive issues_events notifications
  "incident_channel": string, // The name of the channel to receive incident_events notifications
  "alert_channel": string, // The name of the channel to receive alert_events notifications
  "confidential_issue_channel": string, // The name of the channel to receive confidential_issues_events notifications
  "merge_request_channel": string, // The name of the channel to receive merge_requests_events notifications
  "note_channel": string, // The name of the channel to receive note_events notifications
  "confidential_note_channel": string, // The name of the channel to receive confidential_note_events notifications
  "tag_push_channel": string, // The name of the channel to receive tag_push_events notifications
  "deployment_channel": string, // The name of the channel to receive deployment_events notifications
  "pipeline_channel": string, // The name of the channel to receive pipeline_events notifications
  "wiki_page_channel": string, // The name of the channel to receive wiki_page_events notifications
  "vulnerability_channel": string, // The name of the channel to receive vulnerability_events notifications
  "push_events": boolean, // Trigger event for pushes to the repository.
  "issues_events": boolean, // Trigger event when a work item is created, updated, or closed.
  "confidential_issues_events": boolean, // Trigger event when a confidential work item is created, updated, or closed.
  "merge_requests_events": boolean, // Trigger event when a merge request is created, updated, or merged.
  "note_events": boolean, // Trigger event for new comments.
  "confidential_note_events": boolean, // Trigger event for new comments on confidential work items.
  "tag_push_events": boolean, // Trigger event for new tags pushed to the repository.
  "pipeline_events": boolean, // Trigger event when a pipeline status changes.
  "wiki_page_events": boolean, // Trigger event when a wiki page is created or updated.
  "deployment_events": boolean, // Trigger event when a deployment starts or finishes.
  "incident_events": boolean, // Trigger event when an incident is created.
  "work_item_events": boolean,
  "confidential_work_item_events": boolean,
  "vulnerability_events": boolean,
  "alert_events": boolean, // Trigger event when a new, unique alert is recorded.
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

