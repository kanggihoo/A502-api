# 03-Get issue type scheme items [GET]

`GET /rest/api/3/issuetypescheme/mapping`

Returns a [paginated](#pagination) list of issue type scheme items.

Only issue type scheme items used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `issueTypeSchemeId` | `array` | `query` | No | The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `issueTypeSchemeId=10000&issueTypeSchemeId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":4,\"values\":[{\"issueTypeSchemeId\":\"10000\",\"issueTypeId\":\"10000\"},{\"issueTypeSchemeId\":\"10000\",\"issueTypeId\":\"10001\"},{\"issueTypeSchemeId\":\"10000\",\"issueTypeId\":\"10002\"},{\"issueTypeSchemeId\":\"10001\",\"issueTypeId\":\"10000\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

