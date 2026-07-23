# 47-Set a channel's scheme [PUT]

`PUT /api/v4/channels/{channel_id}/scheme`

Set a channel's scheme, more specifically sets the scheme_id value of a channel record.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 4.10


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
{
  "scheme_id": string (required), // The ID of the scheme.
}
```
### Responses

#### 200 - Update channel scheme successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

