# 01-Set status of an external control [PATCH]

`PATCH /api/v4/projects/{id}/compliance_external_controls/{control_id}/status`

Sets the status of a specified external control. Use this operation to inform GitLab that a control has passed or failed a check by an external service.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `control_id` | `integer` | `path` | Yes | The ID of the control |

### Request Body (application/json)

```json
{
  "status": enum("pass" | "fail") (required), // The status of the control
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

