# 20-Create a group [POST]

`POST /api/v4/groups`

Creates a project group. Available only for users who can create groups.

### Request Body (multipart/form-data)

```json
{
  "name": string (required), // The name of the group
  "path": string (required), // The path of the group
  "parent_id": integer, // The parent group id for creating nested group
  "organization_id": integer, // The organization id for the group
  "description": string, // The description of the group
  "visibility": enum("private" | "internal" | "public"), // The visibility of the group
  "avatar": string, // Avatar image for the group
  "share_with_group_lock": boolean, // Prevent sharing a project with another group within this group
  "require_two_factor_authentication": boolean, // Require all users in this group to setup Two-factor authentication
  "two_factor_grace_period": integer, // Time before Two-factor authentication is enforced
  "project_creation_level": enum("noone" | "owner" | "maintainer" | "developer" | "administrator"), // Determine if developers can create projects in the group
  "auto_devops_enabled": boolean, // Default to Auto DevOps pipeline for all projects within this group
  "subgroup_creation_level": enum("owner" | "maintainer"), // Allowed to create subgroups
  "emails_disabled": boolean, // _(Deprecated)_ Disable email notifications. Use: emails_enabled
  "emails_enabled": boolean, // Enable email notifications
  "show_diff_preview_in_email": boolean, // Include the code diff preview in merge request notification emails
  "mentions_disabled": boolean, // Disable a group from getting mentioned
  "lfs_enabled": boolean, // Enable/disable LFS for the projects in this group
  "request_access_enabled": boolean, // Allow users to request member access
  "default_branch": string, // The default branch of group's projects
  "default_branch_protection": enum(0 | 3 | 1 | 2 | 4), // Determine if developers can push to default branch
  "default_branch_protection_defaults": {
    "allowed_to_push": [
      {
        "access_level": enum(30 | 40 | 60 | 0) (required), // A valid access level
      }
    ], // An array of access levels allowed to push
    "allow_force_push": boolean, // Allow force push for all users with push access.
    "allowed_to_merge": [
      {
        "access_level": enum(30 | 40 | 60 | 0) (required), // A valid access level
      }
    ], // An array of access levels allowed to merge
    "code_owner_approval_required": boolean, // Require approval from code owners
    "developer_can_initial_push": boolean, // Allow developers to initial push
  }, // Determine if developers can push to default branch
  "enabled_git_access_protocol": enum("ssh" | "http" | "all"), // Allow only the selected protocols to be used for Git access.
  "crm_enabled": boolean, // Enable Customer Relations Management for this group
  "resource_access_token_notify_inherited": boolean, // Send access token expiry notifications to all inherited members of the group
  "lock_resource_access_token_notify_inherited": boolean, // Prevent subgroups from overriding the access token expiry notification setting
  "membership_lock": boolean, // Prevent adding new members to projects within this group
  "ldap_cn": string, // LDAP Common Name
  "ldap_access": integer, // A valid access level
  "shared_runners_minutes_limit": integer, // (admin-only) compute minutes quota for this group
  "extra_shared_runners_minutes_limit": integer, // (admin-only) Extra compute minutes quota for this group
  "wiki_access_level": enum("disabled" | "private" | "enabled"), // Wiki access level. One of `disabled`, `private` or `enabled`
  "duo_availability": enum("default_on" | "default_off" | "never_on" | "always_on"), // Duo availability. One of `default_on`, `default_off`, `never_on` or `always_on`
  "duo_remote_flows_availability": boolean, // Enable GitLab Duo remote flows for this group
  "duo_foundational_flows_availability": boolean, // Enable GitLab foundational Duo flows for this group
  "duo_custom_agents_availability": boolean, // Enable GitLab Duo custom agents for this group
  "duo_custom_flows_availability": boolean, // Enable GitLab Duo custom flows for this group
  "duo_external_agents_availability": boolean, // Enable GitLab Duo external agents for this group
  "tool_approval_for_session_availability": enum("default_on" | "default_off" | "never_on"), // Tool approval for session availability. One of `default_on`, `default_off` or `never_on`
  "amazon_q_auto_review_enabled": boolean, // Enable Amazon Q auto review for merge request
  "experiment_features_enabled": boolean, // Enable experiment features for this group
  "model_prompt_cache_enabled": boolean, // Enable model prompt cache for this group
  "foundational_agents_statuses": [
    {
      "reference": string (required), // Reference of the foundational agent.
      "enabled": boolean (required), // Whether foundational agent has been enabled or disabled.
    }
  ], // Whether each foundational agent has been enabled or disabled.
  "ai_settings_attributes": {
    "duo_agent_platform_enabled": boolean, // Whether Duo Agent Platform features are enabled
    "duo_workflow_mcp_enabled": boolean, // Enable MCP support for Duo Agent Platform
    "ai_usage_data_collection_enabled": boolean, // Enable AI usage data collection for this namespace
    "ai_catalog_restricted_to_group_hierarchy": boolean, // Restrict the AI Catalog to items within this top-level group hierarchy
    "foundational_agents_default_enabled": boolean, // Whether new foundational agents are enabled by default
    "prompt_injection_protection_level": enum("no_checks" | "log_only" | "interrupt"), // Prompt injection protection level. One of `no_checks`, `log_only` or `interrupt`
    "include_recommended_allowed": boolean, // Whether to include recommended domains in the network access allowlist
    "allow_all_unix_sockets": boolean, // Whether to allow all Unix sockets for network access
    "allow_project_extension": boolean, // Whether to allow projects to extend the network access domain allowlist
    "minimum_access_level_execute": enum(10 | 15 | 20 | 30 | 40 | 50), // The minimum access level required to execute Duo Agent Platform. This field is behind a feature flag.
    "minimum_access_level_execute_async": enum(30 | 40 | 50), // The minimum access level required to execute Duo Agent Platform features in CI/CD. This field is behind a feature flag.
    "minimum_access_level_manage": enum(30 | 40 | 50), // The minimum access level required to manage Duo Agent Platform. This field is behind a feature flag.
    "minimum_access_level_enable_on_projects": enum(30 | 40 | 50), // The minimum access level required to enable Duo Agent Platform. This field is behind a feature flag.
  }, // AI-related settings
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "web_url": string,
  "name": string,
  "path": string,
  "description": string,
  "visibility": string,
  "share_with_group_lock": boolean,
  "require_two_factor_authentication": boolean,
  "two_factor_grace_period": integer,
  "project_creation_level": string,
  "auto_devops_enabled": string,
  "subgroup_creation_level": string,
  "emails_disabled": boolean,
  "emails_enabled": boolean,
  "show_diff_preview_in_email": boolean,
  "mentions_disabled": string,
  "lfs_enabled": boolean,
  "archived": boolean,
  "math_rendering_limits_enabled": boolean,
  "lock_math_rendering_limits_enabled": boolean,
  "crm_enabled": boolean,
  "resource_access_token_notify_inherited": boolean,
  "lock_resource_access_token_notify_inherited": boolean,
  "default_branch": string,
  "default_branch_protection": integer,
  "default_branch_protection_defaults": string,
  "avatar_url": string,
  "request_access_enabled": boolean,
  "full_name": string,
  "full_path": string,
  "created_at": string,
  "parent_id": string,
  "organization_id": integer,
  "shared_runners_setting": string,
  "max_artifacts_size": integer,
  "custom_attributes": {
    "key": string,
    "value": string,
  },
  "statistics": string,
  "marked_for_deletion_on": string,
  "root_storage_statistics": {
    "build_artifacts_size": integer, // CI artifacts size in bytes.
    "container_registry_size": integer, // container registry size in bytes.
    "container_registry_size_is_estimated": boolean, // Indicates whether the deduplicated container registry size for the namespace is an estimated value or not.
    "dependency_proxy_size": integer, // Dependency Proxy sizes in bytes.
    "lfs_objects_size": integer, // LFS objects size in bytes.
    "packages_size": integer, // Packages size in bytes.
    "pipeline_artifacts_size": integer, // CI pipeline artifacts size in bytes.
    "repository_size": integer, // Git repository size in bytes.
    "snippets_size": integer, // Snippets size in bytes.
    "storage_size": integer, // Total storage in bytes.
    "uploads_size": integer, // Uploads size in bytes.
    "wiki_size": integer, // Wiki size in bytes.
  },
  "ldap_cn": string,
  "ldap_access": string,
  "ldap_group_links": {
    "cn": string,
    "group_access": integer,
    "provider": string,
    "filter": string,
    "member_role_id": integer,
  },
  "saml_group_links": {
    "name": string,
    "access_level": integer,
    "member_role_id": integer,
    "provider": string,
  },
  "file_template_project_id": string,
  "wiki_access_level": string,
  "repository_storage": string,
  "duo_core_features_enabled": boolean, // [Experimental] Indicates whether GitLab Duo Core features are enabled for the group
  "duo_features_enabled": string,
  "lock_duo_features_enabled": string,
  "auto_duo_code_review_enabled": string,
  "web_based_commit_signing_enabled": string,
  "allow_personal_snippets": string,
  "duo_namespace_access_rules": string,
  "built_in_project_templates_enabled": boolean,
  "lock_built_in_project_templates_enabled": boolean,
}
```

#### 400 - Bad Request

