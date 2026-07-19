# 06-Update project [PUT]

`PUT /rest/api/3/project/{projectIdOrKey}`

Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project.

All parameters are optional in the body of the request. Schemes will only be updated if they are included in the request, any omitted schemes will be left unchanged.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). is only needed when changing the schemes or project key. Otherwise you will only need *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:<br><br> *  `description` The project description.<br> *  `issueTypes` The issue types associated with the project.<br> *  `lead` The project lead.<br> *  `projectKeys` All project keys associated with the project. |

### Request Body (application/json)

```json
{
  "assigneeType": enum("PROJECT_LEAD" | "UNASSIGNED"), // The default assignee when creating issues for this project.
  "avatarId": integer, // An integer value for the project's avatar.
  "categoryId": integer, // The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation. To remove the project category from the project, set the value to `-1.`
  "description": string, // A brief description of the project.
  "issueSecurityScheme": integer, // The ID of the issue security scheme for the project, which enables you to control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs.
  "key": string, // Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters.
  "lead": string, // This parameter is deprecated because of privacy changes. Use `leadAccountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Cannot be provided with `leadAccountId`.
  "leadAccountId": string, // The account ID of the project lead. Cannot be provided with `lead`.
  "name": string, // The name of the project.
  "notificationScheme": integer, // The ID of the notification scheme for the project. Use the [Get notification schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs.
  "permissionScheme": integer, // The ID of the permission scheme for the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs.
  "releasedProjectKeys": [
    string
  ], // Previous project keys to be released from the current project. Released keys must belong to the current project and not contain the current project key
  "url": string, // A link to information about this project, such as project documentation
}
```
### Responses

#### 200 - Returned if the project is updated.

Example (application/json):
```json
"{\"assigneeType\":\"PROJECT_LEAD\",\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"components\":[{\"ari\":\"ari:cloud:compass:fdb3fdec-4e70-be56-11ee-0242ac120002:component/fdb3fdec-4e70-11ee-be56-0242ac120002/fdb3fdec-11ee-4e70-be56-0242ac120002\",\"assignee\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"assigneeType\":\"PROJECT_LEAD\",\"description\":\"This is a Jira component\",\"id\":\"10000\",\"isAssigneeTypeValid\":false,\"lead\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"metadata\":{\"icon\":\"https://www.example.com/icon.png\"},\"name\":\"Component 1\",\"project\":\"HSP\",\"projectId\":10000,\"realAssignee\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"realAssigneeType\":\"PROJECT_LEAD\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/component/10000\"}],\"description\":\"This project was created as an example for REST.\",\"email\":\"from-jira@example.com\",\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"issueTypes\":[{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false},{\"avatarId\":10002,\"description\":\"A problem with the software.\",\"entityId\":\"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\\\",\",\"id\":\"1\",\"name\":\"Bug\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false}],\"key\":\"EX\",\"lead\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"properties\":{\"propertyKey\":\"propertyValue\"},\"roles\":{\"Developers\":\"https://your-domain.atlassian.net/rest/api/3/project/EX/role/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\",\"url\":\"https://www.example.com\",\"versions\":[]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if:

 *  the user does not have the necessary permission to update project details.
 *  the permission scheme is being changed and the Jira instance is Jira Core Free or Jira Software Free. Permission schemes cannot be changed on free plans.

#### 404 - Returned if the project is not found.

