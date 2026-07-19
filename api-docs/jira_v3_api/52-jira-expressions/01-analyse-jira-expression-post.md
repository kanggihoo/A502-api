# 01-Analyse Jira expression [POST]

`POST /rest/api/3/expression/analyse`

Analyses and validates Jira expressions.

As an experimental feature, this operation can also attempt to type-check the expressions.

Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

**[Permissions](#permissions) required**: None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `check` | `string` | `query` | No | The check to perform:<br><br> *  `syntax` Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length.<br> *  `type` EXPERIMENTAL. Each expression is type checked and the final type of the expression inferred. Any type errors that would result in the expression failure at runtime are reported. For example, accessing properties that don't exist or passing the wrong number of arguments to functions. Also performs the syntax check.<br> *  `complexity` EXPERIMENTAL. Determines the formulae for how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) each expression may execute. |

### Request Body (application/json)

```json
{
  "contextVariables": {}, // Context variables and their types. The type checker assumes that [common context variables](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#context-variables), such as `issue` or `project`, are available in context and sets their type. Use this property to override the default types or provide details of new variables.
  "expressions": [
    string
  ] (required), // The list of Jira expressions to analyse.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"results\":[{\"expression\":\"analysed expression\",\"errors\":[{\"line\":1,\"column\":4,\"message\":\"!, -, typeof, (, IDENTIFIER, null, true, false, NUMBER, STRING, TEMPLATE_LITERAL, new, [ or { expected, > encountered.\",\"type\":\"syntax\"},{\"message\":\"Jira expression is too long (1040), limit: 1000 characters\",\"type\":\"other\"},{\"message\":\"Jira expression has too many nodes (150), limit: 100 leaves\",\"type\":\"other\"}],\"valid\":false},{\"expression\":\"issues.map(i => {idAndKey: [i.id, i.key], summary: i.summary, comments: i.comments})\",\"valid\":true,\"type\":\"List<{idAndKey: [Number, String], summary: String, comments: List<Comment>}>\",\"complexity\":{\"expensiveOperations\":\"N\",\"variables\":{\"N\":\"issues\"}}},{\"expression\":\"issues.map(i => i.id > '0')\",\"errors\":[{\"expression\":\"i.id > 0\",\"message\":\"Can't compare Number to String.\",\"type\":\"type\"}],\"valid\":false,\"type\":\"TypeError\"}]}"
```

#### 400 - 400 response

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - 404 response

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

