# 03-Get cloud customer [GET]

`GET /api/v4/cloud/customer`

Retrieves the customer information for the Mattermost Cloud customer bound to this installation.
##### Permissions
Must have `manage_system` permission and be licensed for Cloud.
__Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Cloud customer returned successfully

Schema (application/json):
```json
{
  "id": string,
  "creator_id": string,
  "create_at": integer,
  "email": string,
  "name": string,
  "num_employees": string,
  "contact_first_name": string,
  "contact_last_name": string,
  "billing_address": {
    "city": string,
    "country": string,
    "line1": string,
    "line2": string,
    "postal_code": string,
    "state": string,
  },
  "company_address": {
    "city": string,
    "country": string,
    "line1": string,
    "line2": string,
    "postal_code": string,
    "state": string,
  },
  "payment_method": {
    "type": string,
    "last_four": integer,
    "exp_month": integer,
    "exp_year": integer,
    "card_brand": string,
    "name": string,
  },
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

