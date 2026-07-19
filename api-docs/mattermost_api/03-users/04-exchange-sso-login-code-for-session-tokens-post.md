# 04-Exchange SSO login code for session tokens [POST]

`POST /api/v4/users/login/sso/code-exchange`

Exchange a short-lived login_code for session tokens using SAML code exchange (mobile SSO flow).
**Deprecated:** This endpoint is deprecated and will be removed in a future release. Mobile clients should use the direct SSO callback flow instead.
##### Permissions
No permission required.


### Request Body (application/json)

```json
{
  "login_code": string (required), // Short-lived one-time code from SSO callback
  "code_verifier": string (required), // SAML verifier to prove code possession
  "state": string (required), // State parameter to prevent CSRF attacks
}
```
### Responses

#### 200 - Code exchange successful

Schema (application/json):
```json
{
  "token": string, // Session token for authentication
  "csrf": string, // CSRF token for request validation
}
```

#### 400 - 

#### 403 - 

#### 410 - Endpoint is deprecated and disabled

