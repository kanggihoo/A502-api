# 03-End a playbook run from dialog [POST]

`POST /plugins/playbooks/api/v0/runs/{id}/end`

This is an internal endpoint to end a playbook run via a confirmation dialog, submitted by a user in the webapp.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run to end. |

### Responses

#### 200 - Playbook run ended

#### 500 - 

