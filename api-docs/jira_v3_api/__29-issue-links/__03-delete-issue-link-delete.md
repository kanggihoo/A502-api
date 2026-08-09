# 03-Delete issue link [DELETE]

`DELETE /rest/api/3/issueLink/{linkId}`

Deletes an issue link.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link.
 *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `linkId` | `string` | `path` | Yes | The ID of the issue link. |

### Responses

#### 200 - 200 response

#### 204 - Returned if the request is successful.

#### 400 - Returned if the issue link ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  issue linking is disabled.
 *  the issue link is not found.
 *  the user doesn't have the required permissions.

