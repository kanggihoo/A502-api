# 07-Retrieve a single runner controller [GET]

`GET /api/v4/runner_controllers/{id}`

Retrieves details of a specified runner controller.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |

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
  "connected": boolean,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

