# 01-Create issue link [POST]

`POST /rest/api/3/issueLink`

Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked,
 *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue,
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Request Body (application/json)

```json
{
  "comment": {
    "author": any, // The ID of the user who created the comment.
    "body": any, // The comment text in [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/).
    "created": string, // The date and time at which the comment was created.
    "id": string, // The ID of the comment.
    "jsdAuthorCanSeeRequest": boolean, // Whether the comment was added from an email sent by a person who is not part of the issue. See [Allow external emails to be added as comments on issues](https://support.atlassian.com/jira-service-management-cloud/docs/allow-external-emails-to-be-added-as-comments-on-issues/)for information on setting up this feature.
    "jsdPublic": boolean, // Whether the comment is visible in Jira Service Desk. Defaults to true when comments are created in the Jira Cloud Platform. This includes when the site doesn't use Jira Service Desk or the project isn't a Jira Service Desk project and, therefore, there is no Jira Service Desk for the issue to be visible on. To create a comment with its visibility in Jira Service Desk set to false, use the Jira Service Desk REST API [Create request comment](https://developer.atlassian.com/cloud/jira/service-desk/rest/#api-rest-servicedeskapi-request-issueIdOrKey-comment-post) operation.
    "properties": [
      {
        "key": string, // The key of the property. Required on create and update.
        "value": any, // The value of the property. Required on create and update.
      }
    ], // A list of comment properties. Optional on create and update.
    "renderedBody": string, // The rendered version of the comment.
    "self": string, // The URL of the comment.
    "updateAuthor": any, // The ID of the user who updated the comment last.
    "updated": string, // The date and time at which the comment was updated last.
    "visibility": any, // The group or role to which this comment is visible. Optional on create and update.
  },
  "inwardIssue": {
    "fields": any, // The fields associated with the issue.
    "id": string, // The ID of an issue. Required if `key` isn't provided.
    "key": string, // The key of an issue. Required if `id` isn't provided.
    "self": string, // The URL of the issue.
  } (required),
  "outwardIssue": {
    "fields": any, // The fields associated with the issue.
    "id": string, // The ID of an issue. Required if `key` isn't provided.
    "key": string, // The key of an issue. Required if `id` isn't provided.
    "self": string, // The URL of the issue.
  } (required),
  "type": {
    "id": string, // The ID of the issue link type and is used as follows:   *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on create when `name` isn't provided. Otherwise, read only.  *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is read only.
    "inward": string, // The description of the issue link type inward link and is used as follows:   *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.  *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only.
    "name": string, // The name of the issue link type and is used as follows:   *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on create when `id` isn't provided. Otherwise, read only.  *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only.
    "outward": string, // The description of the issue link type outward link and is used as follows:   *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.  *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional on update. Otherwise, read only.
    "self": string, // The URL of the issue link type. Read only.
  } (required),
}
```
### Responses

#### 201 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the comment is not created. The response contains an error message indicating why the comment wasn't created. The issue link is also not created.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  issue linking is disabled.
 *  the user cannot view one or both of the issues. For example, the user doesn't have *Browse project* project permission for a project containing one of the issues.
 *  the user does not have *link issues* project permission.
 *  either of the link issues are not found.
 *  the issue link type is not found.

#### 413 - Returned if the per-issue limit for issue links has been breached.

