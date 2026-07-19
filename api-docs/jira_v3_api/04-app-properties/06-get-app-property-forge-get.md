# 06-Get app property (Forge) [GET]

`GET /rest/forge/1/app/properties/{propertyKey}`

Returns the value of a Forge app's property.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
{
  "key": "property-key",
  "value": "property-value"
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

#### 403 - Returned if the request isn't made directly by an app or if it's an impersonated request.

Example (application/json):
```json
{
  "errorMessages": [
    "Access to this resource must be authenticated as an app."
  ]
}
```

#### 404 - Returned if the property isn't found or doesn't belong to the app.

Example (application/json):
```json
{
  "message": "Property with key not found.",
  "statusCode": 404
}
```

