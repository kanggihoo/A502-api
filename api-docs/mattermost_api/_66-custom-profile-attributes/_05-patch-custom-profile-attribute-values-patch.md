# 05-Patch Custom Profile Attribute values [PATCH]

`PATCH /api/v4/custom_profile_attributes/values`

Partially update a set of values on the requester's Custom
Profile Attribute fields by providing only the information you
want to update. Omitted fields will not be updated. The fields
that can be updated are defined in the request body, all other
provided fields will be ignored.

**Note:** Values for fields with `attrs.protected = true` cannot be
updated and will return an error.

__Minimum server version__: 10.5

##### Permissions
Must be authenticated.


### Request Body (application/json)

```json
[
  {
    "id": string,
    "value": any,
  }
]
```
### Responses

#### 200 - Custom Profile Attribute values patch successful

Schema (application/json):
```json
[
  {
    "id": string,
    "value": any,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

