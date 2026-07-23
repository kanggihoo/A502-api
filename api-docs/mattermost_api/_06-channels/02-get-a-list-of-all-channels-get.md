# 02-Get a list of all channels [GET]

`GET /api/v4/channels`

##### Permissions
`manage_system`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `not_associated_to_group` | `string` | `query` | No | A group id to exclude channels that are associated with that group via GroupChannel records. This can also be left blank with `not_associated_to_group=`. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of channels per page. |
| `exclude_default_channels` | `boolean` | `query` | No | Whether to exclude default channels (ex Town Square, Off-Topic) from the results. |
| `include_deleted` | `boolean` | `query` | No | Include channels that have been archived. This correlates to the `DeleteAt` flag being set in the database. |
| `include_total_count` | `boolean` | `query` | No | Appends a total count of returned channels inside the response object - ex: `{ "channels": [], "total_count" : 0 }`. |
| `exclude_policy_constrained` | `boolean` | `query` | No | If set to true, channels which are part of a data retention policy will be excluded. The `sysconsole_read_compliance` permission is required to use this parameter.<br>__Minimum server version__: 5.35 |

### Responses

#### 200 - Channel list retrieval successful

Schema (application/json):
```json
[
  any
]
```

#### 400 - 

#### 401 - 

#### 404 - 

