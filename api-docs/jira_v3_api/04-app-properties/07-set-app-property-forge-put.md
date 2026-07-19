# 07-Set app property (Forge) [PUT]

`PUT /rest/forge/1/app/properties/{propertyKey}`

Sets the value of a Forge app's property.
These values can be retrieved in [Jira expressions](/cloud/jira/platform/jira-expressions/)
through the `app` [context variable](/cloud/jira/platform/jira-expressions/#context-variables).
They are also available in [entity property display conditions](/platform/forge/manifest-reference/display-conditions/entity-property-conditions/).

For other use cases, use the [Storage API](/platform/forge/runtime-reference/storage-api/).

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** Only Forge apps can make this request. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestjira/#method-signature)** requests from Forge.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Request Body (application/json)

```json
any
```
### Responses

#### 200 - Returned if the property is updated.

Example (application/json):
```json
{
  "message": "Property updated.",
  "statusCode": 200
}
```

#### 201 - Returned is the property is created.

Example (application/json):
```json
{
  "message": "Property created.",
  "statusCode": 201
}
```

#### 400 - Returned if:
  * the property key is longer than 127 characters.
  * the value isn't valid JSON.
  * the value is longer than 32768 characters.

Example (application/json):
```json
{
  "message": "The property key can't be longer than 127 characters.",
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

