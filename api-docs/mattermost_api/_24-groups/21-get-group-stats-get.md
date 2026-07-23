# 21-Get group stats [GET]

`GET /api/v4/groups/{group_id}/stats`

Retrieve the stats of a given group.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.26


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 200 - Group stats retrieval successful

Schema (application/json):
```json
{
  "group_id": string,
  "total_member_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

