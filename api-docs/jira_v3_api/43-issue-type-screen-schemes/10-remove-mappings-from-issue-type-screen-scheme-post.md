# 10-Remove mappings from issue type screen scheme [POST]

`POST /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove`

Removes issue type to screen scheme mappings from an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeScreenSchemeId` | `string` | `path` | Yes | The ID of the issue type screen scheme. |

### Request Body (application/json)

```json
{
  "issueTypeIds": [
    string
  ] (required), // The list of issue type IDs.
}
```
### Responses

#### 204 - Returned if the screen scheme mappings are removed from the issue type screen scheme.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The issueTypeIds must not contain duplicates.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type screen scheme or one or more issue type mappings are not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

