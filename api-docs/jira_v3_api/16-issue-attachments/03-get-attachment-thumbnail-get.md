# 03-Get attachment thumbnail [GET]

`GET /rest/api/3/attachment/thumbnail/{id}`

Returns the thumbnail of an attachment.

To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-id-get).

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
| `fallbackToDefault` | `boolean` | `query` | No | Whether a default thumbnail is returned when the requested thumbnail is not found. |
| `width` | `integer` | `query` | No | The maximum width to scale the thumbnail to. |
| `height` | `integer` | `query` | No | The maximum height to scale the thumbnail to. |

### Responses

#### 200 - Returned if the request is successful when `redirect` is set to `false`.

#### 303 - Returned if the request is successful. See the `Location` header for the download URL.

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - The user does not have the necessary permission.

#### 404 - Returned if:

 *  the attachment is not found.
 *  attachments are disabled in the Jira settings.
 *  `fallbackToDefault` is `false` and the request thumbnail cannot be downloaded.

