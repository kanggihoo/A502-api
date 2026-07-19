# 02-Get field reference data (POST) [POST]

`POST /rest/api/3/jql/autocompletedata`

Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.

This operation can filter the custom fields returned by project. Invalid project IDs in `projectIds` are ignored. System fields are always returned.

It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field `Component - Component[Dropdown]` enables dropdown fields `Component - cf[10061]` and `Component - cf[10062]` to be searched simultaneously.

**[Permissions](#permissions) required:** None.

### Request Body (application/json)

```json
{
  "includeCollapsedFields": boolean, // Include collapsed fields for fields that have non-unique names.
  "projectIds": [
    integer
  ], // List of project IDs used to filter the visible field details returned.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"jqlReservedWords\":[\"empty\",\"and\",\"or\",\"in\",\"distinct\"],\"visibleFieldNames\":[{\"displayName\":\"summary\",\"operators\":[\"~\",\"!~\",\"is\",\"is not\"],\"orderable\":\"true\",\"searchable\":\"true\",\"types\":[\"java.lang.String\"],\"value\":\"summary\"},{\"auto\":\"true\",\"cfid\":\"cf[10061]\",\"displayName\":\"Component - cf[10061]\",\"operators\":[\"=\",\"!=\",\"in\",\"not in\",\"is\",\"is not\"],\"orderable\":\"true\",\"types\":[\"com.atlassian.jira.issue.customfields.option.Option\"],\"value\":\"cf[10061]\"},{\"auto\":\"true\",\"cfid\":\"cf[10062]\",\"displayName\":\"Component - cf[10062]\",\"operators\":[\"=\",\"!=\",\"in\",\"not in\",\"is\",\"is not\"],\"orderable\":\"true\",\"types\":[\"com.atlassian.jira.issue.customfields.option.Option\"],\"value\":\"cf[10062]\"},{\"auto\":\"true\",\"displayName\":\"Component - Component[Dropdown]\",\"operators\":[\"=\",\"!=\",\"in\",\"not in\",\"is\",\"is not\"],\"searchable\":\"true\",\"types\":[\"com.atlassian.jira.issue.customfields.option.Option\"],\"value\":\"\\\"Component[Dropdown]\\\"\"}],\"visibleFunctionNames\":[{\"displayName\":\"standardIssueTypes()\",\"isList\":\"true\",\"types\":[\"com.atlassian.jira.issue.issuetype.IssueType\"],\"value\":\"standardIssueTypes()\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect.

