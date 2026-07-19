# 01-Get dynamic webhooks for app [GET]

`GET /rest/api/3/webhook`

Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":3,\"startAt\":0,\"total\":3,\"values\":[{\"events\":[\"jira:issue_updated\",\"jira:issue_created\"],\"expirationDate\":\"2019-06-01T12:42:30.000+0000\",\"fieldIdsFilter\":[\"summary\",\"customfield_10029\"],\"id\":10000,\"jqlFilter\":\"project = PRJ\",\"url\":\"https://your-app.example.com/webhook-received\"},{\"events\":[\"jira:issue_created\"],\"expirationDate\":\"2019-06-01T12:42:30.000+0000\",\"id\":10001,\"jqlFilter\":\"issuetype = Bug\",\"url\":\"https://your-app.example.com/webhook-received\"},{\"events\":[\"issue_property_set\"],\"expirationDate\":\"2019-06-01T12:42:30.000+0000\",\"id\":10002,\"issuePropertyKeysFilter\":[\"my-issue-property-key\"],\"jqlFilter\":\"project = PRJ\",\"url\":\"https://your-app.example.com/webhook-received\"}]}"
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

