# 02-Update announcement banner configuration [PUT]

`PUT /rest/api/3/announcementBanner`

Updates the announcement banner configuration.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "isDismissible": boolean, // Flag indicating if the announcement banner can be dismissed by the user.
  "isEnabled": boolean, // Flag indicating if the announcement banner is enabled or not.
  "message": string, // The text on the announcement banner.
  "visibility": string, // Visibility of the announcement banner. Can be public or private.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if an invalid parameter is passed.

Example (application/json):
```json
"\"Banner message cannot be null.\""
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"\"Only admins can update banner configuration.\""
```

