# 02-List all feature flag definitions [GET]

`GET /api/v4/features/definitions`

Lists all feature flag definitions.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
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
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

