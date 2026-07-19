# 06-Get gadgets [GET]

`GET /rest/api/3/dashboard/{dashboardId}/gadget`

Returns a list of dashboard gadgets on a dashboard.

This operation returns:

 *  Gadgets from a list of IDs, when `id` is set.
 *  Gadgets with a module key, when `moduleKey` is set.
 *  Gadgets from a list of URIs, when `uri` is set.
 *  All gadgets, when no other parameters are set.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardId` | `integer` | `path` | Yes | The ID of the dashboard. |
| `moduleKey` | `array` | `query` | No | The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: `moduleKey=key:one&moduleKey=key:two`. |
| `uri` | `array` | `query` | No | The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: `uri=/rest/example/uri/1&uri=/rest/example/uri/2`. |
| `gadgetId` | `array` | `query` | No | The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: `gadgetId=10000&gadgetId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"gadgets\":[{\"id\":10001,\"moduleKey\":\"com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item\",\"color\":\"blue\",\"position\":{\"row\":0,\"column\":0},\"title\":\"Issue statistics\"},{\"id\":10002,\"moduleKey\":\"com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-graph\",\"color\":\"red\",\"position\":{\"row\":1,\"column\":0},\"title\":\"Activity stream\"},{\"id\":10003,\"moduleKey\":\"com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item\",\"color\":\"yellow\",\"position\":{\"row\":0,\"column\":1},\"title\":\"Bubble chart\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the dashboard is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The dashboard you requested either does not exist or you don't have the required permissions to perform this action.\"],\"errors\":{}}"
```

