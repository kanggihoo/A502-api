# 03-Create or update a feature flag [POST]

`POST /api/v4/features/{name}`

Creates or updates a feature flag value. If a feature with the given name doesn't exist yet, the operation creates one. The value can be a boolean or an integer to indicate percentage of time.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "value": any (required),
  "key": string, // `percentage_of_actors` or `percentage_of_time` (default)
  "feature_group": string, // A Feature group name
  "user": string, // A GitLab username or comma-separated multiple usernames
  "group": string, // A GitLab group's path, for example `gitlab-org`, or comma-separated multiple group paths
  "namespace": string, // A GitLab group or user namespace's path, for example `john-doe`, or comma-separated multiple namespace paths. Introduced in GitLab 15.0.
  "project": string, // A projects path, for example `gitlab-org/gitlab-foss`, or comma-separated multiple project paths
  "organization": string, // An organization ID or path, for example `1` or `default`, or comma-separated multiple organization IDs or paths
  "repository": string, // A repository path, for example `gitlab-org/gitlab-test.git`, `gitlab-org/gitlab-test.wiki.git`, `snippets/21.git`, to name a few. Use comma to separate multiple repository paths
  "runner": string, // A runner ID, or comma-separated list of runner IDs
  "endpoint": string, // A caller_id identifying a code path, for example `GET /api/v4/projects/:id` or `ProjectsController#show`. Use comma to separate multiple endpoint paths
  "force": boolean, // Skip feature flag validation checks, such as a YAML definition
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "state": string,
  "gates": {
    "key": string,
    "value": integer,
  },
  "definition": {
    "name": string,
    "feature_issue_url": string,
    "introduced_by_url": string,
    "rollout_issue_url": string,
    "milestone": string,
    "log_state_changes": boolean,
    "type": string,
    "group": string,
    "default_enabled": boolean,
    "intended_to_rollout_by": string,
  },
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

