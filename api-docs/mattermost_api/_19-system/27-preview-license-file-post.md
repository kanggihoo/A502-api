# 27-Preview license file [POST]

`POST /api/v4/license/preview`

Validate and parse a license file without saving it. This allows administrators
to preview the license details before applying it.

__Minimum server version__: 10.9

##### Permissions
Must have `manage_license_information` permission.


### Request Body (multipart/form-data)

```json
{
  "license": string (required), // The license to be previewed
}
```
### Responses

#### 200 - License preview successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier of the license
  "issued_at": integer, // The timestamp when the license was issued
  "starts_at": integer, // The timestamp when the license becomes active
  "expires_at": integer, // The timestamp when the license expires
  "sku_name": string, // The display name of the license SKU (e.g., "Enterprise", "Professional")
  "sku_short_name": string, // The short name of the license SKU (e.g., "enterprise", "professional")
  "is_trial": boolean, // Whether this is a trial license
  "is_gov_sku": boolean, // Whether this is a government SKU license
  "customer": {
    "id": string,
    "name": string,
    "email": string,
    "company": string,
  },
  "features": {
    "users": integer, // The number of users allowed by the license
  },
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

