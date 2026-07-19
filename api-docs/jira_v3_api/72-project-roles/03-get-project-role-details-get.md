# 03-Get project role details [GET]

`GET /rest/api/3/project/{projectIdOrKey}/roledetails`

Returns all [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) and the details for each role. Note that the list of project roles is common to all projects.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `currentMember` | `boolean` | `query` | No | Whether the roles should be filtered to include only those the user is assigned to. |
| `excludeConnectAddons` | `boolean` | `query` | No |  |
| `excludeOtherServiceRoles` | `boolean` | `query` | No | Do not return the default JSM company-managed space from CSM spaces, or the default CSM roles from JSM spaces. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\",\"name\":\"Developers\",\"id\":10360,\"description\":\"A project role that represents developers in a project\",\"admin\":false,\"default\":true,\"roleConfigurable\":true,\"translatedName\":\"Developers\",\"type\":\"DEFAULT\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or if the user does not have the necessary permissions for the project.

