# 01-Get workflow transition rule configurations [GET]

`GET /rest/api/3/workflow/rule/config`

Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:

 *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
 *  matching one or more transition rule keys.

Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.

Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `types` | `array` | `query` | Yes | The types of the transition rules to return. |
| `keys` | `array` | `query` | No | The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return. |
| `workflowNames` | `array` | `query` | No | The list of workflow names to filter by. |
| `withTags` | `array` | `query` | No | The list of `tags` to filter by. |
| `draft` | `boolean` | `query` | No | **Deprecated:** Whether draft or published workflows are returned. If not provided, both workflow types are returned. The 'draft' parameter will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":10,\"startAt\":0,\"total\":1,\"values\":[{\"workflowId\":{\"name\":\"My Workflow name\",\"draft\":false},\"postFunctions\":[{\"id\":\"b4d6cbdc-59f5-11e9-8647-d663bd873d93\",\"key\":\"postfunction-key\",\"configuration\":{\"value\":\"{ \\\"color\\\": \\\"red\\\" }\",\"disabled\":false,\"tag\":\"Sample tag\"},\"transition\":{\"id\":1,\"name\":\"Open\"}}],\"conditions\":[{\"id\":\"d663bd873d93-59f5-11e9-8647-b4d6cbdc\",\"key\":\"condition-key\",\"configuration\":{\"value\":\"{ \\\"size\\\": \\\"medium\\\" }\",\"disabled\":false,\"tag\":\"Another tag\"},\"transition\":{\"id\":1,\"name\":\"Open\"}}],\"validators\":[{\"id\":\"11e9-59f5-b4d6cbdc-8647-d663bd873d93\",\"key\":\"validator-key\",\"configuration\":{\"value\":\"\\\"{ \\\\\\\"shape\\\\\\\": \\\\\\\"square\\\\\\\" }\\\"\",\"disabled\":false},\"transition\":{\"id\":1,\"name\":\"Open\"}}]}]}"
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

#### 404 - Returned if any transition rule type is not supported.

#### 503 - Returned if we encounter a problem while trying to access the required data.

