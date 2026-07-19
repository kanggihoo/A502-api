# 09-Delete a property field for a playbook [DELETE]

`DELETE /plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}`

Delete a property field for a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook containing the property field. |
| `field_id` | `string` | `path` | Yes | ID of the property field to delete. |

### Responses

#### 204 - Property field deleted successfully.

#### 403 - 

#### 500 - 

