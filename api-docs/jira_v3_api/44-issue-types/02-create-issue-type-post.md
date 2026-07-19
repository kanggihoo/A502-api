# 02-Create issue type [POST]

`POST /rest/api/3/issuetype`

Creates an issue type.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the issue type.
  "hierarchyLevel": integer, // The hierarchy level of the issue type. Use:   *  `-1` for Subtask.  *  `0` for Base.  Defaults to `0`.
  "name": string (required), // The unique name for the issue type. The maximum length is 60 characters.
  "type": enum("subtask" | "standard"), // Deprecated. Use `hierarchyLevel` instead. See the [deprecation notice](https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-fields-in-rest-apis-and-webhooks/54048) for details.  Whether the issue type is `subtype` or `standard`. Defaults to `standard`.
}
```
### Responses

#### 201 - Returned if the request is successful.

Schema (application/json):
```json
{
  "avatarId": integer, // The ID of the issue type's avatar.
  "description": string, // The description of the issue type.
  "entityId": string, // Unique ID for next-gen projects.
  "hierarchyLevel": integer, // Hierarchy level of the issue type.
  "iconUrl": string, // The URL of the issue type's avatar.
  "id": string, // The ID of the issue type.
  "name": string, // The name of the issue type.
  "scope": any, // Details of the next-gen projects the issue type is available in.
  "self": string, // The URL of these issue type details.
  "subtask": boolean, // Whether this issue type is used to create subtasks.
}
```

#### 400 - Returned if the request is invalid because:

 *  no content is sent.
 *  the issue type name exceeds 60 characters.
 *  a subtask issue type is requested on an instance where subtasks are disabled.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 409 - Returned if the issue type name is in use.

