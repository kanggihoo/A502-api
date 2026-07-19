# 02-Upload a metric image for an incident [POST]

`POST /api/v4/projects/{id}/issues/{issue_iid}/metric_images`

Uploads a screenshot of metric charts for an incident. Available only for incidents.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of an issuable |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The image file to be uploaded
  "url": string, // The url to view more metric info
  "url_text": string, // A description of the image or URL
}
```
### Responses

#### 201 - Created

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

