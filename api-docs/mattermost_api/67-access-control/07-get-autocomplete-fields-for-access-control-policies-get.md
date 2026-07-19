# 07-Get autocomplete fields for access control policies [GET]

`GET /api/v4/access_control_policies/cel/autocomplete/fields`

Provides a list of fields that can be used for autocompletion when creating/editing access control policy expressions.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `after` | `string` | `query` | No | The field ID to start after for pagination. |
| `limit` | `integer` | `query` | Yes | The maximum number of fields to return. |

### Responses

#### 200 - Autocomplete fields retrieved successfully.

Schema (application/json):
```json
{
  "fields": [
    {
      "name": string, // The name of the field.
      "description": string, // A description of the field.
    }
  ],
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

