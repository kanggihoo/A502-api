# 04-Get posts for reporting and compliance purposes using cursor-based pagination [POST]

`POST /api/v4/reports/posts`

Get posts from a specific channel for reporting, compliance, and auditing purposes. This endpoint uses cursor-based pagination to efficiently retrieve large datasets.
The cursor is an opaque, base64-encoded token that contains all pagination state. Clients should treat the cursor as an opaque string and pass it back unchanged. When a cursor is provided, query parameters from the initial request are embedded in the cursor and take precedence over request body parameters.
##### Permissions
Requires `manage_system` permission (system admin only).
##### License
Requires an Enterprise license (or higher).
##### Features
- Cursor-based pagination for efficient large dataset retrieval - Support for both create_at and update_at time fields - Ascending or descending sort order - Time range filtering with optional end_time - Include/exclude deleted posts - Exclude system posts (any type starting with "system_") - Optional metadata enrichment (file info, reactions, emojis, priority, acknowledgements)


### Request Body (application/json)

```json
{
  "channel_id": string (required), // The ID of the channel to retrieve posts from
  "cursor": string, // Opaque cursor string for pagination. Omit or use empty string for the first request. For subsequent requests, use the exact cursor value from the previous response's next_cursor. The cursor is base64-encoded and contains all pagination state including time, post ID, and query parameters. Do not attempt to parse or modify the cursor value. 
  "start_time": integer, // Optional start time for query range in Unix milliseconds. Only used for the first request (ignored when cursor is provided). - For "asc" (ascending): starts retrieving from this time going forward - For "desc" (descending): starts retrieving from this time going backward If omitted, defaults to 0 for ascending or MaxInt64 for descending. 
  "time_field": enum("create_at" | "update_at"), // Which timestamp field to use for sorting and filtering. Use "create_at" to retrieve posts by creation time, or "update_at" to retrieve posts by last modification time. 
  "sort_direction": enum("asc" | "desc"), // Sort direction for pagination. Use "asc" to retrieve posts from oldest to newest, or "desc" to retrieve from newest to oldest. 
  "per_page": integer, // Number of posts to return per page. Maximum 1000.
  "include_deleted": boolean, // If true, include posts that have been deleted (DeleteAt > 0). By default, only non-deleted posts are returned. 
  "exclude_system_posts": boolean, // If true, exclude all system posts. 
  "include_metadata": boolean, // If true, enrich posts with additional metadata including file information, reactions, custom emojis, priority, and acknowledgements. Note that this may increase response time for large result sets. 
}
```
### Responses

#### 200 - Posts retrieved successfully

Schema (application/json):
```json
{
  "posts": {}, // Map of post IDs to post objects
  "next_cursor": {
    "cursor": string, // Base64-encoded opaque cursor string containing pagination state
  }, // Opaque cursor for retrieving the next page. If null, there are no more pages. Pass the cursor string from this object in the next request. 
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

