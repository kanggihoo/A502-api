# 09-Get field configuration issue type items [GET]

`GET /rest/api/3/fieldconfigurationscheme/mapping`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Returns a [paginated](#pagination) list of field configuration issue type items.

Only items used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `fieldConfigurationSchemeId` | `array` | `query` | No | The list of field configuration scheme IDs. To include multiple field configuration schemes separate IDs with ampersand: `fieldConfigurationSchemeId=10000&fieldConfigurationSchemeId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":5,\"values\":[{\"fieldConfigurationSchemeId\":\"10020\",\"issueTypeId\":\"10000\",\"fieldConfigurationId\":\"10010\"},{\"fieldConfigurationSchemeId\":\"10020\",\"issueTypeId\":\"10001\",\"fieldConfigurationId\":\"10010\"},{\"fieldConfigurationSchemeId\":\"10021\",\"issueTypeId\":\"10002\",\"fieldConfigurationId\":\"10000\"},{\"fieldConfigurationSchemeId\":\"10022\",\"issueTypeId\":\"default\",\"fieldConfigurationId\":\"10011\"},{\"fieldConfigurationSchemeId\":\"10023\",\"issueTypeId\":\"default\",\"fieldConfigurationId\":\"10000\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if no field configuration schemes are found.

