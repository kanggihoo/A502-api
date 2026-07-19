# 02-Get the total file storage usage for the instance in bytes. [GET]

`GET /api/v4/usage/storage`

Get the total file storage usage for the instance in bytes rounded down to the most significant digit. Example: returns 4000 instead of 4321
##### Permissions
Must be authenticated.
__Minimum server version__: 7.1


### Responses

#### 200 - The total file storage usage for the instance in bytes rounded down to the most significant digit.

Schema (application/json):
```json
{
  "bytes": number, // Total file storage usage for the instance in bytes rounded down to the most significant digit
}
```

#### 401 - 

#### 500 - 

