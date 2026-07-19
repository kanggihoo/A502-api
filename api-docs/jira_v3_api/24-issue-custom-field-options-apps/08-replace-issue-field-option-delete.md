# 08-Replace issue field option [DELETE]

`DELETE /rest/api/3/field/{fieldKey}/option/{optionId}/issue`

Deselects an issue-field select-list option from all issues where it is selected. A different option can be selected to replace the deselected option. The update can also be limited to a smaller set of issues by using a JQL query.

Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

This is an [asynchronous operation](#async). The response object contains a link to the long-running task.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `replaceWith` | `integer` | `query` | No | The ID of the option that will replace the currently selected option. |
| `jql` | `string` | `query` | No | A JQL query that specifies the issues to be updated. For example, *project=10000*. |
| `overrideScreenSecurity` | `boolean` | `query` | No | Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with admin permission. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). |
| `fieldKey` | `string` | `path` | Yes | The field key is specified in the following format: **$(app-key)\_\_$(field-key)**. For example, *example-add-on\_\_example-issue-field*. To determine the `fieldKey` value, do one of the following:<br><br> *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.<br> *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"` |
| `optionId` | `integer` | `path` | Yes | The ID of the option to be deselected. |

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

