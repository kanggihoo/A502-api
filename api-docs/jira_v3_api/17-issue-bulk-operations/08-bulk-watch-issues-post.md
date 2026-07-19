# 08-Bulk watch issues [POST]

`POST /rest/api/3/bulk/issues/watch`

Use this API to submit a bulk watch request. You can watch up to 1,000 issues in a single operation.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "selectedIssueIdsOrKeys": [
    string
  ] (required), // List of issue IDs or keys which are to be bulk watched or unwatched. These IDs or keys can be from different projects and issue types.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"taskId\":\"10641\"}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errors\":[{\"message\":\"Some of the issues in the issueIdsOrKeys are not valid\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

#### 403 - Returned if the user does not have the necessary permission.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

