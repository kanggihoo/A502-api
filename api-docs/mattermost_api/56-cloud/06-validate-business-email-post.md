# 06-Validate business email [POST]

`POST /api/v4/cloud/validate-business-email`

Validate whether an email address is considered a business email by the cloud service.
##### Permissions Must be authenticated.


### Request Body (application/json)

```json
{
  "email": string (required),
}
```
### Responses

#### 200 - Email validation successful

Schema (application/json):
```json
{
  "is_valid": boolean,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

