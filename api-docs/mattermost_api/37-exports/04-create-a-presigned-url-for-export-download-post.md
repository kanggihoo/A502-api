# 04-Create a presigned URL for export download [POST]

`POST /api/v4/exports/{export_name}/presign-url`

Creates a presigned URL for downloading an export file.

__Minimum server version__: 5.33

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `export_name` | `string` | `path` | Yes | The name of the export file |

### Responses

#### 200 - Presigned URL created successfully

Schema (application/json):
```json
{
  "url": string,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

