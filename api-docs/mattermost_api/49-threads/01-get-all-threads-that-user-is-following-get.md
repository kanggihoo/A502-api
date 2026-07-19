# 01-Get all threads that user is following [GET]

`GET /api/v4/users/{user_id}/teams/{team_id}/threads`

Get all threads that user is following

__Minimum server version__: 5.29

##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `team_id` | `string` | `path` | Yes | The ID of the team in which the thread is. |
| `since` | `integer` | `query` | No | Since filters the threads based on their LastUpdateAt timestamp. |
| `deleted` | `boolean` | `query` | No | Deleted will specify that even deleted threads should be returned (For mobile sync). |
| `extended` | `boolean` | `query` | No | Extended will enrich the response with participant details. |
| `page` | `integer` | `query` | No | Page specifies which part of the results to return, by per_page. |
| `per_page` | `integer` | `query` | No | The size of the returned chunk of results. |
| `totalsOnly` | `boolean` | `query` | No | Setting this to true will only return the total counts. |
| `threadsOnly` | `boolean` | `query` | No | Setting this to true will only return threads. |

### Responses

#### 200 - User's thread retrieval successful

Schema (application/json):
```json
{
  "total": integer, // Total number of threads (used for paging)
  "threads": [
    {
      "id": string, // ID of the post that is this thread's root
      "reply_count": integer, // number of replies in this thread
      "last_reply_at": integer, // timestamp of the last post to this thread
      "last_viewed_at": integer, // timestamp of the last time the user viewed this thread
      "participants": [
        {
          "id": string,
          "create_at": integer, // The time in milliseconds a user was created
          "update_at": integer, // The time in milliseconds a user was last updated
          "delete_at": integer, // The time in milliseconds a user was deleted
          "username": string,
          "first_name": string,
          "last_name": string,
          "nickname": string,
          "email": string,
          "email_verified": boolean,
          "auth_service": string,
          "roles": string,
          "locale": string,
          "notify_props": {
            "email": string, // Set to "true" to enable email notifications, "false" to disable. Defaults to "true".
            "push": string, // Set to "all" to receive push notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "mention".
            "desktop": string, // Set to "all" to receive desktop notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "all".
            "desktop_sound": string, // Set to "true" to enable sound on desktop notifications, "false" to disable. Defaults to "true".
            "mention_keys": string, // A comma-separated list of words to count as mentions. Defaults to username and @username.
            "channel": string, // Set to "true" to enable channel-wide notifications (@channel, @all, etc.), "false" to disable. Defaults to "true".
            "first_name": string, // Set to "true" to enable mentions for first name. Defaults to "true" if a first name is set, "false" otherwise.
            "auto_responder_message": string, // The message sent to users when they are auto-responded to. Defaults to "".
            "push_threads": string, // Set to "all" to enable mobile push notifications for followed threads and "none" to disable. Defaults to "all".
            "comments": string, // Set to "any" to enable notifications for comments to any post you have replied to, "root" for comments on your posts, and "never" to disable. Only affects users with collapsed reply threads disabled. Defaults to "never".
            "desktop_threads": string, // Set to "all" to enable desktop notifications for followed threads and "none" to disable. Defaults to "all".
            "email_threads": string, // Set to "all" to enable email notifications for followed threads and "none" to disable. Defaults to "all".
          },
          "props": {},
          "last_password_update": integer,
          "last_picture_update": integer,
          "failed_attempts": integer,
          "mfa_active": boolean,
          "timezone": {
            "useAutomaticTimezone": string, // Set to "true" to use the browser/system timezone, "false" to set manually. Defaults to "true".
            "manualTimezone": string, // Value when setting manually the timezone, i.e. "Europe/Berlin".
            "automaticTimezone": string, // This value is set automatically when the "useAutomaticTimezone" is set to "true".
          },
          "terms_of_service_id": string, // ID of accepted terms of service, if any. This field is not present if empty.
          "terms_of_service_create_at": integer, // The time in milliseconds the user accepted the terms of service
        }
      ], // list of users participating in this thread. only includes IDs unless 'extended' was set to 'true'
      "post": {
        "id": string,
        "create_at": integer, // The time in milliseconds a post was created
        "update_at": integer, // The time in milliseconds a post was last updated
        "delete_at": integer, // The time in milliseconds a post was deleted
        "edit_at": integer,
        "user_id": string,
        "channel_id": string,
        "root_id": string,
        "original_id": string,
        "message": string,
        "type": string,
        "props": {},
        "hashtag": string,
        "file_ids": [
          string
        ],
        "pending_post_id": string,
        "metadata": {
          "embeds": [
            {
              "type": enum("image" | "message_attachment" | "opengraph" | "link"), // The type of content that is embedded in this point.
              "url": string, // The URL of the embedded content, if one exists.
              "data": {}, // Any additional information about the embedded content. Only used at this time to store OpenGraph metadata. This field will be null for non-OpenGraph embeds. 
            }
          ], // Information about content embedded in the post including OpenGraph previews, image link previews, and message attachments. This field will be null if the post does not contain embedded content. 
          "emojis": [
            {
              "id": string, // The ID of the emoji
              "creator_id": string, // The ID of the user that made the emoji
              "name": string, // The name of the emoji
              "create_at": integer, // The time in milliseconds the emoji was made
              "update_at": integer, // The time in milliseconds the emoji was last updated
              "delete_at": integer, // The time in milliseconds the emoji was deleted
            }
          ], // The custom emojis that appear in this point or have been used in reactions to this post. This field will be null if the post does not contain custom emojis. 
          "files": [
            {
              "id": string, // The unique identifier for this file
              "user_id": string, // The ID of the user that uploaded this file
              "post_id": string, // If this file is attached to a post, the ID of that post
              "create_at": integer, // The time in milliseconds a file was created
              "update_at": integer, // The time in milliseconds a file was last updated
              "delete_at": integer, // The time in milliseconds a file was deleted
              "name": string, // The name of the file
              "extension": string, // The extension at the end of the file name
              "size": integer, // The size of the file in bytes
              "mime_type": string, // The MIME type of the file
              "width": integer, // If this file is an image, the width of the file
              "height": integer, // If this file is an image, the height of the file
              "has_preview_image": boolean, // If this file is an image, whether or not it has a preview-sized version
            }
          ], // The FileInfo objects for any files attached to the post. This field will be null if the post does not have any file attachments. 
          "images": {}, // An object mapping the URL of an external image to an object containing the dimensions of that image. This field will be null if the post or its embedded content does not reference any external images. 
          "reactions": [
            {
              "user_id": string, // The ID of the user that made this reaction
              "post_id": string, // The ID of the post to which this reaction was made
              "emoji_name": string, // The name of the emoji that was used for this reaction
              "create_at": integer, // The time in milliseconds this reaction was made
            }
          ], // Any reactions made to this point. This field will be null if no reactions have been made to this post. 
          "priority": any, // Post priority set for this post. This field will be null if no priority metadata has been set. 
          "acknowledgements": [
            {
              "user_id": string, // The ID of the user that made this acknowledgement.
              "post_id": string, // The ID of the post to which this acknowledgement was made.
              "acknowledged_at": integer, // The time in milliseconds in which this acknowledgement was made.
            }
          ], // Any acknowledgements made to this point. 
        },
      },
    }
  ], // Array of threads
}
```

#### 400 - 

#### 401 - 

#### 404 - 

