# 04-Get the current appearance [GET]

`GET /api/v4/application/appearance`

Get the current appearance

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

#### 401 - Unauthorized

#### 403 - Forbidden

