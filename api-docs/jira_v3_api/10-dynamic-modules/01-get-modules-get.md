# 01-Get modules [GET]

`GET /rest/atlassian-connect/1/app/module/dynamic`

Returns all modules registered dynamically by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "modules": [
    {}
  ] (required), // A list of app modules in the same format as the `modules` property in the [app descriptor](https://developer.atlassian.com/cloud/jira/platform/app-descriptor/).
}
```

#### 401 - Returned if the call is not from a Connect app.

Example (application/json):
```json
{
  "message": "The request is not from a Connect app."
}
```

