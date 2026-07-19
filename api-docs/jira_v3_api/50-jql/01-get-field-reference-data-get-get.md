# 01-Get field reference data (GET) [GET]

`GET /rest/api/3/jql/autocompletedata`

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"jqlReservedWords\":[\"empty\",\"and\",\"or\",\"in\",\"distinct\"],\"visibleFieldNames\":[{\"displayName\":\"summary\",\"operators\":[\"~\",\"!~\",\"is\",\"is not\"],\"orderable\":\"true\",\"searchable\":\"true\",\"types\":[\"java.lang.String\"],\"value\":\"summary\"},{\"auto\":\"true\",\"cfid\":\"cf[10880]\",\"displayName\":\"Sprint - cf[10880]\",\"operators\":[\"=\",\"!=\",\"in\",\"not in\",\"is\",\"is not\"],\"orderable\":\"true\",\"searchable\":\"true\",\"types\":[\"com.atlassian.greenhopper.service.sprint.Sprint\"],\"value\":\"Sprint\"}],\"visibleFunctionNames\":[{\"displayName\":\"standardIssueTypes()\",\"isList\":\"true\",\"types\":[\"com.atlassian.jira.issue.issuetype.IssueType\"],\"value\":\"standardIssueTypes()\"},{\"displayName\":\"issuesWithText()\",\"supportsListAndSingleValueOperators\":\"true\",\"types\":[\"com.atlassian.jira.issue.issuetype.IssueType\"],\"value\":\"issuesWithText()\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect.

