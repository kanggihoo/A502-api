# 05-Modify appearance [PUT]

`PUT /api/v4/application/appearance`

Modify appearance

### Request Body (multipart/form-data)

```json
{
  "title": string, // Instance title on the sign in / sign up page
  "description": string, // Markdown text shown on the sign in / sign up page
  "pwa_name": string, // Name of the Progressive Web App
  "pwa_short_name": string, // Optional, short name for Progressive Web App
  "pwa_description": string, // An explanation of what the Progressive Web App does
  "logo": string, // Instance image used on the sign in / sign up page
  "pwa_icon": string, // Icon used for Progressive Web App
  "header_logo": string, // Instance image used for the main navigation bar
  "favicon": string, // Instance favicon in .ico/.png format
  "member_guidelines": string, // Markdown text shown on the members page of a group or project
  "new_project_guidelines": string, // Markdown text shown on the new project page
  "profile_image_guidelines": string, // Markdown text shown on the profile page below Public Avatar
  "header_message": string, // Message within the system header bar
  "footer_message": string, // Message within the system footer bar
  "message_background_color": string, // Background color for the system header / footer bar
  "message_font_color": string, // Font color for the system header / footer bar
  "email_header_and_footer_enabled": boolean, // Add header and footer to all outgoing emails if enabled
  "site_name": string, // Last part of the webpage title. Defaults to empty.
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "title": string,
  "description": string,
  "pwa_name": string,
  "pwa_short_name": string,
  "pwa_description": string,
  "logo": string,
  "pwa_icon": string,
  "header_logo": string,
  "favicon": string,
  "new_project_guidelines": string,
  "member_guidelines": string,
  "profile_image_guidelines": string,
  "header_message": string,
  "footer_message": string,
  "message_background_color": string,
  "message_font_color": string,
  "email_header_and_footer_enabled": boolean,
  "site_name": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

