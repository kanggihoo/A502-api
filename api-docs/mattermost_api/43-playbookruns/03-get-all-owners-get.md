# 03-Get all owners [GET]

`GET /plugins/playbooks/api/v0/runs/owners`

Get the owners of all playbook runs, filtered by team.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `query` | Yes | ID of the team to filter by. |

### Responses

#### 200 - A list of owners.

Schema (application/json):
```json
[
  {
    "user_id": string (required), // A unique, 26 characters long, alphanumeric identifier for the owner.
    "username": string (required), // Owner's username.
  }
]
```

#### 400 - 

#### 403 - 

#### 500 - 

