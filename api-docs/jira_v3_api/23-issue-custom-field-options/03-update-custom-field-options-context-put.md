# 03-Update custom field options (context) [PUT]

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/option`

Updates the options of a custom field.

If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response.

Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Request Body (application/json)

```json
{
  "options": [
    {
      "disabled": boolean, // Whether the option is disabled.
      "id": string (required), // The ID of the custom field option.
      "value": string, // The value of the custom field option.
    }
  ], // Details of the options to update.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"options\":[{\"disabled\":false,\"id\":\"10001\",\"value\":\"Scranton\"},{\"disabled\":true,\"id\":\"10002\",\"value\":\"Manhattan\"},{\"disabled\":false,\"id\":\"10003\",\"value\":\"The Electric City\"}]}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field doesn't support options.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage custom field options.\"],\"errors\":{}}"
```

#### 404 - Returned if the field, context, or one or more options is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

