# 01-Execute a GLQL query [POST]

`POST /api/v4/glql`

Executes a GLQL query to search and filter GitLab resources.

### Request Body (application/json)

```json
{
  "glql_yaml": string (required), // The full GLQL code block containing YAML configuration and query
  "after": string, // Cursor for forward pagination. Use the `endCursor` from previous response to fetch the next page
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "data": {
    "count": integer, // Number of found items
    "nodes": [
      [
        any
      ]
    ], // The list of found items
    "pageInfo": {
      "endCursor": string, // Cursor for the last item
      "hasNextPage": boolean, // Whether there are more items
      "hasPreviousPage": boolean, // Whether there are previous items
      "startCursor": string, // Cursor for the first item
    }, // Pagination information
  }, // Query result data containing count, nodes, and pagination info
  "error": string, // Error message if query failed
  "fields": [
    {
      "key": string, // Unique field key
      "label": string, // Human-readable field label
      "name": string, // Underlying name of field, often the same as `key`, but it may be different if one type of field has multiple possible keys. Example `created` and `createdAt`
    }
  ], // Field definitions for the query results
  "success": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 429 - Too Many Requests

#### 500 - Internal server error

