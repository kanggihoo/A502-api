# 03-Starts a job to export the users to a report file. [POST]

`POST /api/v4/reports/users/export`

Starts a job to export the users to a report file.
##### Permissions
Requires `sysconsole_read_user_management_users`.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `date_range` | `string` | `query` | No | The date range of the post statistics to display. Must be one of ("last30days", "previousmonth", "last6months", "alltime"). Will default to 'alltime' if the input is not valid. |

### Responses

#### 200 - Job successfully started

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a user was created
    "update_at": integer, // The time in milliseconds a user was last updated
    "delete_at": integer, // The time in milliseconds a user was deleted
    "username": string,
    "auth_data": string,
    "auth_service": string,
    "email": string,
    "nickname": string,
    "first_name": string,
    "last_name": string,
    "position": string,
    "roles": string,
    "locale": string,
    "timezone": {
      "useAutomaticTimezone": string, // Set to "true" to use the browser/system timezone, "false" to set manually. Defaults to "true".
      "manualTimezone": string, // Value when setting manually the timezone, i.e. "Europe/Berlin".
      "automaticTimezone": string, // This value is set automatically when the "useAutomaticTimezone" is set to "true".
    },
    "disable_welcome_email": boolean,
    "last_login": integer, // Last time the user was logged in
    "last_status_at": integer, // Last time the user's status was updated
    "last_post_date": integer, // Last time the user made a post within the given date range
    "days_active": integer, // Total number of days a user posted within the given date range
    "total_posts": integer, // Total number of posts made by a user within the given date range
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

