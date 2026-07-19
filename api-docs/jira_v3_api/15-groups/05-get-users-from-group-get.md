# 05-Get users from group [GET]

`GET /rest/api/3/group/member`

Returns a [paginated](#pagination) list of all users in a group.

Note that users are ordered by username, however the username is not returned in the results due to privacy reasons.

**[Permissions](#permissions) required:** either of:

 *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `groupname` | `string` | `query` | No | As a group's name can change, use of `groupId` is recommended to identify a group.  <br>The name of the group. This parameter cannot be used with the `groupId` parameter. |
| `groupId` | `string` | `query` | No | The ID of the group. This parameter cannot be used with the `groupName` parameter. |
| `includeInactiveUsers` | `boolean` | `query` | No | Include inactive users. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page (number should be between 1 and 50). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/group/member?groupId=276f955c-63d7-42c8-9520-92d01dca0625&includeInactiveUsers=false&startAt=4&maxResults=2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group/member?groupId=276f955c-63d7-42c8-9520-92d01dca0625&includeInactiveUsers=false&startAt=2&maxResults=2\",\"startAt\":3,\"total\":5,\"values\":[{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":true,\"avatarUrls\":{},\"displayName\":\"Mia\",\"emailAddress\":\"mia@example.com\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},{\"accountId\":\"5b10a0effa615349cb016cd8\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{},\"displayName\":\"Will\",\"emailAddress\":\"will@example.com\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a0effa615349cb016cd8\",\"timeZone\":\"Australia/Sydney\"}]}"
```

#### 400 - Returned if the group name is not specified.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the calling user does not have the Administer Jira global permission.

#### 404 - Returned if the group is not found.

