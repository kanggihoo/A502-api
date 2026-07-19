# 04-Update a broadcast message [PUT]

`PUT /api/v4/broadcast_messages/{id}`

Updates a specified broadcast message.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Broadcast message ID |

### Request Body (application/json)

```json
{
  "message": string, // Message to display
  "starts_at": string, // Starting time
  "ends_at": string, // Ending time
  "color": string, // Background color (Deprecated. Use "theme" instead.)
  "font": string, // Foreground color (Deprecated. Use "theme" instead.)
  "target_access_levels": [
    integer
  ], // Target user roles
  "target_path": string, // Target path
  "broadcast_type": enum("banner" | "notification"), // Broadcast Type
  "dismissable": boolean, // Is dismissable
  "theme": enum("indigo" | "light-indigo" | "blue" | "light-blue" | "green" | "light-green" | "red" | "light-red" | "dark" | "light"), // The theme for the message
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "message": string,
  "starts_at": string,
  "ends_at": string,
  "color": string,
  "font": string,
  "target_access_levels": [
    any
  ],
  "target_path": string,
  "broadcast_type": string,
  "theme": string,
  "dismissable": boolean,
  "active": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

