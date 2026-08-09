# 04-Get failed webhooks [GET]

`GET /rest/api/3/webhook/failed`

Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.

After 72 hours the failure may no longer be returned by this operation.

The oldest failure is returned first.

This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

**[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `maxResults` | `integer` | `query` | No | The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all records with the same failure time included on the page. |
| `after` | `integer` | `query` | No | The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"values\":[{\"id\":\"1\",\"body\":\"{\\\"data\\\":\\\"webhook data\\\"}\",\"url\":\"https://example.com\",\"failureTime\":1573118132000},{\"id\":\"2\",\"url\":\"https://example.com\",\"failureTime\":1573540473480}],\"maxResults\":100,\"next\":\"https://your-domain.atlassian.net/rest/api/3/webhook/failed?failedAfter=1573540473480&maxResults=100\"}"
```

#### 400 - 400 response

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

#### 403 - Returned if the caller is not a Connect app.

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

