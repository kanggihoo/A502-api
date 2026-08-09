# 05-Convert user identifiers to account IDs in JQL queries [POST]

`POST /rest/api/3/jql/pdcleaner`

Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.

You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).

**[Permissions](#permissions) required:** Permission to access Jira.

### Request Body (application/json)

```json
{
  "queryStrings": [
    string
  ], // A list of queries with user identifiers. Maximum of 100 queries.
}
```
### Responses

#### 200 - Returned if the request is successful. Note that the JQL queries are returned in the same order that they were passed.

Example (application/json):
```json
"{\"queriesWithUnknownUsers\":[{\"convertedQuery\":\"assignee = unknown\",\"originalQuery\":\"assignee = mia\"}],\"queryStrings\":[\"issuetype = Bug AND assignee in (abcde-12345) AND reporter in (abc551-c4e99) order by lastViewed DESC\"]}"
```

#### 400 - Returned if at least one of the queries cannot be converted. For example, the JQL has invalid operators or invalid keywords, or the users in the query cannot be found.

Schema (application/json):
```json
string
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
string
```

