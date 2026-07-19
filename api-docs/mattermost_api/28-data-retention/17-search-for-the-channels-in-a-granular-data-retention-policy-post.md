# 17-Search for the channels in a granular data retention policy [POST]

`POST /api/v4/data_retention/policies/{policy_id}/channels/search`

Searches for the channels to which a granular data retention policy is applied.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |

### Request Body (application/json)

```json
{
  "term": string, // The string to search in the channel name, display name, and purpose.
  "team_ids": [
    string
  ], // Filters results to channels belonging to the given team ids 
  "public": boolean, // Filters results to only return Public / Open channels, can be used in conjunction with `private` to return both `public` and `private` channels 
  "private": boolean, // Filters results to only return Private channels, can be used in conjunction with `public` to return both `private` and `public` channels 
  "deleted": boolean, // Filters results to only return deleted / archived channels 
}
```
### Responses

#### 200 - Channels for retention policy successfully retrieved.

Schema (application/json):
```json
[
  any
]
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

