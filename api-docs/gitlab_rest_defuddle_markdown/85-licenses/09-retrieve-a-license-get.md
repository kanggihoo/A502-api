# 09-Retrieve a license [GET]

`GET /api/v4/license/{id}`

Retrieves information about a specified license.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the GitLab license |

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

