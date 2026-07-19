# 02-Update precomputations (apps) [POST]

`POST /rest/api/3/jql/function/computation`

Update the precomputation value of a function created by a Forge/Connect app.

**[Permissions](#permissions) required:** An API for apps to update their own precomputations.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `skipNotFoundPrecomputations` | `boolean` | `query` | No |  |

### Request Body (application/json)

```json
{
  "values": [
    {
      "error": string, // The error message to be displayed to the user if the given function clause is no longer valid during recalculation of the precomputation.
      "id": string (required), // The id of the precomputation to update.
      "value": string, // The new value of the precomputation.
    }
  ],
}
```
### Responses

#### 200 - 200 response

Schema (application/json):
```json
{
  "notFoundPrecomputationIDs": [
    string
  ], // List of precomputations that were not found and skipped. Only returned if the request passed skipNotFoundPrecomputations=true.
}
```

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation.
  "notFoundPrecomputationIDs": [
    string
  ], // List of precomputations that were not found.
}
```

#### 403 - Returned if the request is not authenticated as the app that provided the function.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation.
  "notFoundPrecomputationIDs": [
    string
  ], // List of precomputations that were not found.
}
```

#### 404 - Returned if the function is not found.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation.
  "notFoundPrecomputationIDs": [
    string
  ], // List of precomputations that were not found.
}
```

