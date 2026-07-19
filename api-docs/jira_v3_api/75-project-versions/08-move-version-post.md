# 08-Move version [POST]

`POST /rest/api/3/version/{id}/move`

Modifies the version's sequence within the project, which affects the display order of the versions in Jira.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version to be moved. |

### Request Body (application/json)

```json
{
  "after": string, // The URL (self link) of the version after which to place the moved version. Cannot be used with `position`.
  "position": enum("Earlier" | "Later" | "First" | "Last"), // An absolute position in which to place the moved version. Cannot be used with `after`.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"archived\":false,\"description\":\"An excellent version\",\"id\":\"10000\",\"name\":\"New Version 1\",\"overdue\":true,\"projectId\":10000,\"releaseDate\":\"2010-07-06\",\"released\":true,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\",\"userReleaseDate\":\"6/Jul/2010\"}"
```

#### 400 - Returned if:

 *  no body parameters are provided.
 *  `after` and `position` are provided.
 *  `position` is invalid.

#### 401 - Returned if:

 *  the authentication credentials are incorrect or missing
 *  the user does not have the required commissions.

#### 404 - Returned if the version or move after version are not found.

