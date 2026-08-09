# 05-Delete component [DELETE]

`DELETE /rest/api/3/component/{id}`

Deletes a component.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the component. |
| `moveIssuesTo` | `string` | `query` | No | The ID of the component to replace the deleted component. If this value is null no replacement is made. |

### Responses

#### 204 - Returned if the request is successful.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to manage the project containing the component or does not have permission to administer Jira.

#### 404 - Returned if:

 *  the component is not found.
 *  the replacement component is not found.
 *  the user does not have permission to browse the project containing the component.

