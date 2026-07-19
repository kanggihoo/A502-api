# 02-Create plan [POST]

`POST /rest/api/3/plans/plan`

Creates a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `useGroupId` | `boolean` | `query` | No | Whether to accept group IDs instead of group names. Group names are deprecated. |

### Request Body (application/json)

```json
{
  "crossProjectReleases": [
    {
      "name": string (required), // The cross-project release name.
      "releaseIds": [
        integer
      ], // The IDs of the releases to include in the cross-project release.
    }
  ], // The cross-project releases to include in the plan.
  "customFields": [
    {
      "customFieldId": integer (required), // The custom field ID.
      "filter": boolean, // Allows filtering issues based on their values for the custom field.
    }
  ], // The custom fields for the plan.
  "exclusionRules": any, // The exclusion rules for the plan.
  "issueSources": [
    {
      "type": enum("Board" | "Project" | "Filter") (required), // The issue source type. This must be "Board", "Project" or "Filter".
      "value": integer (required), // The issue source value. This must be a board ID if the type is "Board", a project ID if the type is "Project" or a filter ID if the type is "Filter".
    }
  ] (required), // The issue sources to include in the plan.
  "leadAccountId": string, // The account ID of the plan lead.
  "name": string (required), // The plan name.
  "permissions": [
    {
      "holder": any (required), // The permission holder.
      "type": enum("View" | "Edit") (required), // The permission type. This must be "View" or "Edit".
    }
  ], // The permissions for the plan.
  "scheduling": any (required), // The scheduling settings for the plan.
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

