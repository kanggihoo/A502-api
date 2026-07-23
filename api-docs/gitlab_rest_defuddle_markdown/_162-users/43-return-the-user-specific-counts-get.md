# 43-Return the user specific counts [GET]

`GET /api/v4/user_counts`

Assigned open issues, assigned MRs and pending todos count

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "merge_requests": integer,
  "assigned_issues": integer,
  "assigned_merge_requests": integer,
  "review_requested_merge_requests": integer,
  "todos": integer,
}
```

#### 401 - Unauthorized

