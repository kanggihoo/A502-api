# 05-Retrieve a user as a regular user [GET]

`GET /api/v4/users/{id}`

Retrieves a specified user as a regular user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `with_custom_attributes` | `boolean` | `query` | No | Include custom attributes in the response |
| `custom_attributes` | `object` | `query` | No | Filter with custom attributes |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "username": string,
  "public_email": string,
  "name": string,
  "state": string,
  "locked": boolean,
  "avatar_url": string,
  "avatar_path": string,
  "custom_attributes": [
    {
      "key": string,
      "value": string,
    }
  ],
  "web_url": string,
  "created_at": string,
  "bio": string,
  "location": string,
  "linkedin": string,
  "twitter": string,
  "discord": string,
  "website_url": string,
  "github": string,
  "job_title": string,
  "pronouns": string,
  "organization": string,
  "bot": boolean,
  "work_information": string,
  "followers": string,
  "following": string,
  "is_followed": string,
  "local_time": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

