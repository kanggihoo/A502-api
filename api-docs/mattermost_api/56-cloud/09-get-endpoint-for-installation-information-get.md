# 09-GET endpoint for Installation information [GET]

`GET /api/v4/cloud/installation`

An endpoint for fetching the installation information.
##### Permissions
Must have `sysconsole_read_site_ip_filters` permission and be licensed for Cloud.
__Minimum server version__: 9.1 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Installation returned successfully

Schema (application/json):
```json
{
  "id": string, // A unique identifier
  "allowed_ip_ranges": {
    "CIDRBlock": string, // An IP address range in CIDR notation
    "Description": string, // A description for the CIDRBlock
  },
  "state": string, // The current state of the installation
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

