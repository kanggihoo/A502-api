# 04-Bulk get groups [GET]

`GET /rest/api/3/group/bulk`

Returns a [paginated](#pagination) list of groups.

**[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `groupId` | `array` | `query` | No | The ID of a group. To specify multiple IDs, pass multiple `groupId` parameters. For example, `groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5`. |
| `groupName` | `array` | `query` | No | The name of a group. To specify multiple names, pass multiple `groupName` parameters. For example, `groupName=administrators&groupName=jira-software-users`. |
| `accessType` | `string` | `query` | No | The access level of a group. Valid values: 'site-admin', 'admin', 'user'. |
| `applicationKey` | `string` | `query` | No | The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":10,\"startAt\":0,\"total\":2,\"values\":[{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jdog-developers\"},{\"groupId\":\"6e87dc72-4f1f-421f-9382-2fee8b652487\",\"name\":\"juvenal-bot\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Browse users and groups permission is required to view groups.\"],\"errors\":{}}"
```

#### 500 - Returned if the group with the given access level can't be retrieved.

Example (application/json):
```json
"{\"errorMessages\":[\"Couldn't retrieve groups with the site-admin accessType.\"],\"errors\":{}}"
```

