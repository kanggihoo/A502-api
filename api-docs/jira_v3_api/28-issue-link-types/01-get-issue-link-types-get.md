# 01-Get issue link types [GET]

`GET /rest/api/3/issueLinkType`

Returns a list of all issue link types.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueLinkTypes\":[{\"id\":\"1000\",\"inward\":\"Duplicated by\",\"name\":\"Duplicate\",\"outward\":\"Duplicates\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000\"},{\"id\":\"1010\",\"inward\":\"Blocked by\",\"name\":\"Blocks\",\"outward\":\"Blocks\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1010\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if issue linking is disabled.

