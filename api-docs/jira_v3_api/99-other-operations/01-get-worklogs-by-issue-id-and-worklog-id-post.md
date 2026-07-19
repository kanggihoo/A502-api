# 01-Get worklogs by issue id and worklog id [POST]

`POST /rest/internal/api/latest/worklog/bulk`

Returns worklog details for a list of issue ID and worklog ID pairs.

This is an internal API for bulk fetching worklogs by their issue and worklog IDs. Worklogs that don't exist will be filtered out from the response.

The returned list of worklogs is limited to 1000 items.

**[Permissions](#permissions) required:** This is an internal service-to-service API that requires ASAP authentication. No user permission checks are performed as this bypasses normal user context.

### Request Body (application/json)

```json
{
  "requests": [
    {
      "issueId": integer, // The issue ID.
      "worklogId": integer, // The worklog ID.
    }
  ], // A list of issue and worklog ID pairs.
}
```
### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "worklogs": [
    {
      "issueId": integer, // The issue ID.
      "worklogId": integer, // The worklog ID.
    }
  ], // A list of successfully retrieved worklogs with their issue and worklog IDs.
}
```

#### 400 - Returned if the request contains more than 1000 worklog pairs, is empty, or has invalid format.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 500 - Returned if there is an internal server error.

