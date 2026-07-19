# 01-List all broadcast messages [GET]

`GET /api/v4/broadcast_messages`

Lists all broadcast messages for the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "message": string,
  "starts_at": string,
  "ends_at": string,
  "color": string,
  "font": string,
  "target_access_levels": [
    any
  ],
  "target_path": string,
  "broadcast_type": string,
  "theme": string,
  "dismissable": boolean,
  "active": boolean,
}
```

#### 400 - Bad Request

