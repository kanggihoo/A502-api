# 08-Update a runner controller [PUT]

`PUT /api/v4/runner_controllers/{id}`

Updates the details of an existing runner controller by its ID.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |

### Request Body (application/json)

```json
{
  "description": string, // Description of the runner controller
  "state": enum("disabled" | "enabled" | "dry_run"), // State of the runner controller (disabled, enabled, dry_run)
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

