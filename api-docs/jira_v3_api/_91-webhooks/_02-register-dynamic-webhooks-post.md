# 02-Register dynamic webhooks [POST]

`POST /rest/api/3/webhook`

Registers webhooks.

**NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

### Request Body (application/json)

```json
{
  "url": string (required), // The URL that specifies where to send the webhooks. This URL must use the same base URL as the Connect app. Only a single URL per app is allowed to be registered.
  "webhooks": [
    {
      "events": [
        enum("jira:issue_created" | "jira:issue_updated" | "jira:issue_deleted" | "comment_created" | "comment_updated" | "comment_deleted" | "issue_property_set" | "issue_property_deleted" | "sprint_created" | "sprint_updated" | "sprint_closed" | "sprint_deleted" | "sprint_started" | "jira:version_released" | "jira:version_unreleased" | "jira:version_created" | "jira:version_moved" | "jira:version_updated" | "jira:version_merged" | "jira:version_deleted")
      ] (required), // The Jira events that trigger the webhook.
      "fieldIdsFilter": [
        string
      ], // A list of field IDs. When the issue changelog contains any of the fields, the webhook `jira:issue_updated` is sent. If this parameter is not present, the app is notified about all field updates.
      "issuePropertyKeysFilter": [
        string
      ], // A list of issue property keys. A change of those issue properties triggers the `issue_property_set` or `issue_property_deleted` webhooks. If this parameter is not present, the app is notified about all issue property updates.
      "jqlFilter": string (required), // The JQL filter that specifies which issues the webhook is sent for. Only a subset of JQL can be used. The supported elements are:   *  Fields: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and `cf[id]`. For custom fields (`cf[id]`), only the epic label custom field is supported.".  *  Operators: `=`, `!=`, `IN`, and `NOT IN`.
    }
  ] (required), // A list of webhooks.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"webhookRegistrationResult\":[{\"createdWebhookId\":1000},{\"errors\":[\"The clause watchCount is unsupported\"]},{\"createdWebhookId\":1001}]}"
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

#### 403 - Returned if the caller isn't an app.

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

