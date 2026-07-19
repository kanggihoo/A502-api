# 03-Suggested priorities for mappings [POST]

`POST /rest/api/3/priorityscheme/mappings`

Returns a [paginated](#pagination) list of priorities that would require mapping, given a change in priorities or projects associated with a priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "maxResults": integer, // The maximum number of results that could be on the page.
  "priorities": any, // The priority changes in the scheme.
  "projects": any, // The project changes in the scheme.
  "schemeId": integer, // The id of the priority scheme.
  "startAt": integer, // The index of the first item returned on the page.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":3,\"values\":[{\"description\":\"Serious problem that could block progress.\",\"iconUrl\":\"/images/icons/priorities/high.svg\",\"id\":\"1\",\"isDefault\":false,\"name\":\"High\",\"statusColor\":\"#f15C75\"},{\"description\":\"Has the potential to affect progress.\",\"iconUrl\":\"/images/icons/priorities/medium.svg\",\"id\":\"2\",\"isDefault\":true,\"name\":\"Medium\",\"statusColor\":\"#f79232\"},{\"description\":\"Minor problem or easily worked around.\",\"iconUrl\":\"/images/icons/priorities/low.svg\",\"id\":\"3\",\"isDefault\":false,\"name\":\"Low\",\"statusColor\":\"#707070\"}]}"
```

#### 400 - Returned if the request isn't valid.

#### 401 - Returned if the authentication credentials are incorrect.

