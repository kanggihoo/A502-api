# 06-Create plan-only team [POST]

`POST /rest/api/3/plans/plan/{planId}/team/planonly`

Creates a plan-only team and configures their planning settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `planId` | `integer` | `path` | Yes | The ID of the plan. |

### Request Body (application/json)

```json
{
  "capacity": number, // The capacity for the plan-only team.
  "issueSourceId": integer, // The ID of the issue source for the plan-only team.
  "memberAccountIds": [
    string
  ], // The account IDs of the plan-only team members.
  "name": string (required), // The plan-only team name.
  "planningStyle": enum("Scrum" | "Kanban") (required), // The planning style for the plan-only team. This must be "Scrum" or "Kanban".
  "sprintLength": integer, // The sprint length for the plan-only team.
}
```
### Responses

#### 201 - Returned if the request is successful.

Schema (application/json):
```json
integer
```

#### 400 - Returned if the request is not valid.

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

#### 401 - Returned if the user is not logged in.

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

#### 403 - Returned if the site has no premium edition of Jira or if the user does not have the Administer Jira global permission.

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

#### 404 - Returned if the plan is not found.

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

#### 409 - Returned if the plan is not active.

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

