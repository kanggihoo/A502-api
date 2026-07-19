# 01-Get current plan limits [GET]

`GET /api/v4/application/plan_limits`

List the current limits of a plan on the GitLab instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `plan_name` | `string` | `query` | No | Name of the plan to get the limits from. Default: default. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "ci_instance_level_variables": integer,
  "ci_pipeline_size": integer,
  "ci_active_jobs": integer,
  "ci_project_subscriptions": integer,
  "ci_pipeline_schedules": integer,
  "ci_needs_size_limit": integer,
  "ci_registered_group_runners": integer,
  "ci_registered_project_runners": integer,
  "conan_max_file_size": integer,
  "dotenv_variables": integer,
  "dotenv_size": integer,
  "enforcement_limit": integer,
  "generic_packages_max_file_size": integer,
  "helm_max_file_size": integer,
  "limits_history": {},
  "maven_max_file_size": integer,
  "notification_limit": integer,
  "npm_max_file_size": integer,
  "nuget_max_file_size": integer,
  "pipeline_hierarchy_size": integer,
  "pypi_max_file_size": integer,
  "terraform_module_max_file_size": integer,
  "storage_size_limit": integer,
  "web_hook_calls": integer,
  "web_hook_calls_low": integer,
  "web_hook_calls_mid": integer,
  "max_pipelines_per_merge_train": integer,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

