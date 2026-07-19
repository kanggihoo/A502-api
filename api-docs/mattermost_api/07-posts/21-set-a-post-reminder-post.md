# 21-Set a post reminder [POST]

`POST /api/v4/users/{user_id}/posts/{post_id}/reminder`

Set a reminder for the user for the post.
##### Permissions
Must have `read_channel` permission for the channel the post is in.

__Minimum server version__: 7.2


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `post_id` | `string` | `path` | Yes | Post GUID |

### Request Body (application/json)

```json
{
  "target_time": integer (required), // Target time for the reminder
}
```
### Responses

#### 200 - Reminder set successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

