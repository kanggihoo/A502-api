# 06-Add notifications to notification scheme [PUT]

`PUT /rest/api/3/notificationscheme/{id}/notification`

Adds notifications to a notification scheme. You can add up to 1000 notifications per request.

*Deprecated: The notification type `EmailAddress` is no longer supported in Cloud. Refer to the [changelog](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1031) for more details.*

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the notification scheme. |

### Request Body (application/json)

```json
{
  "notificationSchemeEvents": [
    {
      "event": any (required), // The ID of the event.
      "notifications": [
        {
          "notificationType": string (required), // The notification type, e.g `CurrentAssignee`, `Group`, `EmailAddress`.
          "parameter": string, // The value corresponding to the specified notification type.
        }
      ] (required), // The list of notifications mapped to a specified event.
    }
  ] (required), // The list of notifications which should be added to the notification scheme.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request isn't valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Event type with ID 2 not found.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

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

#### 403 - Returned if the user doesn't have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"You are not authorized to perform this action. Administrator privileges are required.\"],\"errors\":{}}"
```

#### 404 - Returned if the notification scheme isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Notification scheme with ID 10001 not found.\"],\"errors\":{}}"
```

