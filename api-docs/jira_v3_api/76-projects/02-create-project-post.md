# 02-Create project [POST]

`POST /rest/api/3/project`

Creates a project based on a project type template, as shown in the following table:

| Project Type Key | Project Template Key |  
|--|--|  
| `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`, `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |  
| `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`, `com.atlassian.servicedesk:simplified-external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`, `com.atlassian.servicedesk:simplified-facilities-service-desk`, `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`, `com.atlassian.servicedesk:simplified-design-service-desk`, `com.atlassian.servicedesk:simplified-sales-service-desk`, `com.atlassian.servicedesk:simplified-finance-service-desk`, `com.atlassian.servicedesk:company-managed-blank-service-project`, `com.atlassian.servicedesk:company-managed-general-service-project`, `com.atlassian.servicedesk:team-managed-general-service-project`, `com.atlassian.servicedesk:next-gen-it-service-desk`, `com.atlassian.servicedesk:next-gen-hr-service-desk`, `com.atlassian.servicedesk:next-gen-legal-service-desk`, `com.atlassian.servicedesk:next-gen-marketing-service-desk`, `com.atlassian.servicedesk:next-gen-facilities-service-desk`, `com.atlassian.servicedesk:next-gen-analytics-service-desk`, `com.atlassian.servicedesk:next-gen-finance-service-desk`, `com.atlassian.servicedesk:next-gen-design-service-desk`, `com.atlassian.servicedesk:next-gen-sales-service-desk` |  
| `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`, `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-simplified-scrum-classic` |  
| `customer_service` | `com.atlassian.jcs:customer-service-management` |  
The project types are available according to the installed Jira features as follows:

 *  Jira Core, the default, enables `business` projects.
 *  Jira Service Management enables `service_desk` projects.
 *  Jira Software enables `software` projects.

To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "assigneeType": enum("PROJECT_LEAD" | "UNASSIGNED"), // The default assignee when creating issues for this project.
  "avatarId": integer, // An integer value for the project's avatar.
  "categoryId": integer, // The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.
  "description": string, // A brief description of the project.
  "fieldConfigurationScheme": integer, // Deprecated use [fieldScheme](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) instead. The ID of the field configuration scheme for the project. Use the [Get all field configuration schemes](#api-rest-api-3-fieldconfigurationscheme-get) operation to get a list of field configuration scheme IDs. If you specify the field configuration scheme you cannot specify the project template key.
  "fieldScheme": integer, // The ID of the field scheme for the project. Use the [Get field schemes](#api-rest-api-3-config-fieldschemes-get) operation to get a list of field scheme IDs. If you specify the field scheme you cannot specify the project template key.
  "issueSecurityScheme": integer, // The ID of the issue security scheme for the project, which enables you to control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.
  "issueTypeScheme": integer, // The ID of the issue type scheme for the project. Use the [Get all issue type schemes](#api-rest-api-3-issuetypescheme-get) operation to get a list of issue type scheme IDs. If you specify the issue type scheme you cannot specify the project template key.
  "issueTypeScreenScheme": integer, // The ID of the issue type screen scheme for the project. Use the [Get all issue type screen schemes](#api-rest-api-3-issuetypescreenscheme-get) operation to get a list of issue type screen scheme IDs. If you specify the issue type screen scheme you cannot specify the project template key.
  "key": string (required), // Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters.
  "lead": string, // This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `leadAccountId`.
  "leadAccountId": string, // The account ID of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `lead`.
  "name": string (required), // The name of the project.
  "notificationScheme": integer, // The ID of the notification scheme for the project. Use the [Get notification schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.
  "permissionScheme": integer, // The ID of the permission scheme for the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.
  "projectTemplateKey": enum("com.pyxis.greenhopper.jira:gh-simplified-agility-kanban" | "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum" | "com.pyxis.greenhopper.jira:gh-simplified-basic" | "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic" | "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic" | "com.pyxis.greenhopper.jira:gh-cross-team-template" | "com.pyxis.greenhopper.jira:gh-cross-team-planning-template" | "com.atlassian.servicedesk:simplified-it-service-management" | "com.atlassian.servicedesk:simplified-it-service-management-basic" | "com.atlassian.servicedesk:simplified-it-service-management-operations" | "com.atlassian.servicedesk:simplified-internal-service-desk" | "com.atlassian.servicedesk:simplified-external-service-desk" | "com.atlassian.servicedesk:simplified-hr-service-desk" | "com.atlassian.servicedesk:simplified-facilities-service-desk" | "com.atlassian.servicedesk:simplified-legal-service-desk" | "com.atlassian.servicedesk:simplified-marketing-service-desk" | "com.atlassian.servicedesk:simplified-finance-service-desk" | "com.atlassian.servicedesk:simplified-analytics-service-desk" | "com.atlassian.servicedesk:simplified-design-service-desk" | "com.atlassian.servicedesk:simplified-sales-service-desk" | "com.atlassian.servicedesk:simplified-halp-service-desk" | "com.atlassian.servicedesk:next-gen-it-service-desk" | "com.atlassian.servicedesk:next-gen-hr-service-desk" | "com.atlassian.servicedesk:next-gen-legal-service-desk" | "com.atlassian.servicedesk:next-gen-marketing-service-desk" | "com.atlassian.servicedesk:next-gen-facilities-service-desk" | "com.atlassian.servicedesk:next-gen-analytics-service-desk" | "com.atlassian.servicedesk:next-gen-finance-service-desk" | "com.atlassian.servicedesk:next-gen-design-service-desk" | "com.atlassian.servicedesk:next-gen-sales-service-desk" | "com.atlassian.servicedesk:company-managed-blank-service-project" | "com.atlassian.servicedesk:company-managed-general-service-project" | "com.atlassian.servicedesk:team-managed-general-service-project" | "com.atlassian.jira-core-project-templates:jira-core-simplified-content-management" | "com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval" | "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking" | "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control" | "com.atlassian.jira-core-project-templates:jira-core-simplified-procurement" | "com.atlassian.jira-core-project-templates:jira-core-simplified-project-management" | "com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment" | "com.atlassian.jira-core-project-templates:jira-core-simplified-task-" | "com.atlassian.jcs:customer-service-management"), // A predefined configuration for a project. The type of the `projectTemplateKey` must match with the type of the `projectTypeKey`.
  "projectTypeKey": enum("software" | "service_desk" | "business"), // The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type.
  "url": string, // A link to information about this project, such as project documentation
  "workflowScheme": integer, // The ID of the workflow scheme for the project. Use the [Get all workflow schemes](#api-rest-api-3-workflowscheme-get) operation to get a list of workflow scheme IDs. If you specify the workflow scheme you cannot specify the project template key.
}
```
### Responses

#### 201 - Returned if the project is created.

Example (application/json):
```json
"{\"id\":10010,\"key\":\"EX\",\"self\":\"https://your-domain.atlassian.net/jira/rest/api/3/project/10042\"}"
```

#### 400 - Returned if the request is not valid and the project could not be created.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to create projects.

