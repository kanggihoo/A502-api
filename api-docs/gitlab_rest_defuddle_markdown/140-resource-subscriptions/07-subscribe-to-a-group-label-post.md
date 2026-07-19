# 07-Subscribe to a group label [POST]

`POST /api/v4/groups/{id}/labels/{subscribable_id}/subscribe`

Subscribes the currently authenticated user to a specified group label. They will receive notifications on changes to this item.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |
| `subscribable_id` | `string` | `path` | Yes | The ID of a resource |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "description": string,
  "text_color": string,
  "description_html": string,
  "color": string,
  "archived": boolean,
  "open_issues_count": integer,
  "closed_issues_count": integer,
  "open_merge_requests_count": integer,
  "subscribed": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

