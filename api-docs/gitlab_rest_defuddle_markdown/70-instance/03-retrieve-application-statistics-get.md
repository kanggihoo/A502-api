# 03-Retrieve application statistics [GET]

`GET /api/v4/application/statistics`

Retrieves the current application statistics for this GitLab instance.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "forks": integer, // Approximate number of repo forks
  "issues": integer, // Approximate number of issues
  "merge_requests": integer, // Approximate number of merge requests
  "notes": integer, // Approximate number of notes
  "snippets": integer, // Approximate number of snippets
  "ssh_keys": integer, // Approximate number of SSH keys
  "milestones": integer, // Approximate number of milestones
  "users": integer, // Approximate number of users
  "projects": integer, // Approximate number of projects
  "groups": integer, // Approximate number of projects
  "active_users": integer, // Number of active users
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

