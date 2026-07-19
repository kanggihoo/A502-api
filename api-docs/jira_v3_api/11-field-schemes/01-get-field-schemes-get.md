# 01-Get field schemes [GET]

`GET /rest/api/3/config/fieldschemes`

REST endpoint for retrieving a paginated list of field association schemes with optional filtering.

This endpoint allows clients to fetch field association schemes with optional filtering by project IDs and text queries. The response includes scheme details with navigation links and filter metadata when applicable.

Filtering Behavior:

 *  When projectId or query parameters are provided, the response includes matchedFilters metadata showing which filters were applied.
 *  When no filters are applied, matchedFilters is omitted from individual scheme objects

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `array` | `query` | No | (optional) List of project IDs to filter schemes by. If not provided, schemes from all projects are returned. |
| `query` | `string` | `query` | No | (optional) Text filter for scheme name or description matching (case-insensitive). If not provided, no text filtering is applied. |
| `startAt` | `integer` | `query` | No | Zero-based index of the first item to return (default: 0) |
| `maxResults` | `integer` | `query` | No | Maximum number of items to return per page (default: 50, max: 100) |

### Responses

#### 200 - Pagianted list of field association schemes

Example (application/json):
```json
"{\"description\":\"Field Association Scheme test description\",\"fieldsCount\":5,\"id\":1000,\"isDefault\":false,\"links\":{\"associations\":\"rest/api/3/config/fieldschemes/10000/fields\",\"projects\":\"rest/api/3/config/fieldschemes/10000/projects\"},\"matchedFilters\":{\"projectIds\":[10001,10002],\"query\":\"query\"},\"name\":\"Field Association Scheme test name\"}"
```

#### 400 - Returned if the request parameters are invalid (e.g., negative startAt, maxResults exceeding limit).

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

