# 141-Create/Edit Packagist integration [PUT]

`PUT /api/v4/groups/{id}/integrations/packagist`

Set Packagist integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "username": string (required), // Username of a Packagist account.
  "token": string (required), // API token of the Packagist server.
  "server": string, // URL of the Packagist server. The default value is `https://packagist.org`.
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

