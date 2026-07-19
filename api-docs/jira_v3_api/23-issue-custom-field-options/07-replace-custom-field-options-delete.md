# 07-Replace custom field options [DELETE]

`DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue`

Replaces the options of a custom field.

Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect or Forge apps.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `replaceWith` | `integer` | `query` | No | The ID of the option that will replace the currently selected option. |
| `jql` | `string` | `query` | No | A JQL query that specifies the issues to be updated. For example, *project=10000*. |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `optionId` | `integer` | `path` | Yes | The ID of the option to be deselected. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Responses

#### 303 - Returned if the long-running task to deselect the option is started.

Example (application/json):
```json
"{\"self\":\"https://your-domain.atlassian.net/rest/api/3/task/1\",\"id\":\"1\",\"description\":\"Remove option 1 from issues matched by '*', and replace with option 3\",\"status\":\"COMPLETE\",\"result\":{\"errors\":{\"errorMessages\":[\"Option 2 cannot be set on issue MKY-5 as it is not in the correct scope\"],\"errors\":{},\"httpStatusCode\":{\"empty\":false,\"present\":true}},\"modifiedIssues\":[10001,10010],\"unmodifiedIssues\":[10005]},\"elapsedRuntime\":42}"
```

#### 400 - Returned if the request is not valid.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Connect and Forge app users with Administer Jira global permission can override screen security.\"],\"errors\":{}}"
```

#### 404 - Returned if the field is not found or does not support options, or the options to be replaced are not found.

