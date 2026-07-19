# 13-Update playbook run owner [POST]

`POST /plugins/playbooks/api/v0/runs/{id}/owner`

Update playbook run owner

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose owner will be changed. |

### Request Body (application/json)

```json
{
  "owner_id": string (required), // The user ID of the new owner.
}
```
### Responses

#### 200 - Owner successfully changed.

#### 400 - 

#### 403 - 

#### 500 - 

