# 04-Update an existing software license policy from a project [PATCH]

`PATCH /api/v4/projects/{id}/managed_licenses/{managed_license_id}`

Update an existing software license policy from a project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `managed_license_id` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "name": string, // The name of the license
  "approval_status": enum("allowed" | "denied"), // The approval status of the license.
}
```
### Responses

#### 200 - OK

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

