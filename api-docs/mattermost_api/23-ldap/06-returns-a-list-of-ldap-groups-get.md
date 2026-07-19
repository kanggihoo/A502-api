# 06-Returns a list of LDAP groups [GET]

`GET /api/v4/ldap/groups`

##### Permissions
Must have `manage_system` permission.
__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `q` | `string` | `query` | No | Search term |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of users per page. per page. |

### Responses

#### 200 - LDAP group page retrieval successful

Schema (application/json):
```json
[
  {
    "count": number, // Total number of groups
    "groups": [
      {
        "has_syncables": boolean,
        "mattermost_group_id": string,
        "primary_key": string,
        "name": string,
      }
    ],
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

