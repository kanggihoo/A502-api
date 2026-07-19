# 12-Create a Cube query request [POST]

`POST /api/v4/projects/{project_id}/product_analytics/request/load`

Creates a query request to the Cube API for product analytics and generates an access token. Requires the `product_analytics_features` flag to be enabled.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `integer` | `path` | Yes | ID of the project to query |

### Request Body (application/json)

```json
{
  "query": {} (required), // A valid Cube query. See reference documentation: https://cube.dev/docs/query-format
  "queryType": string, // The query type. Currently only "multi" is supported.
  "include_token": boolean, // Whether to include the access token in the response. (Only required for funnel generation.)
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

