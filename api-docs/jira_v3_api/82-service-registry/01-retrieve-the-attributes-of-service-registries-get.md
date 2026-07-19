# 01-Retrieve the attributes of service registries [GET]

`GET /rest/atlassian-connect/1/service-registry`

Retrieve the attributes of given service registries.

**[Permissions](#permissions) required:** Only Connect apps can make this request and the servicesIds belong to the tenant you are requesting

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceIds` | `array` | `query` | Yes | The ID of the services (the strings starting with "b:" need to be decoded in Base64). |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
[
  {
    "description": string, // service description
    "id": string, // service ID
    "name": string, // service name
    "organizationId": string, // organization ID
    "revision": string, // service revision
    "serviceTier": {
      "description": string, // tier description
      "id": string, // tier ID
      "level": integer, // tier level
      "name": string, // tier name
      "nameKey": string, // name key of the tier
    },
  }
]
```

#### 400 - Returned if the request is invalid.

#### 401 - The request needs to be authenticated.

#### 403 - The request isn't authorized.

#### 500 - The endpoint failed internally.

#### 501 - The endpoint isn't ready for receiving requests.

#### 504 - The upstream service is busy.

