# 32-List all descendant groups [GET]

`GET /api/v4/groups/{id}/descendant_groups`

Lists all descendant groups for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `statistics` | `boolean` | `query` | No | Include project statistics |
| `archived` | `boolean` | `query` | No | Limit by archived status |
| `skip_groups` | `array` | `query` | No | Array of group ids to exclude from list |
| `all_available` | `boolean` | `query` | No | When `true`, returns all accessible groups. When `false`, returns only groups where the user is a member. |
| `visibility` | `string` | `query` | No | Limit by visibility |
| `search` | `string` | `query` | No | Search for a specific group |
| `owned` | `boolean` | `query` | No | Limit by owned by authenticated user |
| `order_by` | `string` | `query` | No | Order by name, path, id or similarity if searching |
| `sort` | `string` | `query` | No | Sort by asc (ascending) or desc (descending) |
| `min_access_level` | `integer` | `query` | No | Minimum access level of authenticated user |
| `top_level_only` | `boolean` | `query` | No | Only include top-level groups |
| `marked_for_deletion_on` | `string` | `query` | No | Return groups that are marked for deletion on this date |
| `active` | `boolean` | `query` | No | Limit by groups that are not archived and not marked for deletion |
| `repository_storage` | `string` | `query` | No | Filter by repository storage used by the group |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `with_custom_attributes` | `boolean` | `query` | No | Include custom attributes in the response |
| `custom_attributes` | `object` | `query` | No | Filter with custom attributes |

### Responses

#### 200 - OK

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

#### 404 - Not Found

