# 14-Remove custom field context from projects [POST]

`POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove`

Removes a custom field context from projects.

A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects.

If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Request Body (application/json)

```json
{
  "projectIds": [
    string
  ] (required), // The IDs of projects.
}
```
### Responses

#### 204 - Returned if the custom field context is removed from the projects.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The projectIds must not contain duplicates.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field, context, or one or more projects are not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The context was not found.\"],\"errors\":{}}"
```

