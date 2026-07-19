# 01-Get global notification level settings and email, defaults to Participate [GET]

`GET /api/v4/notification_settings`

This feature was introduced in GitLab 8.12

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "level": string,
  "events": string,
  "notification_email": string,
}
```

#### 401 - Unauthorized

