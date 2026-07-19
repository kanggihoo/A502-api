# 03-Create Pages domain [POST]

`POST /api/v4/projects/{id}/pages/domains`

Creates a Pages domain in a specified project. You must have permissions to create Pages domains.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "domain": string (required), // The domain
  "certificate": any,
  "key": any,
  "auto_ssl_enabled": boolean, // Enables automatic generation of SSL certificates issued by Let's Encrypt for custom domains.
  "user_provided_certificate": string,
  "user_provided_key": string,
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "domain": string,
  "url": string,
  "verified": string,
  "verification_code": string,
  "enabled_until": string,
  "auto_ssl_enabled": string,
  "certificate": {
    "subject": string,
    "expired": string,
    "certificate": string,
    "certificate_text": string,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

