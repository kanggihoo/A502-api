# 07-Get contents metadata for an expanded attachment [GET]

`GET /rest/api/3/attachment/{id}/expand/raw`

Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported.

Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** For the issue containing the attachment:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the attachment. |

### Responses

#### 200 - Returned if the request is successful. If an empty list is returned in the response, the attachment is empty, corrupt, or not an archive.

Example (application/json):
```json
"{\"entries\":[{\"entryIndex\":0,\"mediaType\":\"audio/mpeg\",\"name\":\"Allegro from Duet in C Major.mp3\",\"size\":1430174},{\"entryIndex\":1,\"mediaType\":\"text/rtf\",\"name\":\"lrm.rtf\",\"size\":331}],\"totalEntryCount\":24}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - The user does not have the necessary permission.

#### 404 - Returned if:

 *  the attachment is not found.
 *  attachments are disabled in the Jira settings.

#### 409 - Returned if the attachment is an archive, but not a supported archive format.

