# 04-Register Unleash client [POST]

`POST /api/v4/feature_flags/unleash/{project_id}/client/register`

Register Unleash client

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `string` | `path` | Yes | The ID of a project |

### Request Body (application/json)

```json
{
  "instance_id": string, // The instance ID of Unleash Client
  "app_name": string, // The application name of Unleash Client
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

