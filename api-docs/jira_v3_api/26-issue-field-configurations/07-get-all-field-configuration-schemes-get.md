# 07-Get all field configuration schemes [GET]

`GET /rest/api/3/fieldconfigurationscheme`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Returns a [paginated](#pagination) list of field configuration schemes.

Only field configuration schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of field configuration scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":10,\"startAt\":0,\"total\":3,\"values\":[{\"id\":\"10000\",\"name\":\"Field Configuration Scheme for Bugs\",\"description\":\"This field configuration scheme is for bugs only.\"},{\"id\":\"10001\",\"name\":\"Field Configuration Scheme for software related projects\",\"description\":\"We can use this one for software projects.\"},{\"id\":\"10002\",\"name\":\"Field Configuration Scheme for Epics\",\"description\":\"Use this one for Epic issue type.\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permissions.

