# 04-Get visible issue field options [GET]

`GET /rest/api/3/field/{fieldKey}/option/suggestions/search`

Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed by the user.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `projectId` | `integer` | `query` | No | Filters the results to options that are only available in the specified project. |
| `fieldKey` | `string` | `path` | Yes | The field key is specified in the following format: **$(app-key)\_\_$(field-key)**. For example, *example-add-on\_\_example-issue-field*. To determine the `fieldKey` value, do one of the following:<br><br> *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.<br> *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"` |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":1,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/field/fieldKey/option/suggestions?startAt=1&maxResults=1\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/field/fieldKey/option/suggestions?startAt=0&maxResults=1\",\"startAt\":0,\"total\":10,\"values\":[{\"id\":1,\"value\":\"Team 1\",\"properties\":{\"leader\":{\"name\":\"Leader Name\",\"email\":\"lname@example.com\"},\"members\":42,\"description\":\"The team's description\",\"founded\":\"2016-06-06\"}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the field is not found or does not support options.

