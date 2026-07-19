# 08-Create field configuration scheme [POST]

`POST /rest/api/3/fieldconfigurationscheme`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Creates a field configuration scheme.

This operation can only create field configuration schemes used in company-managed (classic) projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the field configuration scheme.
  "name": string (required), // The name of the field configuration scheme. The name must be unique.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"We can use this one for software projects.\",\"id\":\"10002\",\"name\":\"Field Configuration Scheme for software related projects\"}"
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

