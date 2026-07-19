# 06-Get Custom Profile Attribute property group data [GET]

`GET /api/v4/custom_profile_attributes/group`

Get the property group used for Custom Profile Attributes.

__Minimum server version__: 10.8

##### Permissions
Must be authenticated.


### Responses

#### 200 - Group fetch successful

Schema (application/json):
```json
{
  "id": string, // The ID of the custom profile attributes group
}
```

#### 401 - 

#### 403 - 

