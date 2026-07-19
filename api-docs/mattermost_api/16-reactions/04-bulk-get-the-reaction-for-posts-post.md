# 04-Bulk get the reaction for posts [POST]

`POST /api/v4/posts/ids/reactions`

Get a list of reactions made by all users to a given post.
##### Permissions
Must have `read_channel` permission for the channel the post is in.

__Minimum server version__: 5.8


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Reactions retrieval successful

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

