# 03-Delete workflow transition rule configurations [PUT]

`PUT /rest/api/3/workflow/rule/config/delete`

Deletes workflow transition rules from one or more workflows. These rule types are supported:

 *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
 *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
 *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

Only rules created by the calling Connect app can be deleted.

**Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

**[Permissions](#permissions) required:** Only Connect apps can use this operation.

### Request Body (application/json)

```json
{
  "workflows": [
    {
      "workflowId": {
        "draft": boolean, // **Deprecated:** Whether the workflow is in the draft state. The 'draft' parameter will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).
        "name": string (required), // The name of the workflow.
      } (required),
      "workflowRuleIds": [
        string
      ] (required), // The list of connect workflow rule IDs.
    }
  ] (required), // The list of workflows with transition rules to delete.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"updateResults\":[{\"workflowId\":{\"name\":\"Workflow with one rule not updated\",\"draft\":false},\"ruleUpdateErrors\":{\"example-rule-id\":[\"The rule with this id does not exist: example-rule-id\"]},\"updateErrors\":[]},{\"workflowId\":{\"name\":\"Workflow with all rules successfully updated\",\"draft\":true},\"ruleUpdateErrors\":{},\"updateErrors\":[]},{\"workflowId\":{\"name\":\"Non-existing workflow\",\"draft\":false},\"ruleUpdateErrors\":{},\"updateErrors\":[\"Workflow not found: WorkflowIdBean{name=Non-existing workflow, draft=false}\"]}]}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"Jira Administration permission is required to access workflow configuration.\"],\"errors\":{},\"httpStatusCode\":{\"empty\":false,\"present\":true}}"
```

#### 403 - Returned if the caller is not a Connect app.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

