# 36-Retrieve details on an email address [GET]

`GET /api/v4/user/emails/{email_id}`

Retrieves details on a specified email address for the currently authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `email_id` | `integer` | `path` | Yes | The ID of the email |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "email": string,
  "confirmed_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

