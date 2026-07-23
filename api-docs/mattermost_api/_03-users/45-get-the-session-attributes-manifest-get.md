# 45-Get the session attributes manifest [GET]

`GET /api/v4/users/sessions/attributes/manifest`

Get the set of session attributes the server expects the client to collect, filtered to the requesting client's platform, including the per-attribute TTL and grace period.
Requires the `SessionAttributes` feature flag and an Enterprise Advanced license.


### Responses

#### 200 - Session attributes manifest retrieval successful

Schema (application/json):
```json
[
  {
    "name": string,
    "type": string,
    "ttl_seconds": integer,
    "grace_period_seconds": integer,
    "platforms": [
      string
    ],
    "display_name": string,
  }
]
```

#### 501 - 

