# 51-Update a channel's moderation settings. [PUT]

`PUT /api/v4/channels/{channel_id}/moderations/patch`

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.22


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
{
  "name": string,
  "roles": {
    "guests": boolean,
    "members": boolean,
  },
}
```
### Responses

#### 200 - Patched successfully

Schema (application/json):
```json
[
  {
    "name": string,
    "roles": {
      "guests": {
        "value": boolean,
        "enabled": boolean,
      },
      "members": {
        "value": boolean,
        "enabled": boolean,
      },
    },
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

