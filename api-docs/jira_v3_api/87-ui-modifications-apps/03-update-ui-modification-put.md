# 03-Update UI modification [PUT]

`PUT /rest/api/3/uiModifications/{uiModificationId}`

Updates a UI modification. UI modification can only be updated by Forge apps.

Each UI modification can define up to 1000 contexts. The same context can be assigned to maximum 100 UI modifications.

**Context types:**

 *  **Jira contexts:** For Jira view types, use `projectId` and `issueTypeId`. One field can act as a wildcard. Supported Jira views:
    
     *  `GIC` \- Jira global issue create
     *  `IssueView` \- Jira issue view
     *  `IssueTransition` \- Jira issue transition
 *  **Jira Service Management contexts:** For Jira Service Management view types, use `portalId` and `requestTypeId`. Wildcards are not supported. Supported JSM views:
    
     *  `JSMRequestCreate` \- Jira Service Management request create portal view

**[Permissions](#permissions) required:**

 *  *None* if the UI modification is created without contexts.
 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `uiModificationId` | `string` | `path` | Yes | The ID of the UI modification. |

### Request Body (application/json)

```json
{
  "contexts": [
    {
      "id": string, // The ID of the UI modification context.
      "isAvailable": boolean, // Whether a context is available. For example, when a project is deleted the context becomes unavailable.
      "issueTypeId": string, // The issue type ID of the context. Null is treated as a wildcard, meaning the UI modification will be applied to all issue types. Each UI modification context can have a maximum of one wildcard.
      "portalId": string, // The portal ID of the context. Only required for Jira Service Management request create portal view (`JSMRequestCreate`).
      "projectId": string, // The project ID of the context. Null is treated as a wildcard, meaning the UI modification will be applied to all projects. Each UI modification context can have a maximum of one wildcard.
      "requestTypeId": string, // The request type ID of the context. Only required for Jira Service Management request create portal view (`JSMRequestCreate`).
      "viewType": enum("GIC" | "IssueView" | "IssueTransition" | "JSMRequestCreate"), // The view type of the context.   Supported values:   *  `GIC` \- Jira global issue create  *  `IssueView` \- Jira issue view  *  `IssueTransition` \- Jira issue transition  *  `JSMRequestCreate` \- Jira Service Management request create portal view  For Jira view types (`GIC`, `IssueView`, `IssueTransition`), null is treated as a wildcard, meaning the UI modification will be applied to all view types. Each Jira context can have a maximum of one wildcard.      Wildcards are not applicable for JSM contexts.
    }
  ], // List of contexts of the UI modification. The maximum number of contexts is 1000. If provided, replaces all existing contexts.
  "data": string, // The data of the UI modification. The maximum size of the data is 50000 characters.
  "description": string, // The description of the UI modification. The maximum length is 255 characters.
  "name": string, // The name of the UI modification. The maximum length is 255 characters.
}
```
### Responses

#### 204 - Returned if the UI modification is updated.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the request is not from a Forge app.

#### 404 - Returned if the UI modification, a project, issue type, portal, or request type in the context are not found.

Example (application/json):
```json
"{\"details\":{\"issueTypesNotFound\":{\"10001\":[\"10000\",\"10001\"]},\"projectNotFound\":[\"10000\"]},\"errorMessages\":[\"Project with ID '10000' was not found.\",\"Project with ID '10001'. The following issue types were not found: [10000, 10001]\"],\"errors\":{}}"
```

