# 02-Create custom field context [POST]

`POST /rest/api/3/field/{fieldId}/context`

Creates a custom field context.

If `projectIds` is empty, a global context is created. A global context is one that applies to all project. If `issueTypeIds` is empty, the context applies to all issue types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the context.
  "id": string, // The ID of the context.
  "issueTypeIds": [
    string
  ], // The list of issue types IDs for the context. If the list is empty, the context refers to all issue types.
  "name": string (required), // The name of the context.
  "projectIds": [
    string
  ], // The list of project IDs associated with the context. If the list is empty, the context is global.
}
```
### Responses

#### 201 - Returned if the custom field context is created.

Example (application/json):
```json
"{\"id\":\"10025\",\"name\":\"Bug fields context\",\"description\":\"A context used to define the custom field options for bugs.\",\"projectIds\":[],\"issueTypeIds\":[\"10010\"]}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the field, project, or issue type is not found.

#### 409 - Returned if the issue type is a sub-task, but sub-tasks are disabled in Jira settings.

Example (application/json):
```json
"{\"errorMessages\":[\"Sub-tasks are disabled in Jira. At least one of the issue types is a sub-task.\"],\"errors\":{}}"
```

