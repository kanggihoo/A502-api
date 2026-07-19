# 05-Update remote issue link by ID [PUT]

`PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

Updates a remote issue link for an issue.

Note: Fields without values in the request are set to null.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `linkId` | `string` | `path` | Yes | The ID of the remote issue link. |

### Request Body (application/json)

```json
{
  "application": any, // Details of the remote application the linked item is in. For example, trello.
  "globalId": string, // An identifier for the remote item in the remote system. For example, the global ID for a remote item in Confluence would consist of the app ID and page ID, like this: `appId=456&pageId=123`.  Setting this field enables the remote issue link details to be updated or deleted using remote system and item details as the record identifier, rather than using the record's Jira ID.  The maximum length is 255 characters.
  "object": any (required), // Details of the item linked to.
  "relationship": string, // Description of the relationship between the issue and the linked item. If not set, the relationship description "links to" is used in Jira.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if:

 *  the link ID is invalid.
 *  the remote issue link does not belong to the issue.
 *  the request body is invalid.

Example (application/json):
```json
"{\"errorMessages\":[],\"errors\":{\"title\":\"'title' is required.\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to link issues.

#### 404 - Returned if the issue or remote issue link is not found or the user does not have permission to view the issue.

