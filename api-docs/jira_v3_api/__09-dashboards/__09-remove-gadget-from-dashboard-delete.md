# 09-Remove gadget from dashboard [DELETE]

`DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`

Removes a dashboard gadget from a dashboard.

When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardId` | `integer` | `path` | Yes | The ID of the dashboard. |
| `gadgetId` | `integer` | `path` | Yes | The ID of the gadget. |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the gadget or the dashboard is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The dashboard gadget was not found.\"],\"errors\":{}}"
```

