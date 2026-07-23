# 08-Get OAuth 2.0 Authorization Server Metadata [GET]

`GET /.well-known/oauth-authorization-server`

Get the OAuth 2.0 Authorization Server Metadata as defined in RFC 8414. This endpoint provides metadata about the OAuth 2.0 authorization server's configuration, including supported endpoints, grant types, response types, and authentication methods.
##### Permissions
No authentication required. This endpoint is publicly accessible to allow OAuth clients to discover the authorization server's configuration.
##### Notes
- This endpoint implements RFC 8414 (OAuth 2.0 Authorization Server Metadata) - The metadata is dynamically generated based on the server's configuration - OAuth Service Provider must be enabled in system settings for this endpoint to be available


### Responses

#### 200 - Metadata retrieval successful

Schema (application/json):
```json
{
  "issuer": string (required), // The authorization server's issuer identifier, which is a URL that uses the "https" scheme
  "authorization_endpoint": string, // URL of the authorization server's authorization endpoint
  "token_endpoint": string, // URL of the authorization server's token endpoint
  "response_types_supported": [
    string
  ] (required), // JSON array containing a list of the OAuth 2.0 response_type values that this authorization server supports
  "registration_endpoint": string, // URL of the authorization server's OAuth 2.0 Dynamic Client Registration endpoint
  "scopes_supported": [
    string
  ], // JSON array containing a list of the OAuth 2.0 scope values that this authorization server supports
  "grant_types_supported": [
    string
  ], // JSON array containing a list of the OAuth 2.0 grant type values that this authorization server supports
  "token_endpoint_auth_methods_supported": [
    string
  ], // JSON array containing a list of client authentication methods supported by the token endpoint
  "code_challenge_methods_supported": [
    string
  ], // JSON array containing a list of PKCE code challenge methods supported by this authorization server
}
```

#### 501 - OAuth Service Provider is not enabled

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

