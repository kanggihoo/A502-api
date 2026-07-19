# 01-Issue a short-lived JWT for a single modular-service audience [POST]

`POST /api/v4/token_exchange`

Issues a short-lived RS256 JWT scoped to one modular-service audience (such as the Artifact Registry). Claims include the requesting user id (sub), organization id, and deployment realm (saas / self-managed). Presented to the corresponding backend and verified against the instance JWKS.

### Request Body (application/json)

```json
{
  "audience": enum("gitlab-artifact-registry") (required), // Target service audience (e.g. gitlab-artifact-registry)
  "expires_in": integer, // Requested token lifetime in seconds. Defaults to 300; cap is 43200. Pending appsec review of client-controlled TTL.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

