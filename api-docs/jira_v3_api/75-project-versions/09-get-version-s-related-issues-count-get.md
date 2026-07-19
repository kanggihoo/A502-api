# 09-Get version's related issues count [GET]

`GET /rest/api/3/version/{id}/relatedIssueCounts`

Returns the following counts for a version:

 *  Number of issues where the `fixVersion` is set to the version.
 *  Number of issues where the `affectedVersion` is set to the version.
 *  Number of issues where a version custom field is set to the version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"customFieldUsage\":[{\"customFieldId\":10000,\"fieldName\":\"Field1\",\"issueCountWithVersionInCustomField\":2},{\"customFieldId\":10010,\"fieldName\":\"Field2\",\"issueCountWithVersionInCustomField\":3}],\"issueCountWithCustomFieldsShowingVersion\":54,\"issuesAffectedCount\":101,\"issuesFixedCount\":23,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if:

 *  the version is not found.
 *  the user does not have the required permissions.

