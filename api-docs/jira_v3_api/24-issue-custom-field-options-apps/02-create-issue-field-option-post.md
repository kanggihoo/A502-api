# 02-Create issue field option [POST]

`POST /rest/api/3/field/{fieldKey}/option`

Creates an option for a select list issue field.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

Each field can have a maximum of 10000 options, and each option can have a maximum of 10000 scopes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldKey` | `string` | `path` | Yes | The field key is specified in the following format: **$(app-key)\_\_$(field-key)**. For example, *example-add-on\_\_example-issue-field*. To determine the `fieldKey` value, do one of the following:<br><br> *  open the app's plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.<br> *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"` |

### Request Body (application/json)

```json
{
  "config": {
    "attributes": [
      enum("notSelectable" | "defaultValue")
    ], // DEPRECATED
    "scope": any, // Defines the projects that the option is available in. If the scope is not defined, then the option is available in all projects.
  },
  "properties": {}, // The properties of the option as arbitrary key-value pairs. These properties can be searched using JQL, if the extractions (see https://developer.atlassian.com/cloud/jira/platform/modules/issue-field-option-property-index/) are defined in the descriptor for the issue field module.
  "value": string (required), // The option's name, which is displayed in Jira.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":1,\"value\":\"Team 1\",\"properties\":{\"leader\":{\"name\":\"Leader Name\",\"email\":\"lname@example.com\"},\"members\":42,\"description\":\"The team's description\",\"founded\":\"2016-06-06\"},\"config\":{\"scope\":{\"projects\":[],\"projects2\":[{\"id\":1001,\"attributes\":[\"notSelectable\"]},{\"id\":1002,\"attributes\":[\"notSelectable\"]}],\"global\":{}},\"attributes\":[]}}"
```

#### 400 - Returned if the option is invalid.

#### 403 - Returned if the request is not authenticated as a Jira administrator or the app that provided the field.

#### 404 - Returned if the field is not found or does not support options.

