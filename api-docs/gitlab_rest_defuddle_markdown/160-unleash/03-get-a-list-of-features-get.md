# 03-Get a list of features [GET]

`GET /api/v4/feature_flags/unleash/{project_id}/client/features`

Get a list of features

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `string` | `path` | Yes | The ID of a project |
| `instance_id` | `string` | `query` | No | The instance ID of Unleash Client |
| `app_name` | `string` | `query` | No | The application name of Unleash Client |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

