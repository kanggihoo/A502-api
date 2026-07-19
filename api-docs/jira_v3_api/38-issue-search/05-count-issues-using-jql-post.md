# 05-Count issues using JQL [POST]

`POST /rest/api/3/search/approximate-count`

Provide an estimated count of the issues that match the [JQL](https://confluence.atlassian.com/x/egORLQ). Recent updates might not be immediately visible in the returned output. This endpoint requires JQL to be bounded.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "jql": string, // A [JQL](https://confluence.atlassian.com/x/egORLQ) expression. For performance reasons, this parameter requires a bounded query. A bounded query is a query with a search restriction.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"count\":153}"
```

#### 400 - Returned if the JQL query cannot be parsed.

#### 401 - Returned if the authentication credentials are incorrect.

