# 01-Workhorse authorize metric image file upload [POST]

`POST /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/authorize`

Workhorse authorize metric image file upload

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `alert_iid` | `integer` | `path` | Yes | The IID of the Alert |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

