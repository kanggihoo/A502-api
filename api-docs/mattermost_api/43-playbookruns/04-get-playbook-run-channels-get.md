# 04-Get playbook run channels [GET]

`GET /plugins/playbooks/api/v0/runs/channels`

Get all channels associated with a playbook run, filtered by team, status, owner, name and/or members, and sorted by ID, name, status, creation date, end date, team, or owner ID.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `query` | Yes | ID of the team to filter by. |
| `sort` | `string` | `query` | No | Field to sort the returned channels by, according to their playbook run. |
| `direction` | `string` | `query` | No | Direction (ascending or descending) followed by the sorting of the playbook runs associated to the channels. |
| `status` | `string` | `query` | No | The returned list will contain only the channels whose playbook run has this status. |
| `owner_user_id` | `string` | `query` | No | The returned list will contain only the channels whose playbook run is commanded by this user. |
| `search_term` | `string` | `query` | No | The returned list will contain only the channels associated to a playbook run whose name contains the search term. |
| `participant_id` | `string` | `query` | No | The returned list will contain only the channels associated to a playbook run for which the given user is a participant. |

### Responses

#### 200 - Channel IDs.

Schema (application/json):
```json
[
  string
]
```

#### 400 - 

#### 403 - 

#### 500 - 

