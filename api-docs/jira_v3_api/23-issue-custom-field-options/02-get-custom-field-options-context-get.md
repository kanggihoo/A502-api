# 02-Get custom field options (context) [GET]

`GET /rest/api/3/field/{fieldId}/context/{contextId}/option`

Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |
| `optionId` | `integer` | `query` | No | The ID of the option. |
| `onlyOptions` | `boolean` | `query` | No | Whether only options are returned. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":4,\"values\":[{\"id\":\"10001\",\"value\":\"New York\"},{\"id\":\"10002\",\"value\":\"Boston\",\"disabled\":true},{\"id\":\"10004\",\"value\":\"Denver\"},{\"id\":\"10003\",\"value\":\"Brooklyn\",\"optionId\":\"10001\"}]}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field doesn't support options.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage custom field options.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field is not found or the context doesn't match the custom field.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

