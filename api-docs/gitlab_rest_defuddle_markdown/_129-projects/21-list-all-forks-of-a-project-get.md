# 21-List all forks of a project [GET]

`GET /api/v4/projects/{id}/forks`

Lists all forks of a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `order_by` | `string` | `query` | No | Return projects ordered by field. storage_size, repository_size, wiki_size, packages_size are only available to admins. Similarity is available when searching and is limited to projects the user has access to. |
| `sort` | `string` | `query` | No | Return projects sorted in ascending and descending order |
| `archived` | `boolean` | `query` | No | Limit by archived status |
| `visibility` | `string` | `query` | No | Limit by visibility |
| `search` | `string` | `query` | No | Return list of projects matching the search criteria |
| `search_namespaces` | `boolean` | `query` | No | Include ancestor namespaces when matching search criteria |
| `owned` | `boolean` | `query` | No | Limit by owned by authenticated user |
| `starred` | `boolean` | `query` | No | Limit by starred status |
| `imported` | `boolean` | `query` | No | Limit by imported by authenticated user |
| `membership` | `boolean` | `query` | No | Limit by projects that the current user is a member of |
| `with_issues_enabled` | `boolean` | `query` | No | Limit by enabled issues feature |
| `with_merge_requests_enabled` | `boolean` | `query` | No | Limit by enabled merge requests feature |
| `with_programming_language` | `string` | `query` | No | Limit to repositories which use the given programming language |
| `min_access_level` | `integer` | `query` | No | Limit by minimum access level of authenticated user |
| `id_after` | `integer` | `query` | No | Limit results to projects with IDs greater than the specified ID |
| `id_before` | `integer` | `query` | No | Limit results to projects with IDs less than the specified ID |
| `last_activity_after` | `string` | `query` | No | Limit results to projects with last_activity after specified time. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `last_activity_before` | `string` | `query` | No | Limit results to projects with last_activity before specified time. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `repository_storage` | `string` | `query` | No | Which storage shard the repository is on. Available only to admins |
| `topic` | `array` | `query` | No | Comma-separated list of topics. Limit results to projects having all topics |
| `topic_id` | `integer` | `query` | No | Limit results to projects with the assigned topic given by the topic ID |
| `updated_before` | `string` | `query` | No | Return projects updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return projects updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `include_pending_delete` | `boolean` | `query` | No | Include projects in pending delete state. Can only be set by admins |
| `marked_for_deletion_on` | `string` | `query` | No | Date when the project was marked for deletion |
| `active` | `boolean` | `query` | No | Limit by projects that are not archived and not marked for deletion |
| `wiki_checksum_failed` | `boolean` | `query` | No | Limit by projects where wiki checksum is failed |
| `repository_checksum_failed` | `boolean` | `query` | No | Limit by projects where repository checksum is failed |
| `include_hidden` | `boolean` | `query` | No | Include hidden projects. Can only be set by admins |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `simple` | `boolean` | `query` | No | Return only the ID, URL, name, and path of each project |
| `with_custom_attributes` | `boolean` | `query` | No | Include custom attributes in the response |
| `custom_attributes` | `object` | `query` | No | Filter with custom attributes |

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

#### 400 - Bad Request

#### 404 - Not Found

