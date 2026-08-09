# 06-Bulk create issue [POST]

`POST /rest/api/3/issue/bulk`

Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks. Transitions may be applied, to move the issues or subtasks to a workflow step other than the default start step, and issue properties set.

The content of each issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

Creating a subtask differs from creating an issue as follows:

 *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types).
 *  `parent` the must contain the ID or key of the parent issue.

**[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or subtask is created.

### Request Body (application/json)

```json
{
  "issueUpdates": [
    {
      "fields": {}, // List of issue screen fields to update, specifying the sub-field to update and its value for each field. This field provides a straightforward option when setting a sub-field. When multiple sub-fields or other operations are required, use `update`. Fields included in here cannot be included in `update`.
      "historyMetadata": any, // Additional issue history details.
      "properties": [
        {
          "key": string, // The key of the property. Required on create and update.
          "value": any, // The value of the property. Required on create and update.
        }
      ], // Details of issue properties to be add or update.
      "transition": any, // Details of a transition. Required when performing a transition, optional when creating or editing an issue.
      "update": {}, // A Map containing the field field name and a list of operations to perform on the issue screen field. Note that fields included in here cannot be included in `fields`.
    }
  ],
}
```
### Responses

#### 201 - Returned if any of the issue or subtask creation requests were successful. A request may be unsuccessful when it:

 *  is missing required fields.
 *  contains invalid field values.
 *  contains fields that cannot be set for the issue type.
 *  is by a user who does not have the necessary permission.
 *  is to create a subtype in a project different that of the parent issue.
 *  is for a subtask when the option to create subtasks is disabled.
 *  is invalid for any other reason.

Example (application/json):
```json
"{\"issues\":[{\"id\":\"10000\",\"key\":\"ED-24\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10000\",\"transition\":{\"status\":200,\"errorCollection\":{\"errorMessages\":[],\"errors\":{}}}},{\"id\":\"10001\",\"key\":\"ED-25\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10001\"}],\"errors\":[]}"
```

#### 400 - Returned if all requests are invalid. Requests may be unsuccessful when they:

 *  are missing required fields.
 *  contain invalid field values.
 *  contain fields that cannot be set for the issue type.
 *  are by a user who does not have the necessary permission.
 *  are to create a subtype in a project different that of the parent issue.
 *  is for a subtask when the option to create subtasks is disabled.
 *  are invalid for any other reason.

Example (application/json):
```json
"{\"issues\":[],\"errors\":[{\"elementErrors\":{\"errorMessages\":[],\"errors\":{\"issuetype\":\"The issue type selected is invalid.\",\"project\":\"Sub-tasks must be created in the same project as the parent.\"}},\"failedElementNumber\":0,\"status\":400},{\"elementErrors\":{\"errorMessages\":[],\"errors\":{\"issuetype\":\"The issue type selected is invalid.\",\"project\":\"Sub-tasks must be created in the same project as the parent.\"}},\"failedElementNumber\":1,\"status\":400}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

