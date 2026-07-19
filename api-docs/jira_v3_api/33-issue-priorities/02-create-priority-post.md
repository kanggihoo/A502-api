# 02-Create priority [POST]

`POST /rest/api/3/priority`

Creates an issue priority.

**Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "avatarId": integer, // The ID for the avatar for the priority. Either the iconUrl or avatarId must be defined, but not both. This parameter is nullable and will become mandatory once the iconUrl parameter is deprecated.
  "description": string, // The description of the priority.
  "iconUrl": enum("/images/icons/priorities/blocker.png" | "/images/icons/priorities/critical.png" | "/images/icons/priorities/high.png" | "/images/icons/priorities/highest.png" | "/images/icons/priorities/low.png" | "/images/icons/priorities/lowest.png" | "/images/icons/priorities/major.png" | "/images/icons/priorities/medium.png" | "/images/icons/priorities/minor.png" | "/images/icons/priorities/trivial.png" | "/images/icons/priorities/blocker_new.png" | "/images/icons/priorities/critical_new.png" | "/images/icons/priorities/high_new.png" | "/images/icons/priorities/highest_new.png" | "/images/icons/priorities/low_new.png" | "/images/icons/priorities/lowest_new.png" | "/images/icons/priorities/major_new.png" | "/images/icons/priorities/medium_new.png" | "/images/icons/priorities/minor_new.png" | "/images/icons/priorities/trivial_new.png"), // The URL of an icon for the priority. Accepted protocols are HTTP and HTTPS. Built in icons can also be used. Either the iconUrl or avatarId must be defined, but not both.
  "name": string (required), // The name of the priority. Must be unique.
  "statusColor": string (required), // The status color of the priority in 3-digit or 6-digit hexadecimal format.
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
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

