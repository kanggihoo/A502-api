# 08-Get cloud subscription [GET]

`GET /api/v4/cloud/subscription`

Retrieves the subscription information for the Mattermost Cloud customer bound to this installation.
##### Permissions
Must have `manage_system` permission and be licensed for Cloud.
__Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Cloud subscription returned successfully

Schema (application/json):
```json
{
  "id": string,
  "customer_id": string,
  "product_id": string,
  "add_ons": [
    string
  ],
  "start_at": integer,
  "end_at": integer,
  "create_at": integer,
  "seats": integer,
  "dns": string,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

