# 02-Create notification scheme [POST]

`POST /rest/api/3/notificationscheme`

Creates a notification scheme with notifications. You can create up to 1000 notifications per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the notification scheme.
  "name": string (required), // The name of the notification scheme. Must be unique (case-insensitive).
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
  ], // The list of notifications which should be added to the notification scheme.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10001\"}"
```

#### 400 - Returned if the request isn't valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The length of the description must not exceed 4000 characters.\"],\"errors\":{}}"
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

