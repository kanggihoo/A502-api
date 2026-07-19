# 02-Create a broadcast message [POST]

`POST /api/v4/broadcast_messages`

Creates a broadcast message.

### Request Body (application/json)

```json
{
  "message": string (required), // Message to display
  "starts_at": string, // Starting time
  "ends_at": string, // Ending time
  "color": string, // Background color (Deprecated. Use "theme" instead.)
  "font": string, // Foreground color (Deprecated. Use "theme" instead.)
  "target_access_levels": [
    integer
  ], // Target user roles
  "target_path": string, // Target path
  "broadcast_type": enum("banner" | "notification"), // Broadcast type. Defaults to banner
  "dismissable": boolean, // Is dismissable
  "theme": enum("indigo" | "light-indigo" | "blue" | "light-blue" | "green" | "light-green" | "red" | "light-red" | "dark" | "light"), // The theme for the message
}
```
### Responses

#### 201 - Created

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

