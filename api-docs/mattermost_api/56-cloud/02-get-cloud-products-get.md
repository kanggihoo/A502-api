# 02-Get cloud products [GET]

`GET /api/v4/cloud/products`

Retrieve a list of all products that are offered for Mattermost Cloud.
##### Permissions
Must have `manage_system` permission and be licensed for Cloud.
__Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Cloud products returned successfully

Schema (application/json):
```json
[
  {
    "id": string,
    "name": string,
    "description": string,
    "price_per_seat": string,
    "add_ons": [
      {
        "id": string,
        "name": string,
        "display_name": string,
        "price_per_seat": string,
      }
    ],
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

