# 79-Create/Edit Irker integration [PUT]

`PUT /api/v4/projects/{id}/integrations/irker`

Set Irker integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "server_host": string, // irker daemon hostname. The default value is `localhost`.
  "server_port": integer, // irker daemon port. The default value is `6659`.
  "default_irc_uri": string, // URI to add before each recipient. The default value is `irc://irc.network.net:6697/`.
  "recipients": string (required), // Comma-separated list of channels or email addresses.
  "colorize_messages": boolean, // Colorize messages
  "push_events": boolean, // Trigger event for pushes to the repository.
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

