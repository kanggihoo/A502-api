# 04-Get default actors for project role [GET]

`GET /rest/api/3/role/{id}/actors`

Returns the [default actors](#api-rest-api-3-resolution-get) for the project role.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs. |

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

