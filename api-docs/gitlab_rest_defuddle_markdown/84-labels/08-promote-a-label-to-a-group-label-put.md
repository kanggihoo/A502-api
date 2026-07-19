# 08-Promote a label to a group label [PUT]

`PUT /api/v4/projects/{id}/labels/promote`

Added in GitLab 12.3 and deprecated in GitLab 12.4. Use PUT /projects/:id/labels/:name/promote instead.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the label to be promoted
}
```
### Responses

#### 200 - OK

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

