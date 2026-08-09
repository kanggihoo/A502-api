# 05-Update version [PUT]

`PUT /rest/api/3/version/{id}`

Updates a project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |

### Request Body (application/json)

```json
{
  "approvers": [
    {
      "accountId": string, // The Atlassian account ID of the approver.
      "declineReason": string, // A description of why the user is declining the approval.
      "description": string, // A description of what the user is approving within the specified version.
      "status": string, // The status of the approval, which can be *PENDING*, *APPROVED*, or *DECLINED*
    }
  ], // If the expand option `approvers` is used, returns a list containing the approvers for this version.
  "archived": boolean, // Indicates that the version is archived. Optional when creating or updating a version.
  "description": string, // The description of the version. Optional when creating or updating a version. The maximum size is 16,384 bytes.
  "driver": string, // The Atlassian account ID of the version driver. Optional when creating or updating a version. If the expand option `driver` is used, returns the Atlassian account ID of the driver.
  "expand": string, // Use [expand](em>#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:   *  `operations` Returns the list of operations available for this version.  *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property contains a count of issues with a status other than *to do*, *in progress*, and *done*.  *  `driver` Returns the Atlassian account ID of the version driver.  *  `approvers` Returns a list containing approvers for this version.  Optional for create and update.
  "id": string, // The ID of the version.
  "issuesStatusForFixVersion": any, // If the expand option `issuesstatus` is used, returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property contains a count of issues with a status other than *to do*, *in progress*, and *done*.
  "moveUnfixedIssuesTo": string, // The URL of the self link to the version to which all unfixed issues are moved when a version is released. Not applicable when creating a version. Optional when updating a version.
  "name": string, // The unique name of the version. Required when creating a version. Optional when updating a version. The maximum length is 255 characters.
  "operations": [
    {
      "href": string,
      "iconClass": string,
      "id": string,
      "label": string,
      "styleClass": string,
      "title": string,
      "weight": integer,
    }
  ], // If the expand option `operations` is used, returns the list of operations available for this version.
  "overdue": boolean, // Indicates that the version is overdue.
  "project": string, // Deprecated. Use `projectId`.
  "projectId": integer, // The ID of the project to which this version is attached. Required when creating a version. Not applicable when updating a version.
  "releaseDate": string, // The release date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). Optional when creating or updating a version.
  "released": boolean, // Indicates that the version is released. If the version is released a request to release again is ignored. Not applicable when creating a version. Optional when updating a version.
  "self": string, // The URL of the version.
  "startDate": string, // The start date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). Optional when creating or updating a version.
  "userReleaseDate": string, // The date on which work on this version is expected to finish, expressed in the instance's *Day/Month/Year Format* date format.
  "userStartDate": string, // The date on which work on this version is expected to start, expressed in the instance's *Day/Month/Year Format* date format.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"archived\":false,\"description\":\"An excellent version\",\"id\":\"10000\",\"name\":\"New Version 1\",\"project\":\"PXA\",\"projectId\":10000,\"releaseDate\":\"2010-07-06\",\"released\":true,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\",\"userReleaseDate\":\"6/Jul/2010\"}"
```

#### 400 - Returned if:

 *  the request is invalid.
 *  the user does not have the required permissions.

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the version is not found.

