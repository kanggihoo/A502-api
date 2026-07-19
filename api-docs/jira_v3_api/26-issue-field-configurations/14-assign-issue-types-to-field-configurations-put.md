# 14-Assign issue types to field configurations [PUT]

`PUT /rest/api/3/fieldconfigurationscheme/{id}/mapping`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Assigns issue types to field configurations on field configuration scheme.

This operation can only modify field configuration schemes used in company-managed (classic) projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the field configuration scheme. |

### Request Body (application/json)

```json
{
  "mappings": [
    {
      "fieldConfigurationId": string (required), // The ID of the field configuration.
      "issueTypeId": string (required), // The ID of the issue type or *default*. When set to *default* this field configuration issue type item applies to all issue types without a field configuration. An issue type can be included only once in a request.
    }
  ] (required), // Field configuration to issue type mappings.
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

#### 404 - Returned if the field configuration scheme, the field configuration, or the issue type is not found.

