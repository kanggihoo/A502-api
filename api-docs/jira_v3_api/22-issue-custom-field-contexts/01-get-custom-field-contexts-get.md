# 01-Get custom field contexts [GET]

`GET /rest/api/3/field/{fieldId}/context`

Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:

 *  With no other parameters set, all contexts.
 *  By defining `id` only, all contexts from the list of IDs.
 *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)
 *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `isAnyIssueType` | `boolean` | `query` | No | Whether to return contexts that apply to all issue types. |
| `isGlobalContext` | `boolean` | `query` | No | Whether to return contexts that apply to all projects. |
| `contextId` | `array` | `query` | No | The list of context IDs. To include multiple contexts, separate IDs with ampersand: `contextId=10000&contextId=10001`. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":2,\"values\":[{\"id\":\"10025\",\"name\":\"Bug fields context\",\"description\":\"A context used to define the custom field options for bugs.\",\"isGlobalContext\":true,\"isAnyIssueType\":false},{\"id\":\"10026\",\"name\":\"Task fields context\",\"description\":\"A context used to define the custom field options for tasks.\",\"isGlobalContext\":false,\"isAnyIssueType\":false}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field was not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

