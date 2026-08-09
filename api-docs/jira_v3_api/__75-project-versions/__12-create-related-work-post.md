# 12-Create related work [POST]

`POST /rest/api/3/version/{id}/relatedwork`

Creates a related work for the given version. You can only create a generic link type of related works via this API. relatedWorkId will be auto-generated UUID, that does not need to be provided.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "category": string (required), // The category of the related work
  "issueId": integer, // The ID of the issue associated with the related work (if there is one). Cannot be updated via the Rest API.
  "relatedWorkId": string, // The id of the related work. For the native release note related work item, this will be null, and Rest API does not support updating it.
  "title": string, // The title of the related work
  "url": string, // The URL of the related work. Will be null for the native release note related work item, but is otherwise required.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"category\":\"Design\",\"relatedWorkId\":\"fabcdef6-7878-1234-beaf-43211234abcd\",\"title\":\"Design link\",\"url\":\"https://www.atlassian.com\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

#### 404 - Returned if the version is not found.

