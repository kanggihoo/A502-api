# 05-Reorder custom field options (context) [PUT]

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move`

Changes the order of custom field options or cascading options in a context.

This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Request Body (application/json)

```json
{
  "after": string, // The ID of the custom field option or cascading option to place the moved options after. Required if `position` isn't provided.
  "customFieldOptionIds": [
    string
  ] (required), // A list of IDs of custom field options to move. The order of the custom field option IDs in the list is the order they are given after the move. The list must contain custom field options or cascading options, but not both.
  "position": enum("First" | "Last"), // The position the custom field options should be moved to. Required if `after` isn't provided.
}
```
### Responses

#### 204 - Returned if options are reordered.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"'after' and 'position' were provided. Only 'after' or 'position' can be specified.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage custom field options.\"],\"errors\":{}}"
```

#### 404 - Returned if the field, the context, or one or more of the options is not found..

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

