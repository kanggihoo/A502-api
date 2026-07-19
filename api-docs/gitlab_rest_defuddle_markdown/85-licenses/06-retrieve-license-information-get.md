# 06-Retrieve license information [GET]

`GET /api/v4/license`

Retrieves information about the current license.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "plan": string,
  "created_at": string,
  "starts_at": string,
  "expires_at": string,
  "historical_max": integer,
  "maximum_user_count": integer,
  "licensee": {},
  "add_ons": {},
  "expired": boolean,
  "overage": integer, // Difference between the number of billable users and the number of licensed users. Calculated differently depending on whether the license has expired or not.
  "user_limit": integer,
  "active_users": integer,
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

