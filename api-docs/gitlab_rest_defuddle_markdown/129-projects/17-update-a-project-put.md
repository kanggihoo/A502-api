# 17-Update a project [PUT]

`PUT /api/v4/projects/{id}`

Updates an existing project. If your HTTP repository is not publicly accessible, add authentication information to the URL `https://username:password@gitlab.company.com/group/project.git`, where `password` is a public access key with the `api` scope.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (multipart/form-data)

```json
{
  "name": string, // The name of the project
  "default_branch": string, // The default branch of the project
  "path": string, // The path of the repository
  "description": string, // The description of the project
  "build_git_strategy": enum("fetch" | "clone"), // The Git strategy. Defaults to `fetch`
  "build_timeout": integer, // Build timeout
  "auto_cancel_pending_pipelines": enum("disabled" | "enabled"), // Auto-cancel pending pipelines
  "ci_config_path": string, // The path to CI config file. Defaults to `.gitlab-ci.yml`
  "service_desk_enabled": boolean, // Disable or enable the service desk
  "issues_enabled": boolean, // Flag indication if the issue tracker is enabled
  "merge_requests_enabled": boolean, // Flag indication if merge requests are enabled
  "wiki_enabled": boolean, // Flag indication if the wiki is enabled
  "jobs_enabled": boolean, // Flag indication if jobs are enabled
  "snippets_enabled": boolean, // Flag indication if snippets are enabled
  "issues_access_level": enum("disabled" | "private" | "enabled"), // Issues access level. One of `disabled`, `private` or `enabled`
  "repository_access_level": enum("disabled" | "private" | "enabled"), // Repository access level. One of `disabled`, `private` or `enabled`
  "merge_requests_access_level": enum("disabled" | "private" | "enabled"), // Merge requests access level. One of `disabled`, `private` or `enabled`
  "forking_access_level": enum("disabled" | "private" | "enabled"), // Forks access level. One of `disabled`, `private` or `enabled`
  "wiki_access_level": enum("disabled" | "private" | "enabled"), // Wiki access level. One of `disabled`, `private` or `enabled`
  "builds_access_level": enum("disabled" | "private" | "enabled"), // Builds access level. One of `disabled`, `private` or `enabled`
  "snippets_access_level": enum("disabled" | "private" | "enabled"), // Snippets access level. One of `disabled`, `private` or `enabled`
  "package_registry_access_level": enum("disabled" | "private" | "enabled" | "public"), // Controls visibility of the package registry. One of `disabled`, `private`, `enabled` or `public`. `private` will make the package registry accessible only to project members (reporter role and above). `enabled` will make the package registry accessible to everyone who has access to the project. `public` will make the package registry accessible to everyone. `disabled` will disable the package registry
  "pages_access_level": enum("disabled" | "private" | "enabled" | "public"), // Pages access level. One of `disabled`, `private`, `enabled` or `public`
  "analytics_access_level": enum("disabled" | "private" | "enabled"), // Analytics access level. One of `disabled`, `private` or `enabled`
  "container_registry_access_level": enum("disabled" | "private" | "enabled"), // Controls visibility of the container registry. One of `disabled`, `private` or `enabled`. `private` will make the container registry accessible only to project members (reporter role and above). `enabled` will make the container registry accessible to everyone who has access to the project. `disabled` will disable the container registry
  "security_and_compliance_access_level": enum("disabled" | "private" | "enabled"), // Security and compliance access level. One of `disabled`, `private` or `enabled`
  "releases_access_level": enum("disabled" | "private" | "enabled"), // Releases access level. One of `disabled`, `private` or `enabled`
  "environments_access_level": enum("disabled" | "private" | "enabled"), // Environments access level. One of `disabled`, `private` or `enabled`
  "feature_flags_access_level": enum("disabled" | "private" | "enabled"), // Feature flags access level. One of `disabled`, `private` or `enabled`
  "infrastructure_access_level": enum("disabled" | "private" | "enabled"), // Infrastructure access level. One of `disabled`, `private` or `enabled`
  "monitor_access_level": enum("disabled" | "private" | "enabled"), // Monitor access level. One of `disabled`, `private` or `enabled`
  "model_experiments_access_level": enum("disabled" | "private" | "enabled"), // Model experiments access level. One of `disabled`, `private` or `enabled`
  "model_registry_access_level": enum("disabled" | "private" | "enabled"), // Model registry access level. One of `disabled`, `private` or `enabled`
  "emails_disabled": boolean, // Deprecated: Use emails_enabled instead.
  "emails_enabled": boolean, // Enable email notifications
  "show_default_award_emojis": boolean, // Show default award emojis
  "show_diff_preview_in_email": boolean, // Include the code diff preview in merge request notification emails
  "warn_about_potentially_unwanted_characters": boolean, // Warn about potentially unwanted characters
  "enforce_auth_checks_on_uploads": boolean, // Enforce auth check on uploads
  "shared_runners_enabled": boolean, // Flag indication if shared runners are enabled for that project
  "group_runners_enabled": boolean, // Flag indication if group runners are enabled for that project
  "resource_group_default_process_mode": enum("unordered" | "oldest_first" | "newest_first" | "newest_ready_first"), // The process mode of the resource group
  "resolve_outdated_diff_discussions": boolean, // Automatically resolve merge request diff threads on lines changed with a push
  "remove_source_branch_after_merge": boolean, // Remove the source branch by default after merge
  "packages_enabled": boolean, // Deprecated: Use :package_registry_access_level instead. Enable project packages feature
  "container_registry_enabled": boolean, // Deprecated: Use :container_registry_access_level instead. Flag indication if the container registry is enabled for that project
  "container_expiration_policy_attributes": {
    "cadence": string, // Container expiration policy cadence for recurring job
    "keep_n": integer, // Container expiration policy number of images to keep
    "older_than": string, // Container expiration policy remove images older than value
    "name_regex": string, // Container expiration policy regex for image removal
    "name_regex_keep": string, // Container expiration policy regex for image retention
    "enabled": boolean, // Flag indication if container expiration policy is enabled
  }, // Object that contains information on the container expiration policy
  "lfs_enabled": boolean, // Flag indication if Git LFS is enabled for that project
  "visibility": enum("private" | "internal" | "public"), // The visibility of the project.
  "public_builds": boolean, // Deprecated: Use public_jobs instead.
  "public_jobs": boolean, // Perform public builds
  "request_access_enabled": boolean, // Allow users to request member access
  "only_allow_merge_if_pipeline_succeeds": boolean, // Only allow to merge if builds succeed
  "allow_merge_on_skipped_pipeline": boolean, // Allow to merge if pipeline is skipped
  "only_allow_merge_if_all_discussions_are_resolved": boolean, // Only allow to merge if all threads are resolved
  "tag_list": [
    string
  ], // Deprecated: Use :topics instead
  "topics": [
    string
  ], // The list of topics for a project
  "avatar": string, // Avatar image for project
  "printing_merge_request_link_enabled": boolean, // Show link to create/view merge request when pushing from the command line
  "merge_method": enum("ff" | "rebase_merge" | "merge"), // The merge method used when merging merge requests
  "suggestion_commit_message": string, // The commit message used to apply merge request suggestions
  "merge_commit_template": string, // Template used to create merge commit message
  "squash_commit_template": string, // Template used to create squash commit message
  "issue_branch_template": string, // Template used to create a branch from an issue
  "auto_devops_enabled": boolean, // Flag indication if Auto DevOps is enabled
  "auto_devops_deploy_strategy": enum("continuous" | "manual" | "timed_incremental"), // Auto Deploy strategy
  "autoclose_referenced_issues": boolean, // Flag indication if referenced issues auto-closing is enabled
  "repository_storage": string, // Which storage shard the repository is on. Available only to admins
  "squash_option": enum("never" | "always" | "default_on" | "default_off"), // Squash default for project. One of `never`, `always`, `default_on`, or `default_off`.
  "mr_default_target_self": boolean, // Merge requests of this forked project targets itself by default
  "mr_default_title_template": string, // Template used to generate the default merge request title. Maximum 100 characters.
  "only_allow_merge_if_all_status_checks_passed": boolean, // Blocks merge requests from merging unless all status checks have passed
  "approvals_before_merge": integer, // How many approvers should approve merge request by default
  "mirror": boolean, // [Deprecated] Enables pull mirroring in a project
  "mirror_trigger_builds": boolean, // [Deprecated] Pull mirroring triggers builds
  "external_authorization_classification_label": string, // The classification label for the project
  "requirements_access_level": enum("disabled" | "private" | "enabled"), // Requirements feature access level. One of `disabled`, `private` or `enabled`
  "prevent_merge_without_jira_issue": boolean, // Require an associated issue from Jira
  "auto_duo_code_review_enabled": boolean, // Enable automatic reviews by GitLab Duo on merge requests
  "duo_remote_flows_enabled": boolean, // Enable GitLab Duo remote flows for this project
  "duo_sast_fp_detection_enabled": boolean, // Enable GitLab Duo SAST false positive detection for this project
  "duo_secret_detection_fp_enabled": boolean, // Enable GitLab Duo Secret Detection false positive detection for this project
  "duo_dependency_bump_breaking_changes_enabled": boolean, // Enable Agentic Breaking Change Resolution for this project
  "duo_sast_vr_workflow_enabled": boolean, // Enable GitLab Duo SAST vulnerability resolution workflow for this project
  "spp_repository_pipeline_access": boolean, // Grant read-only access to security policy configurations for enforcement in linked CI/CD projects
  "merge_request_title_regex": string, // The regex the Merge Request must adhere to
  "merge_request_title_regex_description": string, // The description for the regex the Merge Request must adhere to
  "ci_default_git_depth": integer, // Default number of revisions for shallow cloning
  "keep_latest_artifact": boolean, // Indicates if the latest artifact should be kept for this project.
  "ci_forward_deployment_enabled": boolean, // Prevent older deployment jobs that are still pending
  "ci_forward_deployment_rollback_allowed": boolean, // Allow job retries for rollback deployments
  "ci_allow_fork_pipelines_to_run_in_parent_project": boolean, // Allow fork merge request pipelines to run in parent project
  "ci_separated_caches": boolean, // Enable or disable separated caches based on branch protection.
  "restrict_user_defined_variables": boolean, // Restrict use of user-defined variables when triggering a pipeline
  "ci_pipeline_variables_minimum_override_role": enum("no_one_allowed" | "developer" | "maintainer" | "owner"), // Limit ability to override CI/CD variables when triggering a pipeline to only users with at least the set minimum role
  "ci_push_repository_for_job_token_allowed": boolean, // Allow pushing to this project's repository by authenticating with a CI/CD job token generated in this project.
  "ci_id_token_sub_claim_components": [
    string
  ], // Claims that will be used to build the sub claim in id tokens
  "ci_delete_pipelines_in_seconds": integer, // Pipelines older than the configured time are deleted
  "max_artifacts_size": integer, // Set the maximum file size for each job's artifacts
  "protect_merge_request_pipelines": boolean, // Make protected CI/CD variables and runners available in merge request pipelines
  "ci_display_pipeline_variables": boolean, // Display all manually-defined variables in the pipeline details page after running a pipeline manually
  "allow_pipeline_trigger_approve_deployment": boolean, // Allow pipeline triggerer to approve deployments
  "mirror_user_id": integer, // [Deprecated] User responsible for all the activity surrounding a pull mirror event. Can only be set by admins
  "only_mirror_protected_branches": boolean, // [Deprecated] Only mirror protected branches
  "mirror_branch_regex": string, // [Deprecated] Only mirror branches match regex
  "mirror_overwrites_diverged_branches": boolean, // [Deprecated] Pull mirror overwrites diverged branches
  "import_url": string, // URL from which the project is imported
  "fallback_approvals_required": integer, // Overall approvals required when no rule is present
  "issues_template": string, // Default description for Issues. Description is parsed with GitLab Flavored Markdown.
  "merge_requests_template": string, // Default description for merge requests. Description is parsed with GitLab Flavored Markdown.
  "merge_pipelines_enabled": boolean, // Enable merged results pipelines.
  "merge_trains_enabled": boolean, // Enable merge trains.
  "merge_trains_skip_train_allowed": boolean, // Allow merge train merge requests to be merged without waiting for pipelines to finish.
  "merge_train_enforcement": enum("allow_bypass" | "enforce_for_all_users" | "enforce_with_owner_override"), // Merge train enforcement level. One of `allow_bypass`, `enforce_for_all_users`, or `enforce_with_owner_override`.
  "max_pipelines_per_merge_train": integer, // Maximum number of parallel pipelines per merge train for this project.
  "ci_restrict_pipeline_cancellation_role": string, // Roles allowed to cancel pipelines and jobs.
  "web_based_commit_signing_enabled": boolean, // Enable web based commit signing for this project
  "security_policy_pipeline_must_succeed": boolean, // Require all security policy pipelines to succeed before merge requests can be merged
  "reviewer_assignment_strategy": enum("disabled" | "code_owners" | "dap_powered"), // Strategy used to automatically assign reviewers to merge requests. One of `disabled`, `code_owners`, or `dap_powered`.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "name": string,
  "name_with_namespace": string,
  "path": string,
  "path_with_namespace": string,
  "created_at": string,
  "default_branch": string,
  "tag_list": [
    string
  ],
  "topics": [
    string
  ],
  "ssh_url_to_repo": string,
  "http_url_to_repo": string,
  "web_url": string,
  "readme_url": string,
  "forks_count": integer,
  "license_url": string,
  "license": {
    "key": string,
    "name": string,
    "nickname": string,
    "html_url": string,
    "source_url": string,
  },
  "avatar_url": string,
  "star_count": integer,
  "last_activity_at": string,
  "visibility": string,
  "namespace": {
    "id": integer,
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
  "custom_attributes": {
    "key": string,
    "value": string,
  },
  "repository_storage": string,
  "forked_from_project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
    "default_branch": string,
    "tag_list": [
      string
    ],
    "topics": [
      string
    ],
    "ssh_url_to_repo": string,
    "http_url_to_repo": string,
    "web_url": string,
    "readme_url": string,
    "forks_count": integer,
    "license_url": string,
    "license": {
      "key": string,
      "name": string,
      "nickname": string,
      "html_url": string,
      "source_url": string,
    },
    "avatar_url": string,
    "star_count": integer,
    "last_activity_at": string,
    "visibility": string,
    "namespace": {
      "id": integer,
      "name": string,
      "path": string,
      "kind": string,
      "full_path": string,
      "parent_id": integer,
      "avatar_url": string,
      "web_url": string,
    },
    "custom_attributes": {
      "key": string,
      "value": string,
    },
    "repository_storage": string,
  },
  "container_registry_image_prefix": string,
  "_links": {},
  "marked_for_deletion_at": string,
  "marked_for_deletion_on": string,
  "packages_enabled": boolean,
  "empty_repo": boolean,
  "archived": boolean,
  "owner": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "resolve_outdated_diff_discussions": boolean,
  "container_expiration_policy": {
    "cadence": string,
    "enabled": string,
    "keep_n": string,
    "older_than": string,
    "name_regex": string,
    "name_regex_keep": string,
    "next_run_at": string,
  },
  "repository_object_format": string,
  "issues_enabled": boolean,
  "merge_requests_enabled": boolean,
  "wiki_enabled": boolean,
  "jobs_enabled": boolean,
  "snippets_enabled": boolean,
  "container_registry_enabled": boolean,
  "service_desk_enabled": boolean,
  "service_desk_address": string,
  "can_create_merge_request_in": boolean,
  "issues_access_level": string,
  "repository_access_level": string,
  "merge_requests_access_level": string,
  "forking_access_level": string,
  "wiki_access_level": string,
  "builds_access_level": string,
  "snippets_access_level": string,
  "pages_access_level": string,
  "analytics_access_level": string,
  "container_registry_access_level": string,
  "security_and_compliance_access_level": string,
  "releases_access_level": string,
  "environments_access_level": string,
  "feature_flags_access_level": string,
  "infrastructure_access_level": string,
  "monitor_access_level": string,
  "model_experiments_access_level": string,
  "model_registry_access_level": string,
  "package_registry_access_level": string,
  "emails_disabled": boolean,
  "emails_enabled": boolean,
  "show_diff_preview_in_email": boolean,
  "shared_runners_enabled": boolean,
  "lfs_enabled": boolean,
  "creator_id": integer,
  "mr_default_target_self": boolean,
  "import_url": string,
  "import_type": string,
  "import_status": string,
  "import_error": string,
  "open_issues_count": integer,
  "description_html": string,
  "updated_at": string,
  "ci_default_git_depth": integer,
  "ci_delete_pipelines_in_seconds": integer,
  "ci_forward_deployment_enabled": boolean,
  "ci_forward_deployment_rollback_allowed": boolean,
  "ci_job_token_scope_enabled": boolean,
  "ci_separated_caches": boolean,
  "ci_allow_fork_pipelines_to_run_in_parent_project": boolean,
  "ci_id_token_sub_claim_components": [
    string
  ],
  "build_git_strategy": string,
  "keep_latest_artifact": boolean,
  "restrict_user_defined_variables": boolean,
  "ci_pipeline_variables_minimum_override_role": string,
  "runner_token_expiration_interval": integer,
  "group_runners_enabled": boolean,
  "resource_group_default_process_mode": string,
  "auto_cancel_pending_pipelines": string,
  "build_timeout": integer,
  "auto_devops_enabled": boolean,
  "auto_devops_deploy_strategy": string,
  "ci_push_repository_for_job_token_allowed": boolean,
  "protect_merge_request_pipelines": boolean,
  "ci_display_pipeline_variables": boolean,
  "runners_token": string,
  "ci_config_path": string,
  "public_jobs": boolean,
  "shared_with_groups": [
    {}
  ],
  "only_allow_merge_if_pipeline_succeeds": boolean,
  "allow_merge_on_skipped_pipeline": boolean,
  "request_access_enabled": boolean,
  "only_allow_merge_if_all_discussions_are_resolved": boolean,
  "remove_source_branch_after_merge": boolean,
  "printing_merge_request_link_enabled": boolean,
  "merge_method": string,
  "squash_option": string,
  "enforce_auth_checks_on_uploads": boolean,
  "suggestion_commit_message": string,
  "merge_commit_template": string,
  "squash_commit_template": string,
  "mr_default_title_template": string,
  "issue_branch_template": string,
  "statistics": {
    "commit_count": integer,
    "storage_size": integer,
    "repository_size": integer,
    "wiki_size": integer,
    "lfs_objects_size": integer,
    "job_artifacts_size": integer,
    "pipeline_artifacts_size": integer,
    "packages_size": integer,
    "snippets_size": integer,
    "uploads_size": integer,
    "container_registry_size": integer,
  },
  "warn_about_potentially_unwanted_characters": boolean,
  "autoclose_referenced_issues": boolean,
  "max_artifacts_size": integer,
  "approvals_before_merge": string,
  "mirror": string,
  "mirror_user_id": string,
  "mirror_trigger_builds": string,
  "only_mirror_protected_branches": string,
  "mirror_overwrites_diverged_branches": string,
  "external_authorization_classification_label": string,
  "requirements_enabled": string,
  "requirements_access_level": string,
  "security_and_compliance_enabled": string,
  "secret_push_protection_enabled": boolean,
  "pre_receive_secret_detection_enabled": boolean,
  "compliance_frameworks": string,
  "issues_template": string,
  "merge_requests_template": string,
  "ci_restrict_pipeline_cancellation_role": string,
  "merge_pipelines_enabled": string,
  "merge_trains_enabled": string,
  "merge_trains_skip_train_allowed": string,
  "merge_train_enforcement": string,
  "max_pipelines_per_merge_train": string,
  "only_allow_merge_if_all_status_checks_passed": string,
  "allow_pipeline_trigger_approve_deployment": boolean,
  "prevent_merge_without_jira_issue": string,
  "auto_duo_code_review_enabled": string,
  "reviewer_assignment_strategy": string,
  "duo_remote_flows_enabled": string,
  "duo_foundational_flows_enabled": string,
  "duo_sast_fp_detection_enabled": string,
  "duo_secret_detection_fp_enabled": string,
  "duo_dependency_bump_breaking_changes_enabled": string,
  "duo_sast_vr_workflow_enabled": string,
  "web_based_commit_signing_enabled": string,
  "spp_repository_pipeline_access": boolean, // The spp_repository_pipeline_access setting is only visible if the security_orchestration_policies feature is available.
  "security_policy_pipeline_must_succeed": boolean, // Require all security policy pipelines to succeed before merge requests can be merged.
  "merge_request_title_regex": string,
  "merge_request_title_regex_description": string,
}
```

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not Found

