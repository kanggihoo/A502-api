# 06-Create an export for archived vulnerabilities [POST]

`POST /api/v4/security/projects/{id}/vulnerability_archive_exports`

Creates an export for archived vulnerabilities in a specified project. If an authenticated user does not have permission to read vulnerabilities, returns a `403 Forbidden` status code.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "start_date": string (required), // Start of the date range
  "end_date": string (required), // End of the date range
  "export_format": enum("csv"), // The format of export to be generated
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "created_at": string,
  "project_id": integer,
  "format": string,
  "status": string,
  "started_at": string,
  "finished_at": string,
  "_links": {},
}
```

#### 400 - Bad Request

#### 404 - Not Found

