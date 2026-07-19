# 02-Add actors to project role [POST]

`POST /rest/api/3/project/{projectIdOrKey}/role/{id}`

Adds actors to a project role for the project.

To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-projectIdOrKey-role-id-put).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `id` | `integer` | `path` | Yes | The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs. |

### Request Body (application/json)

```json
{
  "group": [
    string
  ], // The name of the group to add. This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended.
  "groupId": [
    string
  ], // The ID of the group to add. This parameter cannot be used with the `group` parameter.
  "user": [
    string
  ], // The user account ID of the user to add.
}
```
### Responses

#### 200 - Returned if the request is successful. The complete list of actors for the project is returned.

For example, the cURL request above adds a group, *jira-developers*. For the response below to be returned as a result of that request, the user *Mia Krystof* would have previously been added as a `user` actor for this project.

Example (application/json):
```json
"{\"actors\":[{\"actorGroup\":{\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\",\"name\":\"jira-developers\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\",\"user\":\"jira-developers\"},{\"actorUser\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"displayName\":\"Mia Krystof\",\"id\":10241,\"type\":\"atlassian-user-role-actor\"}],\"description\":\"A project role that represents developers in a project\",\"id\":10360,\"name\":\"Developers\",\"scope\":{\"project\":{\"id\":\"10000\",\"key\":\"KEY\",\"name\":\"Next Gen Project\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\"}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing or if the calling user lacks administrative permissions for the project.

#### 404 - Returned if:

 *  the project is not found.
 *  the user or group is not found.
 *  the group or user is not active.

