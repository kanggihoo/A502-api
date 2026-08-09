# 03-Get field auto complete suggestions [GET]

`GET /rest/api/3/jql/autocompletedata/suggestions`

Returns the JQL search auto complete suggestions for a field.

Suggestions can be obtained by providing:

 *  `fieldName` to get a list of all values for the field.
 *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
 *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
 *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldName` | `string` | `query` | No | The name of the field. |
| `fieldValue` | `string` | `query` | No | The partial field item name entered by the user. |
| `predicateName` | `string` | `query` | No | The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*. |
| `predicateValue` | `string` | `query` | No | The partial predicate item name entered by the user. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"results\":[{\"displayName\":\"<b>Ac</b>tiveObjects (AO)\",\"value\":\"ActiveObjects\"},{\"displayName\":\"Atlassian Connect (<b>AC</b>)\",\"value\":\"Atlassian Connect\"},{\"displayName\":\"Atlassian Connect in Jira (<b>AC</b>JIRA)\",\"value\":\"Atlassian Connect in Jira\"}]}"
```

#### 400 - Returned if an invalid combination of parameters is passed.

#### 401 - Returned if the authentication credentials are incorrect.

