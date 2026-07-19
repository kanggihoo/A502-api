# 05-Get app property keys (Forge) [GET]

`GET /rest/forge/1/app/properties`

Returns all property keys for the Forge app.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
{
  "keys": [
    {
      "key": "key1",
      "self": "https://your-domain.atlassian.net/rest/forge/1/app/properties/key1"
    },
    {
      "key": "key2",
      "self": "https://your-domain.atlassian.net/rest/forge/1/app/properties/key2"
    }
  ]
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

