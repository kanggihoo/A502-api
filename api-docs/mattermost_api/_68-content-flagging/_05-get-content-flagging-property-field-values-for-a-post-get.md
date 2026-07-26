# 05-Get content flagging property field values for a post [GET]

`GET /api/v4/content_flagging/post/{post_id}/field_values`

Returns the property field values associated with content flagging reports for a specific post. These values provide additional context about the flags on the post.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The ID of the post to retrieve property field values for |

### Responses

#### 200 - Property field values retrieved successfully

Schema (application/json):
```json
[
  {
    "id": string, // A unique, 26 characters long, alphanumeric identifier for the property value.
    "field_id": string, // The identifier of the property field this value belongs to.
    "value": string, // The JSON-encoded value of the property.
    "create_at": integer, // The property value creation timestamp, formatted as the number of milliseconds since the Unix epoch.
    "update_at": integer, // The property value update timestamp, formatted as the number of milliseconds since the Unix epoch.
    "delete_at": integer, // The property value deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if not deleted.
  }
]
```

#### 403 - Forbidden - User does not have permission to access this post.

#### 404 - Post not found or feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

