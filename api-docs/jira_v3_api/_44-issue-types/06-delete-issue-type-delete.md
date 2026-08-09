# 06-Delete issue type [DELETE]

`DELETE /rest/api/3/issuetype/{id}`

Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (`alternativeIssueTypeId`). A list of alternative issue types are obtained from the [Get alternative issue types](#api-rest-api-3-issuetype-id-alternatives-get) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue type. |
| `alternativeIssueTypeId` | `string` | `query` | No | The ID of the replacement issue type. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if any issues cannot be updated with the alternative issue type.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if:

 *  the issue type is in use and an alternative issue type is not specified.
 *  the issue type or alternative issue type is not found.

#### 409 - Returned if the issue type is in use and:

 *  also specified as the alternative issue type.
 *  is a *standard* issue type and the alternative issue type is a *subtask*.

#### 423 - Returned if a resource related to deletion is locked.

