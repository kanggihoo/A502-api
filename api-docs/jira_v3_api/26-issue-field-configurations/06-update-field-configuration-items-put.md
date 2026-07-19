# 06-Update field configuration items [PUT]

`PUT /rest/api/3/fieldconfiguration/{id}/fields`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Updates fields in a field configuration. The properties of the field configuration fields provided override the existing values.

This operation can only update field configurations used in company-managed (classic) projects.

The operation can set the renderer for text fields to the default text renderer (`text-renderer`) or wiki style renderer (`wiki-renderer`). However, the renderer cannot be updated for fields using the autocomplete renderer (`autocomplete-renderer`).

Hiding a field deletes it from the field configuration - deleting the required, description and renderer type values as well. As a result, hiding and unhiding will not restore the other values but use their default values.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the field configuration. |

### Request Body (application/json)

```json
{
  "fieldConfigurationItems": [
    {
      "description": string, // The description of the field within the field configuration.
      "id": string (required), // The ID of the field within the field configuration.
      "isHidden": boolean, // Whether the field is hidden in the field configuration.
      "isRequired": boolean, // Whether the field is required in the field configuration.
      "renderer": string, // The renderer type for the field within the field configuration.
    }
  ] (required), // Details of fields in a field configuration.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the field configuration is not found.

