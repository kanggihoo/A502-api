# 01-Get comments by IDs [POST]

`POST /rest/api/3/comment/list`

Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Comments are returned where the user:

 *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `renderedBody` Returns the comment body rendered in HTML.<br> *  `properties` Returns the comment's properties. |

### Request Body (application/json)

```json
{
  "ids": [
    integer
  ] (required), // The list of comment IDs. A maximum of 1000 IDs can be specified.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":1048576,\"startAt\":0,\"total\":1,\"values\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"body\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.\"}]}]},\"created\":\"2021-01-17T12:34:00.000+0000\",\"id\":\"10000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000\",\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"Administrators\",\"type\":\"role\",\"value\":\"Administrators\"}}]}"
```

#### 400 - Returned if the request contains more than 1000 IDs or is empty.

