# 02-Bulk update entity properties [PUT]

`PUT /rest/atlassian-connect/1/migration/properties/{entityType}`

Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `Atlassian-Transfer-Id` | `string` | `header` | Yes | The app migration transfer ID. |
| `entityType` | `string` | `path` | Yes | The type indicating the object that contains the entity properties. |

### Request Body (application/json)

```json
[
  {
    "entityId": number (required), // The entity property ID.
    "key": string (required), // The entity property key.
    "value": string (required), // The new value of the entity property.
  }
]
```
### Responses

#### 200 - Returned if the request is successful.

#### 400 - Returned if the request is not valid.

#### 403 - Returned if the authorisation credentials are incorrect or missing.

