# 04-Update a metric image for an incident [PUT]

`PUT /api/v4/projects/{id}/issues/{issue_iid}/metric_images/{metric_image_id}`

Updates a metric image for an incident.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `metric_image_id` | `integer` | `path` | Yes | The ID of metric image |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of an issuable |

### Request Body (application/json)

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

#### 404 - Not Found

