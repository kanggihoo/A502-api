# 10-Bulk create workflows [POST]

`POST /rest/api/3/workflows/create`

Create workflows and related statuses.

**[Permissions](#permissions) required:**

 *  *Administer Jira* project permission to create all, including global-scoped, workflows
 *  *Administer projects* project permissions to create project-scoped workflows

### Request Body (application/json)

```json
{
  "scope": {
    "project": {
      "id": string (required), // The ID of the project.
    },
    "type": enum("PROJECT" | "GLOBAL"), // The scope of the workflow. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects.
  },
  "statuses": [
    {
      "description": string, // The description of the status.
      "id": string, // The ID of the status. When reusing an existing status, this field should be provided.
      "name": string (required), // The name of the status.
      "statusCategory": enum("TODO" | "IN_PROGRESS" | "DONE") (required), // The category of the status.
      "statusReference": string (required), // The reference of the status. If adding a new status to a team-managed workflow, this must be a UUID (for company-managed a UUID is not needed).
    }
  ], // The statuses to associate with the workflows.
  "workflows": [
    {
      "description": string, // The description of the workflow to create.
      "loopedTransitionContainerLayout": {
        "x": number, // The x axis location.
        "y": number, // The y axis location.
      },
      "name": string (required), // The name of the workflow to create.
      "startPointLayout": {
        "x": number, // The x axis location.
        "y": number, // The y axis location.
      },
      "statuses": [
        {
          "approvalConfiguration": {
            "active": enum("true" | "false") (required), // Whether the approval configuration is active.
            "conditionType": enum("number" | "percent" | "numberPerPrincipal") (required), // How the required approval count is calculated. It may be configured to require a specific number of approvals, or approval by a percentage of approvers. If the approvers source field is Approver groups, you can configure how many approvals per group are required for the request to be approved. The number will be the same across all groups.
            "conditionValue": string (required), // The number or percentage of approvals required for a request to be approved. If `conditionType` is `number`, the value must be 20 or less. If `conditionType` is `percent`, the value must be 100 or less.
            "exclude": [
              enum("assignee" | "reporter")
            ], // A list of roles that should be excluded as possible approvers.
            "fieldId": string (required), // The custom field ID of the "Approvers" or "Approver Groups" field.
            "prePopulatedFieldId": string, // The custom field ID of the field used to pre-populate the Approver field. Only supports the "Affected Services" field.
            "transitionApproved": string (required), // The numeric ID of the transition to be executed if the request is approved.
            "transitionRejected": string (required), // The numeric ID of the transition to be executed if the request is declined.
          },
          "layout": {
            "x": number, // The x axis location.
            "y": number, // The y axis location.
          },
          "properties": {} (required), // The properties for this status layout.
          "statusReference": string (required), // A unique ID which the status will use to refer to this layout configuration.
        }
      ] (required), // The statuses associated with this workflow.
      "transitions": [
        {
          "actions": [
            {
              "id": string, // The ID of the rule.
              "parameters": {}, // The parameters related to the rule.
              "ruleKey": string (required), // The rule key of the rule.
            }
          ], // The post-functions of the transition.
          "conditions": {
            "conditionGroups": [
              Ref(ConditionGroupUpdate) [recursive]
            ], // The nested conditions of the condition group.
            "conditions": [
              {
                "id": string, // The ID of the rule.
                "parameters": {}, // The parameters related to the rule.
                "ruleKey": string (required), // The rule key of the rule.
              }
            ], // The rules for this condition.
            "operation": enum("ANY" | "ALL") (required), // Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true.
          },
          "customIssueEventId": string, // The custom event ID of the transition.
          "description": string, // The description of the transition.
          "id": string, // The ID of the transition.
          "links": [
            {
              "fromPort": integer, // The port that the transition starts from.
              "fromStatusReference": string, // The status that the transition starts from.
              "toPort": integer, // The port that the transition goes to.
            }
          ], // The statuses the transition can start from, and the mapping of ports between the statuses.
          "name": string, // The name of the transition.
          "properties": {}, // The properties of the transition.
          "toStatusReference": string, // The status the transition goes to.
          "transitionScreen": {
            "id": string, // The ID of the rule.
            "parameters": {}, // The parameters related to the rule.
            "ruleKey": string (required), // The rule key of the rule.
          },
          "triggers": [
            {
              "id": string, // The ID of the trigger.
              "parameters": {} (required), // The parameters of the trigger.
              "ruleKey": string (required), // The rule key of the trigger.
            }
          ], // The triggers of the transition.
          "type": enum("INITIAL" | "GLOBAL" | "DIRECTED"), // The transition type.
          "validators": [
            {
              "id": string, // The ID of the rule.
              "parameters": {}, // The parameters related to the rule.
              "ruleKey": string (required), // The rule key of the rule.
            }
          ], // The validators of the transition.
        }
      ] (required), // The transitions of this workflow.
    }
  ], // The details of the workflows to create.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statuses\":[{\"description\":\"\",\"id\":\"10003\",\"name\":\"Done\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"DONE\",\"statusReference\":\"10003\"},{\"description\":\"\",\"id\":\"10001\",\"name\":\"To Do\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"TODO\",\"statusReference\":\"10001\"},{\"description\":\"\",\"id\":\"10002\",\"name\":\"In Progress\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"IN_PROGRESS\",\"statusReference\":\"10002\"}],\"workflows\":[{\"description\":\"\",\"id\":\"b9ff2384-d3b6-4d4e-9509-3ee19f607168\",\"isEditable\":true,\"name\":\"Software workflow 1\",\"scope\":{\"type\":\"GLOBAL\"},\"startPointLayout\":{\"x\":-100.00030899047852,\"y\":-153.00020599365234},\"statuses\":[{\"deprecated\":false,\"layout\":{\"x\":317.0000915527344,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10002\"},{\"deprecated\":false,\"layout\":{\"x\":508.000244140625,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10003\"},{\"deprecated\":false,\"layout\":{\"x\":114.99993896484375,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10001\"}],\"transitions\":[{\"actions\":[],\"description\":\"\",\"id\":\"11\",\"links\":[],\"name\":\"To Do\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"21\",\"links\":[],\"name\":\"In Progress\",\"properties\":{},\"toStatusReference\":\"10002\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"1\",\"links\":[],\"name\":\"Create\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"INITIAL\",\"validators\":[]},{\"actions\":[],\"description\":\"Move a work item from in progress to done\",\"id\":\"31\",\"links\":[{\"fromPort\":0,\"fromStatusReference\":\"10002\",\"toPort\":1}],\"name\":\"Done\",\"properties\":{},\"toStatusReference\":\"10003\",\"triggers\":[],\"type\":\"DIRECTED\",\"validators\":[]}],\"version\":{\"id\":\"f010ac1b-3dd3-43a3-aa66-0ee8a447f76e\",\"versionNumber\":0}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 409 - Returned if another workflow configuration update task is ongoing.

