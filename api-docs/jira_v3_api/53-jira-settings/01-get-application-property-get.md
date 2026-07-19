# 01-Get application property [GET]

`GET /rest/api/3/application-properties`

Returns all application properties or an application property.

If you specify a value for the `key` parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of editable properties.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `query` | No | The key of the application property. |
| `permissionLevel` | `string` | `query` | No | The permission level of all items being returned in the list. |
| `keyFilter` | `string` | `query` | No | When a `key` isn't provided, this filters the list of results by the application property `key` using a regular expression. For example, using `jira.lf.*` will return all application properties with keys that start with *jira.lf.*. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"defaultValue\":\"\",\"desc\":\"Jira home directory\",\"id\":\"jira.home\",\"key\":\"jira.home\",\"name\":\"jira.home\",\"type\":\"string\",\"value\":\"/var/jira/jira-home\"},{\"defaultValue\":\"CLONE -\",\"id\":\"jira.clone.prefix\",\"key\":\"jira.clone.prefix\",\"name\":\"The prefix added to the Summary field of cloned issues\",\"type\":\"string\",\"value\":\"CLONE -\"}]"
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

#### 404 - Returned if the application property is not found or the user does not have permission to view it.

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

