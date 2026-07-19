# 05-Add default actors to project role [POST]

`POST /rest/api/3/role/{id}/actors`

Adds [default actors](#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request.

Changing a project role's default actors does not affect project role members for projects already created.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs. |

### Request Body (application/json)

```json
{
  "group": [
    string
  ], // The name of the group to add as a default actor. This parameter cannot be used with the `groupId` parameter. As a group's name can change,use of `groupId` is recommended. This parameter accepts a comma-separated list. For example, `"group":["project-admin", "jira-developers"]`.
  "groupId": [
    string
  ], // The ID of the group to add as a default actor. This parameter cannot be used with the `group` parameter This parameter accepts a comma-separated list. For example, `"groupId":["77f6ab39-e755-4570-a6ae-2d7a8df0bcb8", "0c011f85-69ed-49c4-a801-3b18d0f771bc"]`.
  "user": [
    string
  ], // The account IDs of the users to add as default actors. This parameter accepts a comma-separated list. For example, `"user":["5b10a2844c20165700ede21g", "5b109f2e9729b51b54dc274d"]`.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"actors\":[{\"actorGroup\":{\"name\":\"jira-developers\",\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\"}]}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have administrative permissions.

#### 404 - Returned if the project role is not found.

