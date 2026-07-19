# 01-Get project's sender email [GET]

`GET /rest/api/3/project/{projectId}/email`

Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `integer` | `path` | Yes | The project ID. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"emailAddress\":\"jira@example.customdomain.com\",\"emailAddressStatus\":[\"Email address or domain not verified.\"]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to read project.

#### 404 - Returned if the project or project's sender email address is not found.

