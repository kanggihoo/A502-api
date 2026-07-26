# 01-Upsert synced draft [POST]

`POST /api/v4/drafts`

Create or update a synced draft for the current user.
##### Permissions
Must be authenticated, have permission to create posts in the channel, and synced drafts must be enabled.


### Request Body (application/json)

```json
{
  "channel_id": string (required),
  "root_id": string,
  "message": string (required), // Draft message. Set to an empty string to delete the draft.
  "type": string,
  "props": {},
  "file_ids": [
    string
  ],
  "priority": {
    "priority": enum("" | "important" | "urgent"), // The priority label of a post, either empty, important, or urgent.
    "requested_ack": boolean, // Whether the post author has requested acknowledgements.
    "persistent_notifications": boolean, // Whether persistent notifications are enabled for the post.
  },
}
```
### Responses

#### 201 - Draft upsert successful. Returns `null` when an empty message deletes the draft.

Schema (application/json):
```json
any
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

