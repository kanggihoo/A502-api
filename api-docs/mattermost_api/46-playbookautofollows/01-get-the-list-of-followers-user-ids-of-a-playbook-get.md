# 01-Get the list of followers' user IDs of a playbook [GET]

`GET /plugins/playbooks/api/v0/playbooks/{id}/autofollows`

Get the list of followers' user IDs of a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook to retrieve followers from. |

### Responses

#### 200 - List of the user IDs who follow the playbook.

Schema (application/json):
```json
{
  "total_count": integer, // The total number of users who marked this playbook to auto-follow runs.
  "items": [
    string
  ], // The user IDs of who marked this playbook to auto-follow.
}
```

#### 403 - 

#### 500 - 

