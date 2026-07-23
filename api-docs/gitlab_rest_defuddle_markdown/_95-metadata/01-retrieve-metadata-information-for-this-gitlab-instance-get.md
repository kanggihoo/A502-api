# 01-Retrieve metadata information for this GitLab instance [GET]

`GET /api/v4/metadata`

Retrieves metadata information for the GitLab instance.

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

