# 04-Get all project roles [GET]

`GET /rest/api/3/role`

Gets a list of all project roles, complete with project role details and default actors.

### About project roles ###

[Project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) are a flexible way to to associate users and groups with projects. In Jira Cloud, the list of project roles is shared globally with all projects, but each project can have a different set of actors associated with it (unlike groups, which have the same membership throughout all Jira applications).

Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and workflow conditions.

#### Members and actors ####

In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user associated with a project role.

Actors may be set as [default members](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/#Specifying-'default-members'-for-a-project-role) of the project role or set at the project level:

 *  Default actors: Users and groups that are assigned to the project role for all newly created projects. The default actors can be removed at the project level later if desired.
 *  Actors: Users and groups that are associated with a project role for a project, which may differ from the default actors. This enables you to assign a user to different roles in different projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"actors\":[{\"actorGroup\":{\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\",\"name\":\"jira-developers\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\",\"user\":\"jira-developers\"},{\"actorUser\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"displayName\":\"Mia Krystof\",\"id\":10241,\"type\":\"atlassian-user-role-actor\"}],\"description\":\"A project role that represents developers in a project\",\"id\":10360,\"name\":\"Developers\",\"scope\":{\"project\":{\"id\":\"10000\",\"key\":\"KEY\",\"name\":\"Next Gen Project\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have administrative permissions.

