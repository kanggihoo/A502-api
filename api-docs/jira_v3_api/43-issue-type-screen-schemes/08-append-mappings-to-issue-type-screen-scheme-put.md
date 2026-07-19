# 08-Append mappings to issue type screen scheme [PUT]

`PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping`

Appends issue type to screen scheme mappings to an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeScreenSchemeId` | `string` | `path` | Yes | The ID of the issue type screen scheme. |

### Request Body (application/json)

```json
{
  "issueTypeMappings": [
    {
      "issueTypeId": string (required), // The ID of the issue type or *default*. Only issue types used in classic projects are accepted. An entry for *default* must be provided and defines the mapping for all issue types without a screen scheme.
      "screenSchemeId": string (required), // The ID of the screen scheme. Only screen schemes used in classic projects are accepted.
    }
  ] (required), // The list of issue type to screen scheme mappings. A *default* entry cannot be specified because a default entry is added when an issue type screen scheme is created.
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
"{\"errorMessages\":[\"A default mapping cannot be added.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

#### 404 - Returned if the issue type screen scheme, issue type, or screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

#### 409 - Returned if the issue type is a sub-task, but sub-tasks are disabled in Jira settings.

Example (application/json):
```json
"{\"errorMessages\":[\"Sub-tasks are disabled in Jira. At least one of the issue types is a sub-task.\"],\"errors\":{}}"
```

