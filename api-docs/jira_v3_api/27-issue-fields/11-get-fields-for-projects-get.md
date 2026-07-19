# 11-Get fields for projects [GET]

`GET /rest/api/3/projects/fields`

Returns a [paginated](#pagination) list of fields for the requested projects and work types.

Only fields that are available for the specified combination of projects and work types are returned. This endpoint allows filtering to specific fields if field IDs are provided.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `projectId` | `array` | `query` | Yes | The IDs of projects to return fields for. |
| `workTypeId` | `array` | `query` | Yes | The IDs of work types (issue types) to return fields for. |
| `fieldId` | `array` | `query` | No | The IDs of fields to return. If not provided, all fields are returned. |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "isLast": boolean, // Whether this is the last page.
  "maxResults": integer, // The maximum number of items that could be returned.
  "nextPage": string, // If there is another page of results, the URL of the next page.
  "self": string, // The URL of the page.
  "startAt": integer, // The index of the first item returned.
  "total": integer, // The number of items returned.
  "values": [
    {
      "description": string,
      "fieldId": string,
      "isRequired": boolean,
      "projectId": integer,
      "workTypeId": integer,
    }
  ], // The list of items.
}
```

#### 400 - Returned if the request parameters are invalid.

#### 401 - Returned if authentication is missing.

#### 403 - Returned if the user does not have permission to view the projects or work types.

#### 404 - Returned if the endpoint is not enabled via feature flag.

