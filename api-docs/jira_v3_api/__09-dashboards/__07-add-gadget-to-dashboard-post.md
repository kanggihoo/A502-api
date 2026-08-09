# 07-Add gadget to dashboard [POST]

`POST /rest/api/3/dashboard/{dashboardId}/gadget`

Adds a gadget to a dashboard.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardId` | `integer` | `path` | Yes | The ID of the dashboard. |

### Request Body (application/json)

```json
{
  "color": string, // The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`.
  "ignoreUriAndModuleKeyValidation": boolean, // Whether to ignore the validation of module key and URI. For example, when a gadget is created that is a part of an application that isn't installed.
  "moduleKey": string, // The module key of the gadget type. Can't be provided with `uri`.
  "position": any, // The position of the gadget. When the gadget is placed into the position, other gadgets in the same column are moved down to accommodate it.
  "title": string, // The title of the gadget.
  "uri": string, // The URI of the gadget type. Can't be provided with `moduleKey`.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"color\":\"blue\",\"id\":10001,\"moduleKey\":\"com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item\",\"position\":{\"column\":1,\"row\":0},\"title\":\"Issue statistics\"}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"Cannot add another gadget. The maximum number of gadgets the dashboard can hold has been reached.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the dashboard is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The dashboard you requested either does not exist or you don't have the required permissions to perform this action.\"],\"errors\":{}}"
```

