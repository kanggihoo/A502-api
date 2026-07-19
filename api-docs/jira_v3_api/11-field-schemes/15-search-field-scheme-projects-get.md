# 15-Search field scheme projects [GET]

`GET /rest/api/3/config/fieldschemes/{id}/projects`

REST Endpoint for searching for projects belonging to a given field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The starting index of the returned projects. Base index: 0. |
| `maxResults` | `integer` | `query` | No | The maximum number of projects to return per page, maximum allowed value is 100. |
| `projectId` | `array` | `query` | No | The project Ids to filter by, if empty then all projects belonging to a field association scheme will be returned |
| `id` | `integer` | `path` | Yes | The scheme id to search for associated projects |

### Responses

#### 200 - Returns a paginated list of projects associated with the field association scheme, matching the specified filter criteria.

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
      "avatarUrls": {},
      "deleted": boolean,
      "id": string,
      "key": string,
      "name": string,
    }
  ], // The list of items.
}
```

#### 400 - 400 response

Schema (application/json):
```json
any
```

#### 401 - 401 response

Schema (application/json):
```json
any
```

#### 403 - 403 response

Schema (application/json):
```json
any
```

#### 404 - 404 response

Schema (application/json):
```json
any
```

