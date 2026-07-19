# 04-Update a metric image [PUT]

`PUT /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id}`

Updates a specified metric image for an alert.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `alert_iid` | `integer` | `path` | Yes | The IID of the Alert |
| `metric_image_id` | `integer` | `path` | Yes | The ID of metric image |

### Request Body (multipart/form-data)

```json
{
  "url": string, // The url to view more metric info
  "url_text": string, // A description of the image or URL
}
```
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

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable entity

