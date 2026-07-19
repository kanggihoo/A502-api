# 03-Set app property [PUT]

`PUT /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}`

Sets the value of an app's property. Use this resource to store custom data for your app.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `addonKey` | `string` | `path` | Yes | The key of the app, as defined in its descriptor. |
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
  * the value is not valid JSON.
  * the value is longer than 32768 characters.

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
  "message": "The property key is reserved and cannot be created or updated.",
  "statusCode": 403
}
```

