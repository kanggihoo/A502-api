# 09-Register OAuth client using Dynamic Client Registration [POST]

`POST /api/v4/oauth/apps/register`

Register an OAuth 2.0 client application using Dynamic Client Registration (DCR) as defined in RFC 7591. This endpoint allows clients to register without requiring administrative approval.
##### Permissions
No authentication required. This endpoint implements the OAuth 2.0 Dynamic Client Registration Protocol and can be called by unauthenticated clients.
##### Notes
- This endpoint follows RFC 7591 (OAuth 2.0 Dynamic Client Registration Protocol) - The `client_uri` field, when provided, will be mapped to the OAuth app's homepage - All registered clients are marked as dynamically registered - Dynamic client registration must be enabled in system settings


### Request Body (application/json)

```json
{
  "redirect_uris": [
    string
  ] (required), // Array of redirection URI strings for use in redirect-based flows such as the authorization code and implicit flows
  "client_name": string, // Human-readable string name of the client to be presented to the end-user during authorization
  "client_uri": string, // URL string of a web page providing information about the client
}
```
### Responses

#### 201 - Client registration successful

Schema (application/json):
```json
{
  "client_id": string, // OAuth 2.0 client identifier string
  "client_secret": string, // OAuth 2.0 client secret string
  "redirect_uris": [
    string
  ], // Array of the registered redirection URI strings
  "token_endpoint_auth_method": enum("client_secret_post" | "none"), // String indicator of the requested authentication method for the token endpoint
  "grant_types": [
    string
  ], // Array of OAuth 2.0 grant type strings that the client can use at the token endpoint
  "response_types": [
    string
  ], // Array of the OAuth 2.0 response type strings that the client can use at the authorization endpoint
  "scope": string, // Space-separated list of scope values that the client can use when requesting access tokens
  "client_name": string, // Human-readable string name of the client to be presented to the end-user during authorization
  "client_uri": string, // URL string of a web page providing information about the client
}
```

#### 400 - 

#### 501 - 

