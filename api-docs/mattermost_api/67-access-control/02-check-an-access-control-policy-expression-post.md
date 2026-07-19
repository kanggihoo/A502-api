# 02-Check an access control policy expression [POST]

`POST /api/v4/access_control_policies/cel/check`

Checks the syntax and validity of an access control policy expression.
##### Permissions
Must have the `manage_system` permission.


### Request Body (application/json)

```json
{
  "expression": string, // The expression to check.
}
```
### Responses

#### 200 - Expression check result.

Schema (application/json):
```json
[
  {
    "message": string, // The error message.
    "field": string, // The field related to the error, if applicable.
    "line": integer, // The line number where the error occurred in the expression.
    "column": integer, // The column number where the error occurred in the expression.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

