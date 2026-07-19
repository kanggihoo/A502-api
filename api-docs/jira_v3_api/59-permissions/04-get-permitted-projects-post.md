# 04-Get permitted projects [POST]

`POST /rest/api/3/permissions/project`

Returns all the projects where the user is granted a list of project permissions.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Request Body (application/json)

```json
{
  "permissions": [
    string
  ] (required), // A list of permission keys.
}
```
### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "projects": [
    {
      "id": integer, // The ID of the project.
      "key": string, // The key of the project.
    }
  ], // A list of projects.
}
```

#### 400 - Returned if a project permission is not found.

#### 401 - Returned if the authentication credentials are incorrect or missing.

