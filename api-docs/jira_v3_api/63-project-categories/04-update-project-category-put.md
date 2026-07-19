# 04-Update project category [PUT]

`PUT /rest/api/3/projectCategory/{id}`

Updates a project category.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "description": string, // The description of the project category.
  "id": string, // The ID of the project category.
  "name": string, // The name of the project category. Required on create, optional on update.
  "self": string, // The URL of the project category.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"Updated Project Category\",\"id\":\"10100\",\"name\":\"UPDATED\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10100\"}"
```

#### 400 - Returned if:

 *  `name` has been modified and exceeds 255 characters.
 *  `description` has been modified and exceeds 1000 characters.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the project category is not found.

