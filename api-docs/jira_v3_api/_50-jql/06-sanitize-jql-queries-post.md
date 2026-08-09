# 06-Sanitize JQL queries [POST]

`POST /rest/api/3/jql/sanitize`

Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity.

For example, if the query contains the clause *project = 'Secret project'*, and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with *project = 12345"* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.

Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post).

Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "queries": [
    {
      "accountId": string, // The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
      "query": string (required), // The query to sanitize.
    }
  ] (required), // The list of JQL queries to sanitize. Must contain unique values. Maximum of 20 queries.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"queries\":[{\"initialQuery\":\"project = 'Sample project'\",\"sanitizedQuery\":\"project = 12345\"},{\"initialQuery\":\"project = 'Sample project'\",\"sanitizedQuery\":\"project = 'Sample project'\",\"accountId\":\"5b10ac8d82e05b22cc7d4ef5\"},{\"initialQuery\":\"project = 'Sample project'\",\"sanitizedQuery\":\"project = 12345\",\"accountId\":\"cda2aa1395ac195d951b3387\"},{\"initialQuery\":\"non-parsable query\",\"errors\":{\"errorMessages\":[\"Error in the JQL Query: Expecting operator but got 'query'. The valid operators are '=', '!=', '<', '>', '<=', '>=', '~', '!~', 'IN', 'NOT IN', 'IS' and 'IS NOT'. (line 1, character 9)\"],\"errors\":{}},\"accountId\":\"5b10ac8d82e05b22cc7d4ef5\"}]}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"The queries has to be provided.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

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

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"You are not authorized to perform this action. Administrator privileges are required.\"],\"errors\":{}}"
```

