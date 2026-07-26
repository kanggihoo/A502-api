# 32-Get audits [GET]

`GET /api/v4/audits`

Get a page of audits for all users on the system, selected with `page` and `per_page` query parameters.
##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of audits per page. |

### Responses

#### 200 - Audits retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a audit was created
    "user_id": string,
    "action": string,
    "extra_info": string,
    "ip_address": string,
    "session_id": string,
  }
]
```

#### 403 - 

