# 05-Update screen [PUT]

`PUT /rest/api/3/screens/{screenId}`

Updates a screen. Only screens used in classic projects can be updated.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the screen. The maximum length is 255 characters.
  "name": string, // The name of the screen. The name must be unique. The maximum length is 255 characters.
}
```
### Responses

#### 200 - Returned if the request is successful.

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

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage screens.\"],\"errors\":{}}"
```

#### 404 - Returned if the screen is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen was not found.\"],\"errors\":{}}"
```

