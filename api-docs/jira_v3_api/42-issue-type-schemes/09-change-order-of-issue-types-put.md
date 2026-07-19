# 09-Change order of issue types [PUT]

`PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move`

Changes the order of issue types in an issue type scheme.

The request body parameters must meet the following requirements:

 *  all of the issue types must belong to the issue type scheme.
 *  either `after` or `position` must be provided.
 *  the issue type in `after` must not be in the issue type list.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeSchemeId` | `integer` | `path` | Yes | The ID of the issue type scheme. |

### Request Body (application/json)

```json
{
  "after": string, // The ID of the issue type to place the moved issue types after. Required if `position` isn't provided.
  "issueTypeIds": [
    string
  ] (required), // A list of the issue type IDs to move. The order of the issue type IDs in the list is the order they are given after the move.
  "position": enum("First" | "Last"), // The position the issue types should be moved to. Required if `after` isn't provided.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type scheme does not include some of the specified issue types. Issue type IDs missing from the scheme are:  10007, 10008\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type scheme was not found.\"],\"errors\":{}}"
```

