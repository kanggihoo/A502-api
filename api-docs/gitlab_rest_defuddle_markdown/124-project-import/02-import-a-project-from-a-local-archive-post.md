# 02-Import a project from a local archive [POST]

`POST /api/v4/projects/import`

Imports a project from a local archive.

### Request Body (multipart/form-data)

```json
{
  "path": string (required), // The new project path and name
  "file": string (required), // The project export file to be imported
  "name": string, // The name of the project to be imported. Defaults to the path of the project if not provided.
  "namespace": string, // (deprecated) The ID or path of the namespace to import the project to. Defaults to the current user's namespace.
  "namespace_id": integer, // The ID of the namespace that the project will be imported into. Defaults to the current user's namespace.
  "namespace_path": string, // The path of the namespace that the project will be imported into. Defaults to the current user's namespace.
  "overwrite": boolean, // If there is a project in the same namespace and with the same name overwrite it
  "override_params": {
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
    "duo_dependency_bump_breaking_changes_enabled": boolean, // Turn on Agentic Breaking Change Resolution for this project
    "duo_sast_vr_workflow_enabled": boolean, // Enable GitLab Duo SAST vulnerability resolution workflow for this project
    "spp_repository_pipeline_access": boolean, // Grant read-only access to security policy configurations for enforcement in linked CI/CD projects
    "merge_request_title_regex": string, // The regex the Merge Request must adhere to
    "merge_request_title_regex_description": string, // The description for the regex the Merge Request must adhere to
  }, // New project params to override values in the export
  "file.path": string, // Path to locally stored body (generated by Workhorse)
  "file.name": string, // Real filename as send in Content-Disposition (generated by Workhorse)
  "file.type": string, // Real content type as send in Content-Type (generated by Workhorse)
  "file.size": integer, // Real size of file (generated by Workhorse)
  "file.md5": string, // MD5 checksum of the file (generated by Workhorse)
  "file.sha1": string, // SHA1 checksum of the file (generated by Workhorse)
  "file.sha256": string, // SHA256 checksum of the file (generated by Workhorse)
  "file.etag": string, // Etag of the file (generated by Workhorse)
  "file.remote_id": string, // Remote_id of the file (generated by Workhorse)
  "file.remote_url": string, // Remote_url of the file (generated by Workhorse)
}
```
### Responses

#### 201 - Created

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
  "import_status": string,
  "import_type": string,
  "correlation_id": string,
  "failed_relations": [
    {
      "id": integer,
      "created_at": string,
      "exception_class": string,
      "source": string,
      "exception_message": string,
      "relation_name": string,
      "line_number": integer,
    }
  ],
  "import_error": string,
  "stats": {},
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

