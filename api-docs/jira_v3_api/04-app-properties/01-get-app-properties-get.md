# 01-Get app properties [GET]

`GET /rest/atlassian-connect/1/addons/{addonKey}/properties`

Gets all the properties of an app. The reserved key `connect_client_key_019cdff3-8bfb-71fe-9628-875b700aebb8` is not returned.

**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.
Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `addonKey` | `string` | `path` | Yes | The key of the app, as defined in its descriptor. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
{
  "keys": [
    {
      "self": "https://your-domain.atlassian.net/jira/rest/atlassian-connect/1/addon/example.app.key/properties/propertyKey",
      "key": "propertyKey"
    }
  ]
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

