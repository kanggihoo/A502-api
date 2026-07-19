# 02-Get redaction status [GET]

`GET /rest/api/3/redact/status/{jobId}`

Retrieves the current status of a redaction job ID.

The jobStatus will be one of the following:

 *  IN\_PROGRESS - The redaction job is currently in progress
 *  COMPLETED - The redaction job has completed successfully.
 *  PENDING - The redaction job has not started yet

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `jobId` | `string` | `path` | Yes | Redaction job id |

### Responses

#### 200 - Returned if the job status is successfully retrieved.

Schema (application/json):
```json
{
  "bulkRedactionResponse": {
    "results": [
      {
        "externalId": string (required), // An unique id for the redaction request
        "successful": boolean (required), // Indicates if redaction was success/failure
      }
    ] (required), // Result for requested redactions
  },
  "jobStatus": enum("PENDING" | "IN_PROGRESS" | "COMPLETED"),
}
```

#### 403 - Returned if the AGP subscription is not present.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 404 - Returned if the job id is not found.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

