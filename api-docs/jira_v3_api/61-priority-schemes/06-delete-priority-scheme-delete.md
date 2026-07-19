# 06-Delete priority scheme [DELETE]

`DELETE /rest/api/3/priorityscheme/{schemeId}`

Deletes a priority scheme.

This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The priority scheme ID. |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request isn't valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user doesn't have the necessary permissions.

