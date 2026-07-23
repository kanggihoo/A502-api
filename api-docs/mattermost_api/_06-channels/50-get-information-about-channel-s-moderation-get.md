# 50-Get information about channel's moderation. [GET]

`GET /api/v4/channels/{channel_id}/moderations`

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.22


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Retreived successfully

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

