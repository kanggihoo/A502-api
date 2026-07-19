# 03-Update custom field configurations [PUT]

`PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration`

Update the configuration for contexts of a custom field of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field type.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldIdOrKey` | `string` | `path` | Yes | The ID or key of the custom field, for example `customfield_10000`. |

### Request Body (application/json)

```json
{
  "configurations": [
    {
      "configuration": any, // The field configuration.
      "fieldContextId": string (required), // The ID of the field context the configuration is associated with.
      "id": string (required), // The ID of the configuration.
      "schema": any, // The field value schema.
    }
  ] (required), // The list of custom field configuration details.
}
```
### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user is not a Jira admin or the request is not authenticated as from the app that provided the field.

#### 404 - Returned if the custom field is not found.

