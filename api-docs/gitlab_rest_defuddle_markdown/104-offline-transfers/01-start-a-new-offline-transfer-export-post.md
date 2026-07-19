# 01-Start a new offline transfer export [POST]

`POST /api/v4/offline_exports`

Initiates a new offline transfer export

### Request Body (application/json)

```json
{
  "bucket": string (required), // Name of the object storage bucket where export data is stored
  "aws_s3_configuration": {
    "aws_access_key_id": string (required), // AWS S3 access key ID
    "aws_secret_access_key": string (required), // AWS S3 secret access key
    "region": string (required), // AWS S3 object storage region
    "path_style": boolean, // Use path-style URLs instead of virtual-hosted-style URLs
  }, // AWS S3 object storage configuration
  "s3_compatible_configuration": {
    "aws_access_key_id": string (required), // S3-compatible access key ID
    "aws_secret_access_key": string (required), // S3-compatible secret access key
    "region": string (required), // S3-compatible object storage region
    "endpoint": string (required), // Object storage location endpoint
    "path_style": boolean, // Use path-style URLs instead of virtual-hosted-style URLs
  }, // MinIO or other S3-compatible object storage configuration
  "gcs_configuration": {
    "google_project": string (required), // Google Cloud project ID
    "google_json_key_string": string (required), // Google Cloud service account JSON key contents
  }, // Google Cloud Storage configuration using a service account JSON key
  "gcs_hmac_configuration": {
    "google_storage_access_key_id": string (required), // GCS HMAC access key ID
    "google_storage_secret_access_key": string (required), // GCS HMAC secret
    "region": string (required), // GCS bucket region
    "path_style": boolean, // Use path-style URLs instead of virtual-hosted-style URLs
  }, // Google Cloud Storage configuration using S3-interoperability HMAC keys
  "entities": [
    {
      "full_path": string (required), // Relative path of the entity to export
    }
  ] (required), // List of entities to export
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

