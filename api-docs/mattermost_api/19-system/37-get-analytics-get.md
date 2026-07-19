# 37-Get analytics [GET]

`GET /api/v4/analytics/old`

Get some analytics data about the system. This endpoint uses the old format, the `/analytics` route is reserved for the new format when it gets implemented.

The returned JSON changes based on the `name` query parameter but is always key/value pairs.

__Minimum server version__: 4.0

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | No | Possible values are "standard", "bot_post_counts_day", "post_counts_day", "user_counts_with_posts_day" or "extra_counts" |
| `team_id` | `string` | `query` | No | The team ID to filter the data by |

### Responses

#### 200 - Analytics retrieval successful

#### 400 - 

#### 401 - 

#### 403 - 

