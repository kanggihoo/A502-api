# 02-Get Jira attachment settings [GET]

`GET /rest/api/3/attachment/meta`

Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed.

Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"enabled\":true,\"uploadLimit\":1000000}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

