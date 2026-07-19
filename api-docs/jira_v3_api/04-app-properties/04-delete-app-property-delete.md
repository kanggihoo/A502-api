# 04-Delete app property [DELETE]

`DELETE /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

Deletes an app's property.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `addonKey` | `string` | `path` | Yes | The key of the app, as defined in its descriptor. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the property key is longer than 127 characters.

Example (application/json):
```json
{
  "message": "The property key cannot be longer than 127 characters.",
  "statusCode": 400
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Example (application/json):
```json
{
  "message": "Access to this resource must be authenticated as an app.",
  "statusCode": 401
}
```

#### 403 - Returned if the property key is reserved and read-only.

Example (application/json):
```json
{
  "message": "The property key is reserved and cannot be deleted.",
  "statusCode": 403
}
```

#### 404 - Returned if the property is not found or doesn't belong to the app.

Example (application/json):
```json
{
  "message": "Property with key not found.",
  "statusCode": 404
}
```

