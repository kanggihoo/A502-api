# 02-Add a member role to a group [POST]

`POST /api/v4/groups/{id}/member_roles`

Adds a member role to a group. You can only add member roles at the root level of the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "base_access_level": enum(10 | 15 | 20 | 25 | 30 | 40 | 50) (required), // Base Access Level for the configured role
  "name": string, // Name for role (default: 'Custom')
  "description": string, // Description for role
  "apply_security_scan_profiles": boolean, // Apply security scan profiles.
  "admin_merge_request": boolean, // Allows approval of merge requests.
  "archive_project": boolean, // Allows archiving of projects.
  "admin_ai_catalog_item_consumer": boolean, // Enable, disable, and configure custom agents and flows from the AI catalog for a project.
  "destroy_package": boolean, // Delete packages and package files in the package registry.
  "remove_project": boolean, // Allows deletion of projects.
  "remove_group": boolean, // Ability to delete or restore a subgroup. This ability does not allow deleting top-level groups. Review the retention period settings to prevent accidental deletion.
  "manage_security_policy_link": boolean, // Allows linking security policy projects.
  "admin_ai_catalog_item": boolean, // Create, edit, and delete custom agents and flows in the AI catalog.
  "admin_compliance_framework": boolean, // Create, read, update, and delete compliance frameworks. Users with this permission can also assign a compliance framework label to a project, and set the default framework of a group.
  "admin_cicd_variables": boolean, // Create, read, update, and delete CI/CD variables.
  "manage_deploy_tokens": boolean, // Manage deploy tokens at the group or project level.
  "manage_group_access_tokens": boolean, // Create, read, update, and delete group access tokens. When creating a token, users with this custom permission must select a role for that token that has the same or fewer permissions as the default role used as the base for the custom role.
  "admin_group_member": boolean, // Add or remove users in a group, and assign roles to users. When assigning a role, users with this custom permission must select a role that has the same or fewer permissions as the default role used as the base for their custom role.
  "admin_integrations": boolean, // Create, read, update, and delete integrations with external applications.
  "manage_merge_request_settings": boolean, // Configure merge request settings at the group or project level. Group actions include managing merge checks and approval settings. Project actions include managing MR configurations, approval rules and settings, and branch targets. In order to enable Suggested reviewers, the "Manage project access tokens" custom permission needs to be enabled.
  "manage_project_access_tokens": boolean, // Create, read, update, and delete project access tokens. When creating a token, users with this custom permission must select a role for that token that has the same or fewer permissions as the default role used as the base for the custom role.
  "admin_protected_branch": boolean, // Create, read, update, and delete protected branches for a project.
  "admin_protected_environments": boolean, // Create, read, update, and delete protected environments
  "admin_push_rules": boolean, // Configure push rules for repositories at the group or project level.
  "admin_runners": boolean, // Create, view, edit, and delete group or project Runners. Includes configuring Runner settings.
  "admin_security_attributes": boolean, // Manage the security categories and attributes belonging to a top-level group. Also requires the `read_security_attribute` permission.
  "admin_terraform_state": boolean, // Execute terraform commands, lock/unlock terraform state files, and remove file versions.
  "admin_vulnerability": boolean, // Edit the status, linked issue, and severity of a vulnerability object. Also requires the `read_vulnerability` permission.
  "admin_web_hook": boolean, // Manage webhooks
  "read_agent_artifacts": boolean, // Read GitLab Duo Agent Platform artifacts, including audit events and session metadata, that are exposed through the agent artifacts dashboard.
  "read_compliance_dashboard": boolean, // Read compliance capabilities including adherence, violations, and frameworks for groups and projects.
  "read_security_scan_profiles": boolean, // Read security scan profiles.
  "read_virtual_registry": boolean, // Allows read access to virtual registries at the group level. Enables users to resolve packages through the virtual registry without requiring broader group membership permissions. Only works on top level groups.
  "update_sec_ai_workflow_settings": boolean, // Update security AI workflow settings such as SAST Vulnerability Resolution. Also requires the `read_vulnerability` permission.
  "read_admin_cicd": boolean, // Read CI/CD details for runners and jobs in the Admin Area.
  "read_crm_contact": boolean, // Read CRM contact.
  "read_dependency": boolean, // Allows read-only access to the dependencies and licenses.
  "read_admin_groups": boolean, // Read group details in the Admin Area.
  "read_admin_projects": boolean, // Read project details in the Admin Area.
  "read_code": boolean, // Allows read-only access to the source code in the user interface. Does not allow users to edit or download repository archives, clone or pull repositories, view source code in an IDE, or view merge requests for private projects. You can download individual files because read-only access inherently grants the ability to make a local copy of the file.
  "read_runners": boolean, // Allows read-only access to group or project runners, including the runner fleet dashboard.
  "read_security_attribute": boolean, // Allows read-only access to the security categories and attributes that belong to a top-level group.
  "read_admin_subscription": boolean, // Read subscription details in the Admin area.
  "read_admin_monitoring": boolean, // Read system information such as background migrations, health checks, and Gitaly in the Admin Area.
  "read_admin_users": boolean, // Read the user list and user details in the Admin area.
  "read_vulnerability": boolean, // Read vulnerability reports and security dashboards.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "group_id": integer,
  "name": string,
  "description": string,
  "base_access_level": integer,
  "apply_security_scan_profiles": boolean,
  "admin_merge_request": boolean,
  "archive_project": boolean,
  "admin_ai_catalog_item_consumer": boolean,
  "destroy_package": boolean,
  "remove_project": boolean,
  "remove_group": boolean,
  "manage_security_policy_link": boolean,
  "admin_ai_catalog_item": boolean,
  "admin_compliance_framework": boolean,
  "admin_cicd_variables": boolean,
  "manage_deploy_tokens": boolean,
  "manage_group_access_tokens": boolean,
  "admin_group_member": boolean,
  "admin_integrations": boolean,
  "manage_merge_request_settings": boolean,
  "manage_project_access_tokens": boolean,
  "admin_protected_branch": boolean,
  "admin_protected_environments": boolean,
  "admin_push_rules": boolean,
  "admin_runners": boolean,
  "admin_security_attributes": boolean,
  "admin_terraform_state": boolean,
  "admin_vulnerability": boolean,
  "admin_web_hook": boolean,
  "read_agent_artifacts": boolean,
  "read_compliance_dashboard": boolean,
  "read_security_scan_profiles": boolean,
  "read_virtual_registry": boolean,
  "update_sec_ai_workflow_settings": boolean,
  "read_admin_cicd": boolean,
  "read_crm_contact": boolean,
  "read_dependency": boolean,
  "read_admin_groups": boolean,
  "read_admin_projects": boolean,
  "read_code": boolean,
  "read_runners": boolean,
  "read_security_attribute": boolean,
  "read_admin_subscription": boolean,
  "read_admin_monitoring": boolean,
  "read_admin_users": boolean,
  "read_vulnerability": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

