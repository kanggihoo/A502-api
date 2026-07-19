# 01-Retrieve information about a model record [GET]

`GET /api/v4/admin/data_management/{model_name}/{record_identifier}`

Retrieves information about a specified model record. Only available to administrators.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `model_name` | `string` | `path` | Yes | See https://docs.gitlab.com/administration/admin_area/#data-management for the list of allowed values |
| `record_identifier` | `any` | `path` | Yes | The identifier of the model record |

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

