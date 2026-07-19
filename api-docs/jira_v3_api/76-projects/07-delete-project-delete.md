# 07-Delete project [DELETE]

`DELETE /rest/api/3/project/{projectIdOrKey}`

Deletes a project.

You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `enableUndo` | `boolean` | `query` | No | Whether this project is placed in the Jira recycle bin where it will be available for restoration. |

### Responses

#### 204 - Returned if the project is deleted.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have permission to delete it.

