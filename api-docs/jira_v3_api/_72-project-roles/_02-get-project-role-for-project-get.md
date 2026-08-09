# 02-Get project role for project [GET]

`GET /rest/api/3/project/{projectIdOrKey}/role/{id}`

Returns a project role's details and actors associated with the project. The list of actors is sorted by display name.

To check whether a user belongs to a role based on their group memberships, use [Get user](#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `id` | `integer` | `path` | Yes | The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs. |
| `excludeInactiveUsers` | `boolean` | `query` | No | Exclude inactive users. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"actors\":[{\"actorGroup\":{\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\",\"name\":\"jira-developers\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\",\"user\":\"jira-developers\"},{\"actorUser\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"displayName\":\"Mia Krystof\",\"id\":10241,\"type\":\"atlassian-user-role-actor\"}],\"description\":\"A project role that represents developers in a project\",\"id\":10360,\"name\":\"Developers\",\"scope\":{\"project\":{\"id\":\"10000\",\"key\":\"KEY\",\"name\":\"Next Gen Project\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\"}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the project or project role is not found.
 *  the user does not have administrative permission.

