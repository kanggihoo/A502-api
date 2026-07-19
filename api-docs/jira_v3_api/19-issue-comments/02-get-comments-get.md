# 02-Get comments [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/comment`

Returns all comments for an issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Comments are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field. Accepts *created* to sort comments by their created date. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"comments\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"body\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.\"}]}]},\"created\":\"2021-01-17T12:34:00.000+0000\",\"id\":\"10000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000\",\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"Administrators\",\"type\":\"role\",\"value\":\"Administrators\"}}],\"maxResults\":1,\"startAt\":0,\"total\":1}"
```

#### 400 - Returned if `orderBy` is set to a value other than *created*.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue is not found or the user does not have permission to view it.

