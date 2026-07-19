# 02-Create field configuration [POST]

`POST /rest/api/3/fieldconfiguration`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Creates a field configuration. The field configuration is created with the same field properties as the default configuration, with all the fields being optional.

This operation can only create configurations for use in company-managed (classic) projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the field configuration.
  "name": string (required), // The name of the field configuration. Must be unique.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"My field configuration description\",\"id\":10001,\"name\":\"My Field Configuration\"}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

