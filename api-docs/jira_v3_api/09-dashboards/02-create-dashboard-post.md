# 02-Create dashboard [POST]

`POST /rest/api/3/dashboard`

Creates a dashboard.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `extendAdminPermissions` | `boolean` | `query` | No | Whether admin level permissions are used. It should only be true if the user has *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) |

### Request Body (application/json)

```json
{
  "description": string, // The description of the dashboard.
  "editPermissions": [
    {
      "group": any, // The group that the filter is shared with. For a request, specify the `groupId` or `name` property for the group. As a group's name can change, use of `groupId` is recommended.
      "id": integer, // The unique identifier of the share permission.
      "project": any, // The project that the filter is shared with. This is similar to the project object returned by [Get project](#api-rest-api-3-project-projectIdOrKey-get) but it contains a subset of the properties, which are: `self`, `id`, `key`, `assigneeType`, `name`, `roles`, `avatarUrls`, `projectType`, `simplified`.   For a request, specify the `id` for the project.
      "role": any, // The project role that the filter is shared with.   For a request, specify the `id` for the role. You must also specify the `project` object and `id` for the project that the role is in.
      "type": enum("user" | "group" | "project" | "projectRole" | "global" | "loggedin" | "authenticated" | "project-unknown") (required), // The type of share permission:   *  `user` Shared with a user.  *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.  *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.  *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.  *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.  *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.  *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
      "user": any, // The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.
    }
  ] (required), // The edit permissions for the dashboard.
  "name": string (required), // The name of the dashboard.
  "sharePermissions": [
    {
      "group": any, // The group that the filter is shared with. For a request, specify the `groupId` or `name` property for the group. As a group's name can change, use of `groupId` is recommended.
      "id": integer, // The unique identifier of the share permission.
      "project": any, // The project that the filter is shared with. This is similar to the project object returned by [Get project](#api-rest-api-3-project-projectIdOrKey-get) but it contains a subset of the properties, which are: `self`, `id`, `key`, `assigneeType`, `name`, `roles`, `avatarUrls`, `projectType`, `simplified`.   For a request, specify the `id` for the project.
      "role": any, // The project role that the filter is shared with.   For a request, specify the `id` for the role. You must also specify the `project` object and `id` for the project that the role is in.
      "type": enum("user" | "group" | "project" | "projectRole" | "global" | "loggedin" | "authenticated" | "project-unknown") (required), // The type of share permission:   *  `user` Shared with a user.  *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.  *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.  *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.  *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.  *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.  *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
      "user": any, // The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.
    }
  ] (required), // The share permissions for the dashboard.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10000\",\"isFavourite\":false,\"name\":\"System Dashboard\",\"popularity\":1,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/10000\",\"sharePermissions\":[{\"type\":\"global\"}],\"view\":\"https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000\"}"
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

