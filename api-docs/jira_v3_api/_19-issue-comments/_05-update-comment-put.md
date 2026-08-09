# 05-Update comment [PUT]

`PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}`

Updates a comment.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any comment or *Edit own comments* to update comment created by the user.
 *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

**WARNING:** Child comments inherit visibility from their parent comment. Attempting to update a child comment's visibility will result in a 400 (Bad Request) error.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `id` | `string` | `path` | Yes | The ID of the comment. |
| `notifyUsers` | `boolean` | `query` | No | Whether users are notified when a comment is updated. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML. |

### Request Body (application/json)

```json
{
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
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"body\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.\"}]}]},\"created\":\"2021-01-17T12:34:00.000+0000\",\"id\":\"10000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000\",\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"Administrators\",\"type\":\"role\",\"value\":\"Administrators\"}}"
```

#### 400 - Returned if the user does not have permission to edit the comment or the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue or comment is not found or the user does not have permission to view the issue or comment.

