# 11-Add issue types to context [PUT]

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype`

Adds issue types to a custom field context, appending the issue types to the issue types list.

A custom field context without any issue types applies to all issue types. Adding issue types to such a custom field context would result in it applying to only the listed issue types.

If any of the issue types exists in the custom field context, the operation fails and no issue types are added.

This API will not allow adding issue types to the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Request Body (application/json)

```json
{
  "issueTypeIds": [
    string
  ] (required), // The list of issue type IDs.
}
```
### Responses

#### 204 - Returned if operation is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"These issue types are already associated with the context: 10001.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field, context, or one or more issue types are not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The context was not found.\"],\"errors\":{}}"
```

#### 409 - Returned if the issue type is a sub-task, but sub-tasks are disabled in Jira settings.

Example (application/json):
```json
"{\"errorMessages\":[\"Sub-tasks are disabled in Jira. At least one of the issue types is a sub-task.\"],\"errors\":{}}"
```

