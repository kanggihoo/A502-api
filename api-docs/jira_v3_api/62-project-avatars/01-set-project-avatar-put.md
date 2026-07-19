# 01-Set project avatar [PUT]

`PUT /rest/api/3/project/{projectIdOrKey}/avatar`

Sets the avatar displayed for a project.

Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or (case-sensitive) key of the project. |

### Request Body (application/json)

```json
{
  "fileName": string, // The file name of the avatar icon. Returned for system avatars.
  "id": string (required), // The ID of the avatar.
  "isDeletable": boolean, // Whether the avatar can be deleted.
  "isSelected": boolean, // Whether the avatar is used in Jira. For example, shown as a project's avatar.
  "isSystemAvatar": boolean, // Whether the avatar is a system avatar.
  "owner": string, // The owner of the avatar. For a system avatar the owner is null (and nothing is returned). For non-system avatars this is the appropriate identifier, such as the ID for a project or the account ID for a user.
  "urls": {}, // The list of avatar icon URLs.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to administer the project.

#### 404 - Returned if the project or avatar is not found or the user does not have permission to view the project.

