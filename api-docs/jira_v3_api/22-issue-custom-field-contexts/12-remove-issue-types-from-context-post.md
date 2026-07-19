# 12-Remove issue types from context [POST]

`POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove`

Removes issue types from a custom field context.

A custom field context without any issue types applies to all issue types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Request Body (application/json)

```json
{
  "issueTypeIds": [
    string
  ] (required), // The list of issue type IDs.
}
```
### Responses

#### 204 - Returned if operation is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"These issue types are not associated with the context: 10002.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field, context, or one or more issue types are not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The context was not found.\"],\"errors\":{}}"
```

