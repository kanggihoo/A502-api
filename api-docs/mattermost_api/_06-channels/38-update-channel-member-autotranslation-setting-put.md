# 38-Update channel member autotranslation setting [PUT]

`PUT /api/v4/channels/{channel_id}/members/{user_id}/autotranslation`

Update a user's autotranslation setting for a channel. This controls whether messages in the channel should not be automatically translated for the user. By default, autotranslations are enabled for all users if the channel is enabled for autotranslation.
##### Permissions
Must be logged in as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "autotranslation_disabled": boolean (required), // Whether to disable autotranslation for the user in this channel
}
```
### Responses

#### 200 - Channel member autotranslation setting update successful

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

