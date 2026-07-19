# 02-Create project category [POST]

`POST /rest/api/3/projectCategory`

Creates a project category.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"Created Project Category\",\"id\":\"10100\",\"name\":\"CREATED\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10100\"}"
```

#### 400 - Returned if:

 *  `name` is not provided or exceeds 255 characters.
 *  `description` exceeds 1000 characters.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 409 - Returned if the project category name is in use.

