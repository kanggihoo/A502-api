# 03-Get issue type screen scheme items [GET]

`GET /rest/api/3/issuetypescreenscheme/mapping`

Returns a [paginated](#pagination) list of issue type screen scheme items.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `issueTypeScreenSchemeId` | `array` | `query` | No | The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: `issueTypeScreenSchemeId=10000&issueTypeScreenSchemeId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":4,\"values\":[{\"issueTypeId\":\"10000\",\"issueTypeScreenSchemeId\":\"10020\",\"screenSchemeId\":\"10010\"},{\"issueTypeId\":\"10001\",\"issueTypeScreenSchemeId\":\"10021\",\"screenSchemeId\":\"10010\"},{\"issueTypeId\":\"10002\",\"issueTypeScreenSchemeId\":\"10022\",\"screenSchemeId\":\"10010\"},{\"issueTypeId\":\"default\",\"issueTypeScreenSchemeId\":\"10023\",\"screenSchemeId\":\"10011\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

