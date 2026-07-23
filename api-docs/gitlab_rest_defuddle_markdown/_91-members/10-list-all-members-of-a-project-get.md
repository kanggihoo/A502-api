# 10-List all members of a project [GET]

`GET /api/v4/projects/{id}/members/all`

Lists all members of a specified project viewable by the authenticated user. Also returns inherited members from ancestor groups or invited groups. If a user is a member of this project and one or more ancestor groups, only returns the highest `access_level`. Members from an invited group are returned if the invited group is public, the requester is a member of an invited group, or the requester is a member of the shared group or project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `query` | `string` | `query` | No | A query string to search for members |
| `user_ids` | `array` | `query` | No | Array of user ids to look up for membership |
| `show_seat_info` | `boolean` | `query` | No | Show seat information for members |
| `state` | `string` | `query` | No | Filter results by member state |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

