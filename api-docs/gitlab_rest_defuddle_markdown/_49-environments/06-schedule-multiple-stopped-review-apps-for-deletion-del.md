# 06-Schedule multiple stopped review apps for deletion [DEL]

`DELETE /api/v4/projects/{id}/environments/review_apps`

Schedules multiple stopped review apps for deletion. The deletion is performed after 1 week. By default, only environments 30 days or older are deleted.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `before` | `string` | `query` | No | The date before which environments can be deleted. Defaults to 30 days ago. Expected in ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`) |
| `limit` | `integer` | `query` | No | Maximum number of environments to delete. Defaults to 100 |
| `dry_run` | `boolean` | `query` | No | Defaults to true for safety reasons. It performs a dry run where no actual deletion will be performed. Set to false to actually delete the environment |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "slug": string,
  "external_url": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

#### 409 - Conflict

