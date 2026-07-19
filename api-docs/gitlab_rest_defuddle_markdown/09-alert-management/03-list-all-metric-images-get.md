# 03-List all metric images [GET]

`GET /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images`

Lists all metric images for a specified alert.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `alert_iid` | `integer` | `path` | Yes | The IID of the Alert |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "created_at": string,
  "filename": string,
  "file_path": string,
  "url": string,
  "url_text": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

