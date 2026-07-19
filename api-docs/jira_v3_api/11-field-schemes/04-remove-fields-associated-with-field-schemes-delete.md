# 04-Remove fields associated with field schemes [DELETE]

`DELETE /rest/api/3/config/fieldschemes/fields`

Remove fields associated with field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{}
```
### Responses

#### 200 - Returned if the field association update was successful.

Example (application/json):
```json
"{\"results\":[{\"fieldId\":\"customfield_10000\",\"schemeId\":10000,\"success\":true},{\"fieldId\":\"customfield_10001\",\"schemeId\":10002,\"success\":true}]}"
```

#### 204 - The request completed successfully. No additional content will be sent in the response.

Schema (application/json):
```json
any
```

#### 207 - Returned if the field association update was partially successful.

Example (application/json):
```json
"{\"results\":[{\"fieldId\":\"customfield_10000\",\"schemeId\":10000,\"success\":true},{\"error\":\"Scheme 10001 doesn't exist\",\"fieldId\":\"customfield_10001\",\"schemeId\":10001,\"success\":false}]}"
```

#### 400 - Returned if the request is invalid. If request is malformed, returns a collection of errors. If request is well-formed but contains invalid scheme or field IDs, returns failure details.

Example (application/json):
```json
"{\"results\":[{\"error\":\"Scheme 99999 doesn't exist\",\"fieldId\":\"customfield_10000\",\"schemeId\":99999,\"success\":false},{\"error\":\"Field invalid_field doesn't exist\",\"fieldId\":\"invalid_field\",\"schemeId\":10001,\"success\":false}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
any
```

#### 403 - Returned if the user does not have the required permissions

Schema (application/json):
```json
any
```

