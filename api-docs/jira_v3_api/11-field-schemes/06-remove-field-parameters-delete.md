# 06-Remove field parameters [DELETE]

`DELETE /rest/api/3/config/fieldschemes/fields/parameters`

Remove field association parameters overrides for work types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{}
```
### Responses

#### 200 - Returned if the removal was successful.

#### 204 - The request completed successfully. No additional content will be sent in the response.

Schema (application/json):
```json
any
```

#### 207 - Returned if the removal was partially successful.

Example (application/json):
```json
"{\"results\":[{\"error\":{\"code\":\"FIELD_IS_NOT_ASSOCIATED\",\"message\":\"The field 'customfield_10000' is not associated with the scheme '10000'.\"},\"fieldId\":\"customfield_10000\",\"schemeId\":10000,\"success\":false,\"workTypeIds\":[1,2]},{\"fieldId\":\"description\",\"schemeId\":10001,\"success\":true,\"workTypeIds\":[3]}]}"
```

#### 400 - Returned if the request is invalid. If request is malformed, returns a collection of errors. If request is well-formed but contains invalid scheme or project IDs, returns failure details.

Schema (application/json):
```json
{}
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

