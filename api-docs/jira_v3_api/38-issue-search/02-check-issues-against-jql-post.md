# 02-Check issues against JQL [POST]

`POST /rest/api/3/jql/match`

Checks whether one or more issues would be returned by one or more JQL queries.

**[Permissions](#permissions) required:** None, however, issues are only matched against JQL queries where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "issueIds": [
    integer
  ] (required), // A list of issue IDs.
  "jqls": [
    string
  ] (required), // A list of JQL queries.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"matches\":[{\"matchedIssues\":[10000,10004],\"errors\":[]},{\"matchedIssues\":[100134,10025,10236],\"errors\":[]},{\"matchedIssues\":[],\"errors\":[]},{\"matchedIssues\":[],\"errors\":[\"Invalid JQL: broken = value\"]}]}"
```

#### 400 - Returned if `jqls` exceeds the maximum number of JQL queries or `issueIds` exceeds the maximum number of issue IDs.

