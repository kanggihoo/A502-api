# 10-Get cloud subscription invoices [GET]

`GET /api/v4/cloud/subscription/invoices`

Retrieves the invoices for the subscription bound to this installation.
##### Permissions
Must have `manage_system` permission and be licensed for Cloud.
__Minimum server version__: 5.30 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Subscription invoices returned successfully

Schema (application/json):
```json
[
  {
    "id": string,
    "number": string,
    "create_at": integer,
    "total": integer,
    "tax": integer,
    "status": string,
    "period_start": integer,
    "period_end": integer,
    "subscription_id": string,
    "item": [
      {
        "price_id": string,
        "total": integer,
        "quantity": integer,
        "price_per_unit": integer,
        "description": string,
        "metadata": [
          string
        ],
      }
    ],
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

