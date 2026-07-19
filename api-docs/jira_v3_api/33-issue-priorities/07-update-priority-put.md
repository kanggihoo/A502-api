# 07-Update priority [PUT]

`PUT /rest/api/3/priority/{id}`

Updates an issue priority.

At least one request body parameter must be defined.

**Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue priority. |

### Request Body (application/json)

```json
{
  "avatarId": integer, // The ID for the avatar for the priority. This parameter is nullable and both iconUrl and avatarId cannot be defined.
  "description": string, // The description of the priority.
  "iconUrl": enum("/images/icons/priorities/blocker.png" | "/images/icons/priorities/critical.png" | "/images/icons/priorities/high.png" | "/images/icons/priorities/highest.png" | "/images/icons/priorities/low.png" | "/images/icons/priorities/lowest.png" | "/images/icons/priorities/major.png" | "/images/icons/priorities/medium.png" | "/images/icons/priorities/minor.png" | "/images/icons/priorities/trivial.png" | "/images/icons/priorities/blocker_new.png" | "/images/icons/priorities/critical_new.png" | "/images/icons/priorities/high_new.png" | "/images/icons/priorities/highest_new.png" | "/images/icons/priorities/low_new.png" | "/images/icons/priorities/lowest_new.png" | "/images/icons/priorities/major_new.png" | "/images/icons/priorities/medium_new.png" | "/images/icons/priorities/minor_new.png" | "/images/icons/priorities/trivial_new.png"), // The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Both iconUrl and avatarId cannot be defined.
  "name": string, // The name of the priority. Must be unique.
  "statusColor": string, // The status color of the priority in 3-digit or 6-digit hexadecimal format.
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
"{\"errorMessages\":[\"The length of the description must not exceed 255 characters.\"],\"errors\":{}}"
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

#### 404 - Returned if the issue priority isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Priority with ID 10000 not found.\"],\"errors\":{}}"
```

