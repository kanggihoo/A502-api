# 01-Get content flagging configuration [GET]

`GET /api/v4/content_flagging/flag/config`

Returns the configuration for content flagging, including the list of available reasons for flagging content. This data is used to gather details from the user when they flag content.
An enterprise advanced license is required.


### Responses

#### 200 - Configuration retrieved successfully

Schema (application/json):
```json
{
  "reasons": [
    string
  ], // List of reasons for flagging content
  "reporter_comment_required": boolean, // Indicates if a comment from the reporter is required when flagging content
}
```

#### 404 - Feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

