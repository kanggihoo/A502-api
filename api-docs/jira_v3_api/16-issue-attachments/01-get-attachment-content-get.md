# 01-Get attachment content [GET]

`GET /rest/api/3/attachment/content/{id}`

Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details.

To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-thumbnail-id-get).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the attachment. |
| `redirect` | `boolean` | `query` | No | Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to `false` to avoid making multiple requests to download the attachment. |

### Responses

#### 200 - Returned if the request is successful when `redirect` is set to `false`.

#### 206 - Returned if the request is successful when a `Range` header is provided and `redirect` is set to `false`.

#### 303 - Returned if the request is successful. See the `Location` header for the download URL.

#### 400 - Returned if the range supplied in the `Range` header is malformed.

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - The user does not have the necessary permission.

#### 404 - Returned if:

 *  the attachment is not found.
 *  attachments are disabled in the Jira settings.

#### 416 - Returned if the server is unable to satisfy the range of bytes provided.

