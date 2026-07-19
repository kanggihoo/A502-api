# 01-Upload a metric image for an incident [POST]

`POST /api/v4/projects/{id}/issues/{issue_iid}/metric_images/authorize`

Upload a metric image for an incident

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of an issuable |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

