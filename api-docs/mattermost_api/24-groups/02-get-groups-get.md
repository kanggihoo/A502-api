# 02-Get groups [GET]

`GET /api/v4/groups`

Retrieve a list of all groups not associated to a particular channel or team.

If you use `not_associated_to_team`, you must be a team admin for that particular team (permission to manage that team).

If you use `not_associated_to_channel`, you must be a channel admin for that particular channel (permission to manage that channel).

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of groups per page. |
| `q` | `string` | `query` | No | String to pattern match the `name` and `display_name` field. Will return all groups whose `name` and `display_name` field match any of the text. |
| `include_member_count` | `boolean` | `query` | No | Boolean which adds the `member_count` attribute to each group JSON object |
| `not_associated_to_team` | `string` | `query` | No | Team GUID which is used to return all the groups not associated to this team |
| `not_associated_to_channel` | `string` | `query` | No | Group GUID which is used to return all the groups not associated to this channel |
| `since` | `integer` | `query` | No | Only return groups that have been modified since the given Unix timestamp (in milliseconds). All modified groups, including deleted and created groups, will be returned.<br>__Minimum server version__: 5.24<br> |
| `filter_allow_reference` | `boolean` | `query` | No | Boolean which filters the group entries with the `allow_reference` attribute set. |

### Responses

#### 200 - Group list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "name": string,
    "display_name": string,
    "description": string,
    "source": string,
    "remote_id": string,
    "create_at": integer,
    "update_at": integer,
    "delete_at": integer,
    "has_syncables": boolean,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

