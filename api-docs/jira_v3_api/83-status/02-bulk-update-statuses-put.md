# 02-Bulk update statuses [PUT]

`PUT /rest/api/3/statuses`

Updates statuses by ID.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Request Body (application/json)

```json
{
  "statuses": [
    {
      "description": string, // The description of the status.
      "id": string (required), // The ID of the status.
      "name": string (required), // The name of the status.
      "statusCategory": enum("TODO" | "IN_PROGRESS" | "DONE") (required), // The category of the status.
    }
  ] (required), // The list of statuses that will be updated.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is too long, maxSize=255\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 409 - Returned if another workflow configuration update task is ongoing.

