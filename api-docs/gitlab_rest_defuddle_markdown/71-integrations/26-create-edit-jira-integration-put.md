# 26-Create/Edit Jira integration [PUT]

`PUT /api/v4/projects/{id}/services/jira`

Set Jira integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "url": string (required), // The URL to the Jira project which is being linked to this GitLab project (for example, `https://jira.example.com`).
  "api_url": string, // The base URL to the Jira instance API. Web URL value is used if not set (for example, `https://jira-api.example.com`).
  "jira_auth_type": integer, // The authentication method to use with Jira. Use `0` for basic authentication, `1` for Jira personal access token, and `2` for Jira Cloud service accounts. Defaults to `0`.
  "username": string, // The email or username to use with Jira. Use an email for Jira Cloud, and a username for Jira Data Center and Jira Server. Required when using basic authentication (`jira_auth_type` is `0`).
  "password": string (required), // The Jira API token, password, or personal access token to use with Jira. When using Basic Authentication (`jira_auth_type` is `0`), use an API token for Jira Cloud, and a password for Jira Data Center or Jira Server. For a Jira personal access token (`jira_auth_type` is `1`), use the personal access token.
  "jira_issue_regex": string, // Regular expression to match Jira issue keys.
  "jira_issue_prefix": string, // Prefix to match Jira issue keys.
  "jira_issue_transition_id": string, // The ID of one or more transitions for [custom issue transitions](../integration/jira/issues.md#custom-issue-transitions).Ignored when `jira_issue_transition_automatic` is enabled. Defaults to a blank string,which disables custom transitions.
  "issues_enabled": string, // Enable viewing Jira issues in GitLab.
  "project_keys": [
    string
  ], // Keys of Jira projects to display. When `issues_enabled` is `true`, this setting filters which Jira projects are shown in GitLab. It does not restrict the API token's access.
  "vulnerabilities_enabled": boolean, // Turn on Jira issue creation for GitLab vulnerabilities.
  "vulnerabilities_issuetype": string, // Jira issue type to use when creating issues from vulnerabilities.
  "project_key": string, // Key of the project to use when creating issues from vulnerabilities.This parameter is required if using the integration to create Jira issues from vulnerabilities.
  "customize_jira_issue_enabled": boolean, // When set to `true`, opens a prefilled form on the Jira instancewhen creating a Jira issue from a vulnerability.
  "jira_check_enabled": boolean, // Verify Jira issues referenced in commit messages exist before allowing the push.
  "jira_exists_check_enabled": boolean, // Verify the Jira issues referenced in commit messages exist in Jira.
  "jira_assignee_check_enabled": boolean, // Verify the committer is the assignee of the Jira issues referenced in commit messages.
  "jira_status_check_enabled": boolean, // Verify the status of Jira issues referenced in commit messages.
  "jira_allowed_statuses_as_string": string, // Comma-separated list of allowed Jira issue statuses.
  "comment_on_event_enabled": boolean, // Enable comments inside Jira issues on each GitLab event (commit / merge request)
  "commit_events": boolean, // Trigger event when a commit is created or updated.
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

