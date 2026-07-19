# 02-Create screen scheme [POST]

`POST /rest/api/3/screenscheme`

Creates a screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the screen scheme. The maximum length is 255 characters.
  "name": string (required), // The name of the screen scheme. The name must be unique. The maximum length is 255 characters.
  "screens": any (required), // The IDs of the screens for the screen types of the screen scheme. Only screens used in classic projects are accepted.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":10001}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is used by another scheme.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if a screen used as one of the screen types in the screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"One or more screens assigned to screen types was not found.\"],\"errors\":{}}"
```

