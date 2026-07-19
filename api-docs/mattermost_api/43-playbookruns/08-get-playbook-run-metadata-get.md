# 08-Get playbook run metadata [GET]

`GET /plugins/playbooks/api/v0/runs/{id}/metadata`

Get playbook run metadata

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose metadata will be retrieved. |

### Responses

#### 200 - Playbook run metadata.

Schema (application/json):
```json
{
  "channel_name": string, // Name of the channel associated to the playbook run.
  "channel_display_name": string, // Display name of the channel associated to the playbook run.
  "team_name": string, // Name of the team the playbook run is in.
  "num_members": integer, // Number of users that have been members of the playbook run at any point.
  "total_posts": integer, // Number of posts in the channel associated to the playbook run.
}
```

#### 403 - 

#### 500 - 

