# 03-Get workflow transition rule configurations [POST]

`POST /rest/atlassian-connect/1/migration/workflow/rule/search`

Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `Atlassian-Transfer-Id` | `string` | `header` | Yes | The app migration transfer ID. |

### Request Body (application/json)

```json
{
  "expand": string, // Use expand to include additional information in the response. This parameter accepts `transition` which, for each rule, returns information about the transition the rule is assigned to.
  "ruleIds": [
    string
  ] (required), // The list of workflow rule IDs.
  "workflowEntityId": string (required), // The workflow ID.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
{
  "workflowEntityId": "a498d711-685d-428d-8c3e-bc03bb450ea7",
  "invalidRules": [
    "55d44f1d-c859-42e5-9c27-2c5ec3f340b1"
  ],
  "validRules": [
    {
      "workflowId": {
        "name": "Workflow name",
        "draft": true
      },
      "postFunctions": [
        {
          "id": "123",
          "key": "WorkflowKey",
          "configuration": {
            "value": "WorkflowValidator"
          },
          "transition": {
            "name": "transition",
            "id": 123
          }
        }
      ],
      "conditions": [
        {
          "id": "123",
          "key": "WorkflowKey",
          "configuration": {
            "value": "WorkflowValidator"
          },
          "transition": {
            "name": "transition",
            "id": 123
          }
        }
      ],
      "validators": [
        {
          "id": "123",
          "key": "WorkflowKey",
          "configuration": {
            "value": "WorkflowValidator"
          },
          "transition": {
            "name": "transition",
            "id": 123
          }
        }
      ]
    }
  ]
}
```

#### 400 - Returned if the request is not valid.

#### 403 - Returned if the authorisation credentials are incorrect or missing.

