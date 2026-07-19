# 07-Get projects with field schemes [GET]

`GET /rest/api/3/config/fieldschemes/projects`

Get projects with field association schemes. This will be a temporary API but useful when transitioning from the legacy field configuration APIs to the new ones.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The starting index of the returned projects. Base index: 0. |
| `maxResults` | `integer` | `query` | No | The maximum number of projects to return per page, maximum allowed value is 100. |
| `projectId` | `array` | `query` | Yes | List of project ids to filter the results by. |

### Responses

#### 200 - Returns the list of project with field association schemes.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":3,\"startAt\":0,\"total\":3,\"values\":[{\"projectId\":10000,\"schemeId\":1},{\"projectId\":10001,\"schemeId\":1},{\"projectId\":10002,\"schemeId\":2}]}"
```

#### 400 - Returned if the request is invalid.

Schema (application/json):
```json
{}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
any
```

#### 403 - Returned if the user does not have the required permissions.

Schema (application/json):
```json
any
```

#### 404 - Returned if the feature flag is disabled.

Schema (application/json):
```json
any
```

