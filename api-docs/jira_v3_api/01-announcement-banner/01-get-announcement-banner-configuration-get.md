# 01-Get announcement banner configuration [GET]

`GET /rest/api/3/announcementBanner`

Returns the current announcement banner configuration.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"hashId\":\"9HN2FJK9DM8BHRWERVW3RRTGDJ4G4D5C\",\"isDismissible\":false,\"isEnabled\":true,\"message\":\"This is a public, enabled, non-dismissible banner, set using the API\",\"visibility\":\"public\"}"
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
"\"Only admins can read banner configuration.\""
```

