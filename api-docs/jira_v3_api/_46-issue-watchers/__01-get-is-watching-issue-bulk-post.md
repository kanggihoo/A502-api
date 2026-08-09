# 01-Get is watching issue bulk [POST]

`POST /rest/api/3/issue/watching`

Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is `false`.

This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "issueIds": [
    string
  ] (required), // The list of issue IDs.
}
```
### Responses

#### 200 - Returned if the request is successful

Example (application/json):
```json
"{\"issuesIsWatching\":{\"10001\":true,\"10002\":false,\"10005\":true}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

