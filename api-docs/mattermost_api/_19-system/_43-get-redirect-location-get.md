# 43-Get redirect location [GET]

`GET /api/v4/redirect_location`

__Minimum server version__: 3.10
##### Permissions
Must be logged in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `url` | `string` | `query` | Yes | Url to check |

### Responses

#### 200 - Got redirect location

Schema (image/*):
```json
{
  "location": string,
}
```

#### 404 - 

