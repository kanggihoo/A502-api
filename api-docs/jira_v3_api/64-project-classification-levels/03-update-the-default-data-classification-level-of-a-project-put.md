# 03-Update the default data classification level of a project [PUT]

`PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default`

Updates the default data classification level for a project.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case-sensitive). |

### Request Body (application/json)

```json
{
  "id": string (required), // The ID of the project classification.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the project is not found.

