# 03-Bulk create statuses [POST]

`POST /rest/api/3/statuses`

Creates statuses for a global or project scope.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Request Body (application/json)

```json
{
  "scope": {
    "project": {
      "id": string (required), // The ID of the project.
    },
    "type": enum("PROJECT" | "GLOBAL") (required), // The scope of the status. `GLOBAL` for company-managed projects and `PROJECT` for team-managed projects.
  } (required),
  "statuses": [
    {
      "description": string, // The description of the status.
      "name": string (required), // The name of the status.
      "statusCategory": enum("TODO" | "IN_PROGRESS" | "DONE") (required), // The category of the status.
    }
  ] (required), // Details of the statuses being created.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"The issue is resolved\",\"id\":\"1000\",\"name\":\"Finished\",\"scope\":{\"project\":{\"id\":\"1\"},\"type\":\"PROJECT\"},\"statusCategory\":\"DONE\"}]"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is too long, maxSize=255\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 409 - Returned if another workflow configuration update task is ongoing.

