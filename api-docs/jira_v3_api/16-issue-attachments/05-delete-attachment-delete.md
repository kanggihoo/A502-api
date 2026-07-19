# 05-Delete attachment [DELETE]

`DELETE /rest/api/3/attachment/{id}`

Deletes an attachment from an issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the project holding the issue containing the attachment:

 *  *Delete own attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by the calling user.
 *  *Delete all attachments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by any user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the attachment. |

### Responses

#### 204 - Returned if the request is successful.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if:

 *  the attachment is not found.
 *  attachments are disabled in the Jira settings.

