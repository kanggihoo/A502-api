# 07-Create a license [POST]

`POST /api/v4/license`

Creates a license.

### Request Body (application/json)

```json
{
  "license": string (required), // The license string
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad request

