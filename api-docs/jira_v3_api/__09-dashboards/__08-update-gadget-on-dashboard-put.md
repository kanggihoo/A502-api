# 08-Update gadget on dashboard [PUT]

`PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}`

Changes the title, position, and color of the gadget on a dashboard.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardId` | `integer` | `path` | Yes | The ID of the dashboard. |
| `gadgetId` | `integer` | `path` | Yes | The ID of the gadget. |

### Request Body (application/json)

```json
{
  "color": string, // The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`, `purple`, `gray`, or `white`.
  "position": any, // The position of the gadget.
  "title": string, // The title of the gadget.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"The gadget cannot be placed in the selected row. The selected row does not exist on the dashboard.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the gadget or the dashboard is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The dashboard you requested either does not exist or you don't have the required permissions to perform this action.\"],\"errors\":{}}"
```

