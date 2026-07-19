# 02-Get app property [GET]

`GET /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

Returns the key and value of an app's property. The property key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8`
is reserved. It returns a synthetic, read-only property containing the Connect `clientKey` for the requested tenant.
This is intended for Forge apps with `app.connect.key` to retrieve the Connect client key during migration.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `addonKey` | `string` | `path` | Yes | The key of the app, as defined in its descriptor. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
{
  "self": "https://your-domain.atlassian.net/jira/rest/atlassian-connect/1/addon/example.app.key/properties/propertyKey",
  "key": "propertyKey",
  "value": "propertyValue"
}
```

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

#### 404 - Returned if the property is not found or doesn't belong to the app.

Example (application/json):
```json
{
  "message": "Property with key not found.",
  "statusCode": 404
}
```

