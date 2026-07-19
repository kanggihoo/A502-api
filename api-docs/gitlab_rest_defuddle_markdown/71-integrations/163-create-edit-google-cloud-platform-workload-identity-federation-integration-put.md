# 163-Create/Edit Google Cloud Platform Workload Identity Federation integration [PUT]

`PUT /api/v4/groups/{id}/integrations/google-cloud-platform-workload-identity-federation`

Set Google Cloud Platform Workload Identity Federation integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "workload_identity_federation_project_id": string (required), // Google Cloud project ID for the Workload Identity Federation.
  "workload_identity_federation_project_number": string (required), // Google Cloud project number for the Workload Identity Federation.
  "workload_identity_pool_id": string (required), // ID of the Workload Identity Pool.
  "workload_identity_pool_provider_id": string (required), // ID of the Workload Identity Pool provider.
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

