# 22-Acknowledge a post [POST]

`POST /api/v4/users/{user_id}/posts/{post_id}/ack`

Acknowledge a post that has a request for acknowledgements.
##### Permissions
Must have `read_channel` permission for the channel the post is in.<br/> Must be logged in as the user or have `edit_other_users` permission.

__Minimum server version__: 7.7


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `post_id` | `string` | `path` | Yes | Post GUID |

### Responses

#### 200 - Acknowledgement saved successfully

Schema (application/json):
```json
{
  "user_id": string, // The ID of the user that made this acknowledgement.
  "post_id": string, // The ID of the post to which this acknowledgement was made.
  "acknowledged_at": integer, // The time in milliseconds in which this acknowledgement was made.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

