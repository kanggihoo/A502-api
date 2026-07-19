# 01-List all experiments [GET]

`GET /api/v4/experiments`

Lists all experiments on the GitLab instance. Each experiment has an `enabled` status that indicates whether the experiment is enabled globally, or only in specific contexts.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "definition": {
    "name": string,
    "feature_issue_url": string,
    "introduced_by_url": string,
    "rollout_issue_url": string,
    "milestone": string,
    "log_state_changes": boolean,
    "type": string,
    "group": string,
    "default_enabled": boolean,
    "intended_to_rollout_by": string,
  },
  "current_status": {
    "state": string,
    "gates": {
      "key": string,
      "value": integer,
    },
  },
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

