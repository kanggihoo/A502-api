# 03-Create screen [POST]

`POST /rest/api/3/screens`

Creates a screen with a default field tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the screen. The maximum length is 255 characters.
  "name": string (required), // The name of the screen. The name must be unique. The maximum length is 255 characters.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":10005,\"name\":\"Resolve Security Issue Screen\",\"description\":\"Enables changes to resolution and linked issues.\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is used by another screen.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage screens.\"],\"errors\":{}}"
```

