# 03-Update security policy settings [PUT]

`PUT /api/v4/admin/security/compliance_policy_settings`

Updates the security policy settings for this GitLab instance.

### Request Body (application/json)

```json
{
  "csp_namespace_id": integer (required), // ID of the group designated to centrally manage security policies and compliance frameworks.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "csp_namespace_id": integer,
}
```

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 422 - 422 Unprocessable Entity

