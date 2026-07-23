# 12-Update a project member [PUT]

`PUT /api/v4/projects/{id}/members/{user_id}`

Updates a specified member of a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `user_id` | `integer` | `path` | Yes | The user ID of the new member |

### Request Body (application/json)

```json
{
  "access_level": integer (required), // A valid access level
  "expires_at": string, // Date string in the format YEAR-MONTH-DAY
  "member_role_id": integer, // The ID of the Member Role to be updated
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
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
  "access_level": string,
  "created_at": string,
  "created_by": {
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
  "expires_at": string,
  "group_saml_identity": {
    "provider": string,
    "extern_uid": string,
    "saml_provider_id": string,
  },
  "group_scim_identity": {
    "extern_uid": string,
    "group_id": string,
    "active": string,
  },
  "email": string,
  "is_using_seat": string,
  "override": string,
  "membership_state": string,
  "member_role": {
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
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

