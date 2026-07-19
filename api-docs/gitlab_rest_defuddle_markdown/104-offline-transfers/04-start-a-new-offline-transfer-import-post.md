# 04-Start a new offline transfer import [POST]

`POST /api/v4/offline_imports`

Initiates a new offline transfer import from object storage

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
  "export_prefix": string (required), // Prefix of the export within the bucket
  "entities": [
    {
      "source_type": enum("group_entity" | "project_entity") (required), // Type of the entity to import
      "source_full_path": string (required), // Full path of the entity on the source instance
      "destination_namespace": string (required), // Full path of the destination namespace
      "destination_slug": string, // Destination slug for the imported entity
    }
  ] (required), // List of entities to import
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "status": string,
  "source_type": string,
  "source_url": string,
  "created_at": string,
  "updated_at": string,
  "has_failures": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

#### 422 - Unprocessable entity

#### 429 - Too many requests

