# 03-Retrieve model information [GET]

`GET /api/v4/admin/data_management/{model_name}`

Retrieves information about a data model in an instance. Only available to administrators.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `model_name` | `string` | `path` | Yes | See https://docs.gitlab.com/administration/admin_area/#data-management for the list of allowed values |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `identifiers` | `any` | `query` | No | The record identifiers to filter by |
| `checksum_state` | `string` | `query` | No | The checksum status of the records to filter by |
| `cursor` | `string` | `query` | No | Cursor for obtaining the next set of records |
| `sort` | `string` | `query` | No | Order of sorting |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "record_identifier": any,
  "model_class": string,
  "created_at": string,
  "file_size": integer,
  "checksum_information": {},
}
```

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Model Not Found

