# 03-Get issue link type [GET]

`GET /rest/api/3/issueLinkType/{issueLinkTypeId}`

Returns an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueLinkTypeId` | `string` | `path` | Yes | The ID of the issue link type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"1000\",\"inward\":\"Duplicated by\",\"name\":\"Duplicate\",\"outward\":\"Duplicates\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000\"}"
```

#### 400 - Returned if the issue link type ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  issue linking is disabled.
 *  the issue link type is not found.
 *  the user does not have the required permissions.

