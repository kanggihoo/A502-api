# 08-Create Admin Role on the GitLab instance [POST]

`POST /api/v4/admin_member_roles`

Create Admin Role on the GitLab instance

### Request Body (application/json)

```json
{
  "name": string, // Name for role (default: 'Admin role - custom')
  "description": string, // Description for role
  "read_admin_cicd": boolean, // Read CI/CD details for runners and jobs in the Admin Area.
  "read_admin_groups": boolean, // Read group details in the Admin Area.
  "read_admin_projects": boolean, // Read project details in the Admin Area.
  "read_admin_subscription": boolean, // Read subscription details in the Admin area.
  "read_admin_monitoring": boolean, // Read system information such as background migrations, health checks, and Gitaly in the Admin Area.
  "read_admin_users": boolean, // Read the user list and user details in the Admin area.
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

