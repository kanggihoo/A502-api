# 02-Change plan limits [PUT]

`PUT /api/v4/application/plan_limits`

Modify the limits of a plan on the GitLab instance.

### Request Body (application/json)

```json
{
  "plan_name": enum("default" | "free" | "bronze" | "silver" | "premium" | "gold" | "ultimate" | "ultimate_trial" | "ultimate_trial_paid_customer" | "premium_trial" | "opensource") (required), // Name of the plan to update
  "ci_instance_level_variables": integer, // Maximum number of Instance-level CI/CD variables that can be defined
  "ci_pipeline_size": integer, // Maximum number of jobs in a single pipeline
  "ci_active_jobs": integer, // Total number of jobs in currently active pipelines
  "ci_project_subscriptions": integer, // Maximum number of pipeline subscriptions to and from a project
  "ci_pipeline_schedules": integer, // Maximum number of pipeline schedules
  "ci_needs_size_limit": integer, // Maximum number of needs dependencies that a job can have
  "ci_registered_group_runners": integer, // Maximum number of runners created or active in a group during the past seven days
  "ci_registered_project_runners": integer, // Maximum number of runners created or active in a project during the past seven days
  "conan_max_file_size": integer, // Maximum Conan package file size in bytes
  "dotenv_size": integer, // Maximum size of a dotenv artifact in bytes
  "dotenv_variables": integer, // Maximum number of variables in a dotenv artifact
  "enforcement_limit": integer, // Maximum storage size for the root namespace enforcement in MiB
  "generic_packages_max_file_size": integer, // Maximum generic package file size in bytes
  "helm_max_file_size": integer, // Maximum Helm chart file size in bytes
  "maven_max_file_size": integer, // Maximum Maven package file size in bytes
  "notification_limit": integer, // Maximum storage size for the root namespace notifications in MiB
  "npm_max_file_size": integer, // Maximum NPM package file size in bytes
  "nuget_max_file_size": integer, // Maximum NuGet package file size in bytes
  "pypi_max_file_size": integer, // Maximum PyPI package file size in bytes
  "terraform_module_max_file_size": integer, // Maximum Terraform Module package file size in bytes
  "storage_size_limit": integer, // Maximum storage size for the root namespace in MiB
  "pipeline_hierarchy_size": integer, // Maximum number of downstream pipelines in a pipeline's hierarchy tree
  "web_hook_calls": integer, // Maximum number of times a webhook can be called per minute, per top-level namespace. 0 for unlimited.
  "web_hook_calls_low": integer, // Maximum number of times a webhook can be called per minute, per top-level namespace. 0 for unlimited (GitLab.com only).
  "web_hook_calls_mid": integer, // Maximum number of times a webhook can be called per minute, per top-level namespace. 0 for unlimited (GitLab.com only).
  "max_pipelines_per_merge_train": integer, // Maximum number of parallel pipelines per merge train
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

