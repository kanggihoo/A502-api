# 12-Update field configuration scheme [PUT]

`PUT /rest/api/3/fieldconfigurationscheme/{id}`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Updates a field configuration scheme.

This operation can only update field configuration schemes used in company-managed (classic) projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the field configuration scheme. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the field configuration scheme.
  "name": string (required), // The name of the field configuration scheme. The name must be unique.
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
"{\"errorMessages\":[\"A field configuration scheme is using this name.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access field configurations.\"],\"errors\":{}}"
```

#### 404 - Returned if the field configuration scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The field configuration scheme was not found.\"],\"errors\":{}}"
```

