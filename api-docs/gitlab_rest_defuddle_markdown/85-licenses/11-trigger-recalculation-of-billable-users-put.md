# 11-Trigger recalculation of billable users [PUT]

`PUT /api/v4/license/{id}/refresh_billable_users`

Triggers recalculation of billable users for a specified license.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the GitLab license |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "success": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

