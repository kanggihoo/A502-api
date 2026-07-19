# 01-Get a list of paged and sorted users for admin reporting purposes [GET]

`GET /api/v4/reports/users`

Get a list of paged users for admin reporting purposes, based on provided parameters.
##### Permissions
Requires `sysconsole_read_user_management_users`.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `sort_column` | `string` | `query` | No | The column to sort the users by. Must be one of ("CreateAt", "Username", "FirstName", "LastName", "Nickname", "Email") or the API will return an error. |
| `direction` | `string` | `query` | No | The direction to accept paging values from. Will return values ahead of the cursor if "prev", and below the cursor if "next". Default is "next". |
| `sort_direction` | `string` | `query` | No | The sorting direction. Must be one of ("asc", "desc"). Will default to 'asc' if not specified or the input is invalid. |
| `page_size` | `integer` | `query` | No | The maximum number of users to return. |
| `from_column_value` | `string` | `query` | No | The value of the sorted column corresponding to the cursor to read from. Should be blank for the first page asked for. |
| `from_id` | `string` | `query` | No | The value of the user id corresponding to the cursor to read from. Should be blank for the first page asked for. |
| `date_range` | `string` | `query` | No | The date range of the post statistics to display. Must be one of ("last30days", "previousmonth", "last6months", "alltime"). Will default to 'alltime' if the input is not valid. |
| `role_filter` | `string` | `query` | No | Filter users by their role. |
| `team_filter` | `string` | `query` | No | Filter users by a specified team ID. |
| `has_no_team` | `boolean` | `query` | No | If true, show only users that have no team. Will ignore provided "team_filter" if true. |
| `hide_active` | `boolean` | `query` | No | If true, show only users that are inactive. Cannot be used at the same time as "hide_inactive" |
| `hide_inactive` | `boolean` | `query` | No | If true, show only users that are active. Cannot be used at the same time as "hide_active" |
| `search_term` | `string` | `query` | No | A filtering search term that allows filtering by Username, FirstName, LastName, Nickname or Email |

### Responses

#### 200 - User page retrieval successful

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

