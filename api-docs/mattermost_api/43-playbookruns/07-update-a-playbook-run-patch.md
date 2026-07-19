# 07-Update a playbook run [PATCH]

`PATCH /plugins/playbooks/api/v0/runs/{id}`

Update a playbook run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run to retrieve. |

### Request Body (application/json)

```json
{
  "name": string, // The new name of the playbook run. Must not be empty.
  "summary": string, // The new summary of the playbook run. Can be empty to clear the summary.
}
```
### Responses

#### 200 - Playbook run successfully updated.

#### 400 - 

#### 500 - 

