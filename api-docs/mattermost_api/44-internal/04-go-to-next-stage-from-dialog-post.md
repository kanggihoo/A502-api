# 04-Go to next stage from dialog [POST]

`POST /plugins/playbooks/api/v0/runs/{id}/next-stage-dialog`

This is an internal endpoint to go to the next stage via a confirmation dialog, submitted by a user in the webapp.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The PlaybookRun ID |

### Request Body (application/json)

```json
{
  "state": string, // String representation of the zero-based index of the stage to go to.
}
```
### Responses

#### 200 - Playbook run stage update.

#### 400 - 

#### 500 - 

