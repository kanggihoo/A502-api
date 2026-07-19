# 02-Update workflow transition rule configurations [PUT]

`PUT /rest/api/3/workflow/rule/config`

Updates configuration of workflow transition rules. The following rule types are supported:

 *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
 *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
 *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

Only rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app can be updated.

To assist with app migration, this operation can be used to:

 *  Disable a rule.
 *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).

Rules are enabled if the `disabled` parameter is not provided.

**Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

### Request Body (application/json)

```json
{
  "workflows": [
    {
      "conditions": [
        {
          "configuration": {
            "disabled": boolean, // Whether the rule is disabled.
            "tag": string, // A tag used to filter rules in [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).
            "value": string (required), // Configuration of the rule, as it is stored by the Connect or the Forge app on the rule configuration page.
          } (required),
          "id": string (required), // The ID of the transition rule.
          "key": string (required), // The key of the rule, as defined in the Connect or the Forge app descriptor.
          "transition": any,
        }
      ], // The list of conditions within the workflow.
      "postFunctions": [
        {
          "configuration": {
            "disabled": boolean, // Whether the rule is disabled.
            "tag": string, // A tag used to filter rules in [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).
            "value": string (required), // Configuration of the rule, as it is stored by the Connect or the Forge app on the rule configuration page.
          } (required),
          "id": string (required), // The ID of the transition rule.
          "key": string (required), // The key of the rule, as defined in the Connect or the Forge app descriptor.
          "transition": any,
        }
      ], // The list of post functions within the workflow.
      "validators": [
        {
          "configuration": {
            "disabled": boolean, // Whether the rule is disabled.
            "tag": string, // A tag used to filter rules in [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).
            "value": string (required), // Configuration of the rule, as it is stored by the Connect or the Forge app on the rule configuration page.
          } (required),
          "id": string (required), // The ID of the transition rule.
          "key": string (required), // The key of the rule, as defined in the Connect or the Forge app descriptor.
          "transition": any,
        }
      ], // The list of validators within the workflow.
      "workflowId": {
        "draft": boolean, // **Deprecated:** Whether the workflow is in the draft state. The 'draft' parameter will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).
        "name": string (required), // The name of the workflow.
      } (required),
    }
  ] (required), // The list of workflows with transition rules to update.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"updateResults\":[{\"workflowId\":{\"name\":\"Workflow with one rule not updated\",\"draft\":false},\"ruleUpdateErrors\":{\"example-rule-id\":[\"The rule with this id does not exist: example-rule-id\"]},\"updateErrors\":[]},{\"workflowId\":{\"name\":\"Workflow with all rules successfully updated\",\"draft\":true},\"ruleUpdateErrors\":{},\"updateErrors\":[]},{\"workflowId\":{\"name\":\"Non-existing workflow\",\"draft\":false},\"ruleUpdateErrors\":{},\"updateErrors\":[\"Workflow not found: WorkflowIdBean{name=Non-existing workflow, draft=false}\"]}]}"
```

#### 400 - Returned if the request is invalid.

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

#### 403 - Returned if the caller is not a Connect or Forge app.

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

#### 503 - Returned if we encounter a problem while trying to access the required data.

