# 03-Get metadata from Identity Provider [POST]

`POST /api/v4/saml/metadatafromidp`

Get SAML metadata from the Identity Provider. SAML must be configured properly.
##### Permissions
No permission required.


### Request Body (application/json)

```json
{
  "saml_metadata_url": string, // The URL from which to retrieve the SAML IDP data.
}
```
### Responses

#### 200 - SAML metadata retrieval successful

Schema (application/json):
```json
string
```

#### 501 - 

