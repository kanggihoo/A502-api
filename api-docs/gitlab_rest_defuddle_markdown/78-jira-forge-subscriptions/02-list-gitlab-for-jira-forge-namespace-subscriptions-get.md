# 02-List GitLab for Jira (Forge) namespace subscriptions [GET]

`GET /api/v4/integrations/jira_forge/subscriptions`

Lists the GitLab namespaces subscribed to the Forge installation.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "created_at": string,
  "unlink_path": string,
  "group": {
    "name": string,
    "avatar_url": string,
    "full_name": string,
    "description": string,
  },
}
```

#### 401 - Unauthorized

