# 02-Create a new software license policy in a project [POST]

`POST /api/v4/projects/{id}/managed_licenses`

Create a new software license policy in a project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the license
  "approval_status": enum("allowed" | "denied") (required), // The approval status of the license.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "approval_status": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

