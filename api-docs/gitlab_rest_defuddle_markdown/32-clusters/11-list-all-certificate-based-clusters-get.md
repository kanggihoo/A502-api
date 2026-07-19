# 11-List all certificate-based clusters [GET]

`GET /api/v4/discover-cert-based-clusters`

Lists all certificate-based clusters associated with a project. This feature was introduced in GitLab 17.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `integer` | `query` | Yes | The group ID to find all certificate-based clusters in the hierarchy |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "groups": {},
  "projects": {},
}
```

#### 400 - Bad Request

#### 403 - Forbidden

