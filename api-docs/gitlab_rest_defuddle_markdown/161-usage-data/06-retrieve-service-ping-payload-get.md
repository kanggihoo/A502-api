# 06-Retrieve Service Ping payload [GET]

`GET /api/v4/usage_data/service_ping`

Retrieves the Service Ping payload from the application cache as JSON. If no cached payload is available, returns an empty response. Requires a personal access token with the `read_service_ping` scope. Introduced in GitLab 16.9.

### Responses

#### 200 - OK

#### 401 - 401 Unauthorized

#### 403 - Forbidden

#### 404 - Not found

