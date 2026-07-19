# 04-Create custom field options (context) [POST]

`POST /rest/api/3/field/{fieldId}/context/{contextId}/option`

Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.

The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.

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
  "options": [
    {
      "disabled": boolean, // Whether the option is disabled.
      "optionId": string, // For cascading options, the ID of a parent option.
      "value": string (required), // The value of the custom field option.
    }
  ], // Details of options to create.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"options\":[{\"disabled\":false,\"id\":\"10001\",\"value\":\"Scranton\"},{\"disabled\":true,\"id\":\"10002\",\"optionId\":\"10000\",\"value\":\"Manhattan\"},{\"disabled\":false,\"id\":\"10003\",\"value\":\"The Electric City\"}]}"
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

#### 404 - Returned if the custom field is not found or the context doesn't match the custom field.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

