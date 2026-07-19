# 04-Recalculate checksums for model records [PUT]

`PUT /api/v4/admin/data_management/{model_name}/checksum`

Recalculates checksums for selected records of a specified model, filtered by `checksum_state` and `identifiers` parameters if provided. The request enqueues a background job to perform the recalculation. Only available to administrators on primary Geo sites.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `model_name` | `string` | `path` | Yes | See https://docs.gitlab.com/administration/admin_area/#data-management for the list of allowed values |

### Request Body (application/json)

```json
{
  "identifiers": any,
  "checksum_state": enum("started" | "succeeded" | "failed" | "disabled"), // The checksum status of the records to filter by
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "record_identifier": any,
  "model_class": string,
  "created_at": string,
  "file_size": integer,
  "checksum_information": {},
}
```

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Model Not Found

