# 49-Channel members counts for each group that has atleast one member in the channel [GET]

`GET /api/v4/channels/{channel_id}/member_counts_by_group`

Returns a set of ChannelMemberCountByGroup objects which contain a `group_id`, `channel_member_count` and a `channel_member_timezones_count`.
##### Permissions
Must have `read_channel` permission for the given channel.
__Minimum server version__: 5.24


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `include_timezones` | `boolean` | `query` | No | Defines if member timezone counts should be returned or not |

### Responses

#### 200 - Successfully returns member counts by group for the given channel.

#### 400 - 

#### 401 - 

#### 403 - 

