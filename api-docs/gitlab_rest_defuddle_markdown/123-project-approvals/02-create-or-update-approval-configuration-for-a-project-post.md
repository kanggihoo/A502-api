# 02-Create or update approval configuration for a project [POST]

`POST /api/v4/projects/{id}/approvals`

Creates or updates the approval configuration for a project. The currently authenticated user must be an eligible approver.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "approvals_before_merge": integer, // The amount of approvals required before an MR can be merged
  "reset_approvals_on_push": boolean, // Should the approval count be reset on a new push
  "selective_code_owner_removals": boolean, // Reset approvals from Code Owners if their files changed
  "disable_overriding_approvers_per_merge_request": boolean, // Should MRs be able to override approvers and approval count
  "merge_requests_author_approval": boolean, // Should merge request authors be able to self approve merge requests; `true` means authors cannot self approve
  "merge_requests_disable_committers_approval": boolean, // Should committers be able to self approve merge requests
  "require_password_to_approve": boolean, // Should approvers authenticate via password before adding approval
  "require_reauthentication_to_approve": boolean, // Should approvers authenticate via password or SAML before adding approval
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "approvers": {
    "user": {
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
  },
  "approver_groups": {
    "group": {
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
    },
  },
  "approvals_before_merge": integer,
  "reset_approvals_on_push": boolean,
  "selective_code_owner_removals": boolean,
  "disable_overriding_approvers_per_merge_request": boolean,
  "merge_requests_author_approval": boolean,
  "merge_requests_disable_committers_approval": boolean,
  "require_password_to_approve": boolean,
  "require_reauthentication_to_approve": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

