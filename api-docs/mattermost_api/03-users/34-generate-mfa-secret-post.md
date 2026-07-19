# 34-Generate MFA secret [POST]

`POST /api/v4/users/{user_id}/mfa/generate`

Generates an multi-factor authentication secret for a user and returns it as a string and as base64 encoded QR code image.
##### Permissions
Must be logged in as the user or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - MFA secret generation successful

Schema (application/json):
```json
{
  "secret": string, // The MFA secret as a string
  "qr_code": string, // A base64 encoded QR code image
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

