# 05-Update issue type [PUT]

`PUT /rest/api/3/issuetype/{id}`

Updates the issue type.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue type. |

### Request Body (application/json)

```json
{
  "avatarId": integer, // The ID of an issue type avatar. This can be obtained be obtained from the following endpoints:   *  [System issue type avatar IDs only](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-avatar-type-system-get)  *  [System and custom issue type avatar IDs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/#api-rest-api-3-universal-avatar-type-type-owner-entityid-get)
  "description": string, // The description of the issue type.
  "name": string, // The unique name for the issue type. The maximum length is 60 characters.
}
```
### Responses

#### 200 - Returned if the request is successful.

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
 *  the avatar is not associated with this issue type.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the issue type is not found.

#### 409 - Returned if the issue type name is in use.

