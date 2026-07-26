# 03-Update a scheduled post [PUT]

`PUT /api/v4/posts/schedule/{scheduled_post_id}`

Updates a scheduled post
##### Permissions
Must have `create_post` permission for the channel where the scheduled post belongs to.
__Minimum server version__: 10.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scheduled_post_id` | `string` | `path` | Yes | ID of the scheduled post to update |

### Request Body (application/json)

```json
{
  "id": string (required), // ID of the scheduled post to update
  "channel_id": string (required), // The channel ID to post in
  "user_id": string (required), // The current user ID
  "scheduled_at": integer (required), // UNIX timestamp in milliseconds of the time when the scheduled post should be sent
  "message": string (required), // The message contents, can be formatted with Markdown
}
```
### Responses

#### 200 - Updated scheduled post

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

