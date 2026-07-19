# 03-Update screen scheme [PUT]

`PUT /rest/api/3/screenscheme/{screenSchemeId}`

Updates a screen scheme. Only screen schemes used in classic projects can be updated.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenSchemeId` | `string` | `path` | Yes | The ID of the screen scheme. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the screen scheme. The maximum length is 255 characters.
  "name": string, // The name of the screen scheme. The name must be unique. The maximum length is 255 characters.
  "screens": any, // The IDs of the screens for the screen types of the screen scheme. Only screens used in classic projects are accepted.
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
"{\"errorMessages\":[\"The name is used by another scheme.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the screen scheme or a screen used as one of the screen types is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen scheme was not found.\"],\"errors\":{}}"
```

