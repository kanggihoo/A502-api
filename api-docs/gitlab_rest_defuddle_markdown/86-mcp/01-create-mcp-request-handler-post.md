# 01-Create MCP request handler [POST]

`POST /api/v4/mcp`

Handles Model Context Protocol requests

### Request Body (application/json)

```json
{
  "jsonrpc": enum("2.0") (required), // JSON-RPC protocol version identifier. Must be `2.0`.
  "method": string (required), // Name of the JSON-RPC method invoked on the MCP server.
  "id": string, // ID of the JSON-RPC request returned in the response.
  "params": any,
}
```
### Responses

#### 201 - Created

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

