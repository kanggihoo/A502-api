# 04-Parse JQL query [POST]

`POST /rest/api/3/jql/parse`

Parses and validates JQL queries.

Validation is performed in context of the current user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `validation` | `string` | `query` | Yes | How to validate the JQL query and treat the validation results. Validation options include:<br><br> *  `strict` Returns all errors. If validation fails, the query structure is not returned.<br> *  `warn` Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.<br> *  `none` No validation is performed. If JQL query is correctly formed, the query structure is returned. |

### Request Body (application/json)

```json
{
  "queries": [
    string
  ] (required), // A list of queries to parse.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"queries\":[{\"query\":\"summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER -5d ORDER BY updated DESC\",\"structure\":{\"orderBy\":{\"fields\":[{\"direction\":\"desc\",\"field\":{\"encodedName\":\"updated\",\"name\":\"updated\"}}]},\"where\":{\"clauses\":[{\"field\":{\"encodedName\":\"summary\",\"name\":\"summary\"},\"operand\":{\"encodedValue\":\"test\",\"value\":\"test\"},\"operator\":\"~\"},{\"clauses\":[{\"field\":{\"encodedName\":\"labels\",\"name\":\"labels\"},\"operand\":{\"encodedOperand\":\"urgent, blocker)\",\"values\":[{\"encodedValue\":\"urgent\",\"value\":\"urgent\"},{\"encodedValue\":\"blocker\",\"value\":\"blocker\"}]},\"operator\":\"in\"},{\"field\":{\"encodedName\":\"lastCommentedBy\",\"name\":\"lastCommentedBy\",\"property\":[{\"entity\":\"issue\",\"key\":\"propertyKey\",\"path\":\"path.in.property\",\"type\":\"user\"}]},\"operand\":{\"arguments\":[],\"encodedOperand\":\"currentUser()\",\"function\":\"currentUser\"},\"operator\":\"=\"}],\"operator\":\"or\"},{\"field\":{\"encodedName\":\"status\",\"name\":\"status\"},\"operator\":\"changed\",\"predicates\":[{\"operand\":{\"arguments\":[\"-1M\"],\"encodedOperand\":\"startOfMonth(-1M)\",\"function\":\"startOfMonth\"},\"operator\":\"after\"}]}],\"operator\":\"and\"}}},{\"query\":\"issue.property[\\\"spaces here\\\"].value in (\\\"Service requests\\\", Incidents)\",\"structure\":{\"where\":{\"field\":{\"encodedName\":\"issue.property[\\\"spaces here\\\"].value\",\"name\":\"issue.property[spaces here].value\",\"property\":[{\"entity\":\"issue\",\"key\":\"spaces here\",\"path\":\"value\"}]},\"operand\":{\"encodedOperand\":\"(\\\"Service requests\\\", Incidents)\",\"values\":[{\"encodedValue\":\"\\\"Service requests\\\"\",\"value\":\"Service requests\"},{\"encodedValue\":\"Incidents\",\"value\":\"Incidents\"}]},\"operator\":\"in\"}}},{\"errors\":[\"Error in the JQL Query: Expecting operator but got 'query'. The valid operators are '=', '!=', '<', '>', '<=', '>=', '~', '!~', 'IN', 'NOT IN', 'IS' and 'IS NOT'. (line 1, character 9)\"],\"query\":\"invalid query\"},{\"errors\":[\"The operator '=' is not supported by the 'summary' field.\"],\"query\":\"summary = test\"},{\"errors\":[\"Operator 'in' does not support the non-list value '\\\"test\\\"' for field 'summary'.\"],\"query\":\"summary in test\"},{\"query\":\"project = INVALID\",\"warnings\":[\"The value 'INVALID' does not exist for the field 'project'.\"]},{\"errors\":[\"Field 'universe' does not exist or you do not have permission to view it.\"],\"query\":\"universe = 42\"}]}"
```

#### 400 - Returned if the request is invalid.

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

#### 401 - Returned if the authentication credentials are incorrect.

