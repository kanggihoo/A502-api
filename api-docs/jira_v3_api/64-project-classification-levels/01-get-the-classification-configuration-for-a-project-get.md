# 01-Get the classification configuration for a project [GET]

`GET /rest/api/3/project/{projectIdOrKey}/classification-config`

Returns the consolidated classification configuration for a project's admin settings page.

This includes permitted classification levels (with status), the project's default classification level, the organization's default classification level, and the container override setting.

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
"{\"classificationLevels\":[{\"id\":\"ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38\",\"status\":\"published\",\"name\":\"Restricted\",\"rank\":1,\"description\":\"Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled\",\"guideline\":\"Access to data must be restricted to only individuals who need access in order to perform their job duties.\",\"color\":\"RED\"}],\"containerOverride\":\"ANY\",\"defaultClassificationLevel\":{\"id\":\"ari:cloud:platform::classification-tag/5bfa70f7-4af1-44f5-9e12-1ce185f15a38\",\"status\":\"published\",\"name\":\"Restricted\",\"rank\":1,\"description\":\"Data we hold that would be very damaging and would cause loss of trust with customers and present legal risk if mishandled\",\"guideline\":\"Access to data must be restricted to only individuals who need access in order to perform their job duties.\",\"color\":\"RED\"},\"organizationClassificationLevel\":{\"id\":\"ari:cloud:platform::classification-tag/a82d653e-1035-4aa2-b9de-4265511fd487\",\"status\":\"published\",\"name\":\"Confidential\",\"rank\":2,\"description\":\"Data we hold that would likely be damaging and could cause loss of trust with our customers if mishandled\",\"guideline\":\"Data should be encrypted at rest and in transit.\",\"color\":\"BLUE\"}}"
```

#### 401 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the project is not found or the feature is disabled.

