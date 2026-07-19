# 04-Get version [GET]

`GET /rest/api/3/version/{id}`

Returns a project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `operations` Returns the list of operations available for this version.<br> *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property represents the number of issues with a status other than *to do*, *in progress*, and *done*.<br> *  `driver` Returns the Atlassian account ID of the version driver.<br> *  `approvers` Returns a list containing the Atlassian account IDs of approvers for this version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"archived\":false,\"description\":\"An excellent version\",\"id\":\"10000\",\"name\":\"New Version 1\",\"overdue\":true,\"projectId\":10000,\"releaseDate\":\"2010-07-06\",\"released\":true,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\",\"userReleaseDate\":\"6/Jul/2010\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the version is not found or the user does not have the necessary permission.

