# 03-Create a dependency list export [POST]

`POST /api/v4/pipelines/{id}/dependency_list_exports`

Creates a CycloneDX JSON export for all the project dependencies detected in a pipeline. If an authenticated user does not have the read_dependency permission, this request returns a `403 Forbidden` status code.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID of the pipeline |

### Request Body (application/json)

```json
{
  "send_email": boolean, // Send an email when the export completes
  "export_type": enum("sbom"), // The type of the export file
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

