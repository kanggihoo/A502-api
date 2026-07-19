# 01-Redact [POST]

`POST /rest/api/3/redact`

Submit a job to redact issue field data. This will trigger the redaction of the data in the specified fields asynchronously.

The redaction status can be polled using the job id.

### Request Body (application/json)

```json
{
  "redactions": [
    {
      "contentItem": {
        "entityId": string (required), // The ID of the content entity.   *  For redacting an issue field, this will be the field ID (e.g., summary, customfield\_10000).  *  For redacting a comment, this will be the comment ID.  *  For redacting a worklog, this will be the worklog ID.
        "entityType": enum("issuefieldvalue" | "issue-comment" | "issue-worklog") (required), // The type of the entity to redact; It will be one of the following:   *  **issuefieldvalue** \- To redact in issue fields  *  **issue-comment** \- To redact in issue comments.  *  **issue-worklog** \- To redact in issue worklogs
        "id": string (required), // This would be the issue ID
      } (required),
      "externalId": string (required), // Unique id for the redaction request; ID format should be of UUID
      "reason": string (required), // The reason why the content is being redacted
      "redactionPosition": {
        "adfPointer": string, // The ADF pointer indicating the position of the text to be redacted. This is only required when redacting from rich text(ADF) fields. For plain text fields, this field can be omitted.
        "expectedText": string (required), // The text which will be redacted, encoded using SHA256 hash and Base64 digest
        "from": integer (required), // The start index(inclusive) for the redaction in specified content
        "to": integer (required), // The ending index(exclusive) for the redaction in specified content
      } (required),
    }
  ],
}
```
### Responses

#### 202 - Returned if the job submission is successful. The response contains the job id.

Schema (application/json):
```json
string
```

#### 400 - Returned if the redaction request is invalid.

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

#### 401 - Returned if the user / app is not authorised to redact data

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

