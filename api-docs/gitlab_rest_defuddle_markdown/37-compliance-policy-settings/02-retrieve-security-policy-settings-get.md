# 02-Retrieve security policy settings [GET]

`GET /api/v4/admin/security/compliance_policy_settings`

Retrieves the current security policy settings for this GitLab instance.

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

