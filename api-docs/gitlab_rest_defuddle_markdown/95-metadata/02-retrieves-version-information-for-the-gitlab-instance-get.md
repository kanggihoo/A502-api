# 02-Retrieves version information for the GitLab instance [GET]

`GET /api/v4/version`

This feature was introduced in GitLab 8.13 and deprecated in 15.5. We recommend you instead use the Metadata API.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "version": string,
  "revision": string,
  "kas": {},
  "enterprise": boolean,
}
```

#### 401 - Unauthorized

