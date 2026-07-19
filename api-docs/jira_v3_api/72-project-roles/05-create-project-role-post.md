# 05-Create project role [POST]

`POST /rest/api/3/role`

Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default actors to the project role after creating it.

*Note that although a new project role is available to all projects upon creation, any default actors that are associated with the project role are not added to projects that existed prior to the role being created.*<

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // A description of the project role. Required when fully updating a project role. Optional when creating or partially updating a project role.
  "name": string, // The name of the project role. Must be unique. Cannot begin or end with whitespace. The maximum length is 255 characters. Required when creating a project role. Optional when partially updating a project role.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"A project role that represents developers in a project\",\"id\":10360,\"name\":\"Developers\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\"}"
```

#### 400 - Returned if the request is not valid. The `name` cannot be empty or start or end with whitespace.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have administrative permissions.

#### 409 - Returned if a project role with the provided name already exists.

