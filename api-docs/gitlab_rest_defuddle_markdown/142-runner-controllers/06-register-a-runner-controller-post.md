# 06-Register a runner controller [POST]

`POST /api/v4/runner_controllers`

Registers a runner controller.

### Request Body (application/json)

```json
{
  "description": string, // Description of the runner controller
  "state": enum("disabled" | "enabled" | "dry_run"), // State of the runner controller (disabled, enabled, dry_run)
}
```
### Responses

#### 201 - Created

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

