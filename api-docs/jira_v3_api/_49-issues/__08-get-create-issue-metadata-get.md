# 08-Get create issue metadata [GET]

`GET /rest/api/3/issue/createmeta`

Returns details of projects, issue types within projects, and, when requested, the create screen fields for each issue type for the user. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

Deprecated, see [Create Issue Meta Endpoint Deprecation Notice](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1304).

The request can be restricted to specific projects or issue types using the query parameters. The response will contain information for the valid projects, issue types, or project and issue type combinations requested. Note that invalid project, issue type, or project and issue type combinations do not generate errors.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIds` | `array` | `query` | No | List of project IDs. This parameter accepts a comma-separated list. Multiple project IDs can also be provided using an ampersand-separated list. For example, `projectIds=10000,10001&projectIds=10020,10021`. This parameter may be provided with `projectKeys`. |
| `projectKeys` | `array` | `query` | No | List of project keys. This parameter accepts a comma-separated list. Multiple project keys can also be provided using an ampersand-separated list. For example, `projectKeys=proj1,proj2&projectKeys=proj3`. This parameter may be provided with `projectIds`. |
| `issuetypeIds` | `array` | `query` | No | List of issue type IDs. This parameter accepts a comma-separated list. Multiple issue type IDs can also be provided using an ampersand-separated list. For example, `issuetypeIds=10000,10001&issuetypeIds=10020,10021`. This parameter may be provided with `issuetypeNames`. |
| `issuetypeNames` | `array` | `query` | No | List of issue type names. This parameter accepts a comma-separated list. Multiple issue type names can also be provided using an ampersand-separated list. For example, `issuetypeNames=name1,name2&issuetypeNames=name3`. This parameter may be provided with `issuetypeIds`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about issue metadata in the response. This parameter accepts `projects.issuetypes.fields`, which returns information about the fields in the issue creation screen for each issue type. Fields hidden from the screen are not returned. Use the information to populate the `fields` and `update` fields in [Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"projects\":[{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000&avatarId=10011\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000&avatarId=10011\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000&avatarId=10011\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?pid=10000&avatarId=10011\"},\"id\":\"10000\",\"issuetypes\":[{\"description\":\"An error in the code\",\"fields\":{\"issuetype\":{\"allowedValues\":[\"set\"],\"autoCompleteUrl\":\"issuetype\",\"hasDefaultValue\":false,\"key\":\"issuetype\",\"name\":\"Issue Type\",\"required\":true}},\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/issuetypes/bug.png\",\"id\":\"1\",\"name\":\"Bug\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false}],\"key\":\"ED\",\"name\":\"Edison Project\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/ED\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

