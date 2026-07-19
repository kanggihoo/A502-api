# 11-Update a playbook run's status [POST]

`POST /plugins/playbooks/api/v0/runs/{id}/status`

Update a playbook run's status

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run to update. |

### Request Body (application/json)

```json
{
  "message": string (required), // The status update message.
  "reminder": number, // The number of seconds until the system will send a reminder to the owner to update the status. No reminder will be scheduled if reminder is 0 or omitted.
}
```
### Responses

#### 200 - Playbook run updated.

#### 400 - 

#### 403 - 

#### 500 - 

