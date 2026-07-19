# 02-Register modules [POST]

`POST /rest/atlassian-connect/1/app/module/dynamic`

Registers a list of modules.

**[Permissions](#permissions) required:** Only Connect apps can make this request.

### Request Body (application/json)

```json
{
  "modules": [
    {}
  ] (required), // A list of app modules in the same format as the `modules` property in the [app descriptor](https://developer.atlassian.com/cloud/jira/platform/app-descriptor/).
}
```
### Responses

#### 200 - Returned if the request is successful.

#### 400 - Returned if:
* any of the provided modules is invalid. For example, required properties are missing.
* any of the modules conflict with registered dynamic modules or modules defined in the app descriptor. For example, there are duplicate keys.

Details of the issues encountered are included in the error message.

Example (application/json):
```json
{
  "message": "Installation failed. The app com.example.app.key has duplicate module keys: [module-key]. Please contact the app vendor."
}
```

#### 401 - Returned if the call is not from a Connect app.

Example (application/json):
```json
{
  "message": "The request is not from a Connect app."
}
```

