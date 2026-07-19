# 02-Get bulk editable fields [GET]

`GET /rest/api/3/bulk/issues/fields`

Use this API to get a list of fields visible to the user to perform bulk edit operations. You can pass single or multiple issues in the query to get eligible editable fields. This API uses pagination to return responses, delivering 50 fields at a time.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  Depending on the field, any field-specific permissions required to edit it.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdsOrKeys` | `string` | `query` | Yes | The IDs or keys of the issues to get editable fields from. |
| `searchText` | `string` | `query` | No | (Optional)The text to search for in the editable fields. |
| `endingBefore` | `string` | `query` | No | (Optional)The end cursor for use in pagination. |
| `startingAfter` | `string` | `query` | No | (Optional)The start cursor for use in pagination. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"fields\":[{\"id\":\"assignee\",\"isRequired\":false,\"name\":\"Assignee\",\"searchUrl\":\"https://your-domain.atlassian.net/rest/api/3/user/assignable/multiProjectSearch?projectKeys=KAN&query=\",\"type\":\"assignee\"},{\"id\":\"components\",\"isRequired\":false,\"multiSelectFieldOptions\":[\"ADD\",\"REMOVE\",\"REPLACE\",\"REMOVE_ALL\"],\"name\":\"Components\",\"type\":\"components\",\"unavailableMessage\":\"{0}NOTE{1}: The project of the selected issue(s) does not have any components.\"},{\"fieldOptions\":[{\"description\":\"This problem will block progress.\",\"id\":\"1\",\"priority\":\"Highest\"},{\"description\":\"Has the potential to affect progress.\",\"id\":\"2\",\"priority\":\"Lowest\"},{\"description\":\"Trivial problem with little or no impact on progress.\",\"id\":\"3\",\"priority\":\"Medium\"}],\"id\":\"priority\",\"isRequired\":false,\"name\":\"Priority\",\"type\":\"priority\"}]}"
```

#### 400 - Returned if the request is not valid.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

#### 403 - Returned if the user does not have the necessary permission.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

#### 404 - Returned if no editable fields are found for the provided issue IDs.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

