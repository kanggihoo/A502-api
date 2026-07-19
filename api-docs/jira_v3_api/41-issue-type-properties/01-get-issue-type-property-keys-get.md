# 01-Get issue type property keys [GET]

`GET /rest/api/3/issuetype/{issueTypeId}/properties`

Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.
 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeId` | `string` | `path` | Yes | The ID of the issue type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"keys\":[{\"key\":\"issue.support\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support\"}]}"
```

#### 400 - Returned if the issue type ID is invalid.

#### 404 - Returned if:

 *  the issue type is not found.
 *  the user does not have the required permissions.

