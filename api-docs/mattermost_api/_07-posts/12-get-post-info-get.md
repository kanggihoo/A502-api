# 12-Get post info [GET]

`GET /api/v4/posts/{post_id}/info`

Get additional metadata and access information for a post.
##### Permissions
Must be able to access the post's team and channel context.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | Post ID |

### Responses

#### 200 - Post info retrieval successful

Schema (application/json):
```json
{
  "channel_id": string, // The ID of the channel containing the post.
  "channel_type": string, // The type of the channel containing the post.
  "channel_display_name": string, // The display name of the channel containing the post.
  "has_joined_channel": boolean, // Whether the requesting user is already a member of the channel.
  "team_id": string, // The ID of the team containing the channel, if applicable.
  "team_type": string, // The type of the team containing the channel, if applicable.
  "team_display_name": string, // The display name of the team containing the channel, if applicable.
  "has_joined_team": boolean, // Whether the requesting user is already a member of the team.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

