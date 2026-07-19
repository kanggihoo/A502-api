# 02-Get the default data classification level of a project [GET]

`GET /rest/api/3/project/{projectIdOrKey}/classification-level/default`

Returns the default data classification for a project.

**[Permissions](#permissions) required:**

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case-sensitive). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"classification\":{\"id\":\"ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38\",\"status\":\"published\",\"name\":\"Restricted\",\"rank\":1,\"description\":\"Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled\",\"guideline\":\"Access to data must be restricted to only individuals who need access in order to perform their job duties.\",\"guidelineADF\":\"{\\\"version\\\":1,\\\"type\\\":\\\"doc\\\",\\\"content\\\":[{\\\"type\\\":\\\"paragraph\\\",\\\"content\\\":[{\\\"type\\\":\\\"text\\\",\\\"text\\\":\\\"Access to data must be restricted to only individuals who need access in order to perform their job duties.\\\"}]}]}\",\"color\":\"RED\"}}"
```

#### 401 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the project is not found.

