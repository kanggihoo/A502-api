# 01-Creates a scheduled post [POST]

`POST /api/v4/posts/schedule`

Creates a scheduled post
##### Permissions
Must have `create_post` permission for the channel the post is being created in.
__Minimum server version__: 10.3


### Request Body (application/json)

```json
{
  "scheduled_at": integer (required), // UNIX timestamp in milliseconds of the time when the scheduled post should be sent
  "channel_id": string (required), // The channel ID to post in
  "message": string (required), // The message contents, can be formatted with Markdown
  "root_id": string, // The post ID to comment on
  "file_ids": [
    any
  ], // A list of file IDs to associate with the post. Note that posts are limited to 5 files maximum. Please use additional posts for more files.
  "props": {}, // A general JSON property bag to attach to the post
}
```
### Responses

#### 200 - Created scheduled post

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

