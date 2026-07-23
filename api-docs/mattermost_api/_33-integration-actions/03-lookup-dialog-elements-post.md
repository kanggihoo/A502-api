# 03-Lookup dialog elements [POST]

`POST /api/v4/actions/dialogs/lookup`

Endpoint used by the Mattermost clients to lookup dynamic dialog elements. See https://docs.mattermost.com/developer/interactive-dialogs.html for more information on interactive dialogs.
__Minimum server version: 11.0__


### Request Body (application/json)

```json
{
  "url": string (required), // The URL to send the lookup request to
  "channel_id": string (required), // Channel ID the user is performing the lookup from
  "team_id": string, // Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team). 
  "submission": {} (required), // String map where keys are element names and values are the element input values
  "callback_id": string, // Callback ID sent when the dialog was opened
  "state": string, // State sent when the dialog was opened
}
```
### Responses

#### 200 - Dialog lookup successful

Schema (application/json):
```json
{
  "options": [
    {
      "text": string, // Display text for the option
      "value": string, // Value for the option
    }
  ], // List of options returned from the lookup
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 429 - The upstream integration rate-limited the request. The original status code is preserved so clients can honor retry semantics.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 502 - The upstream integration returned a 5xx (other than 503). Surfaced as Bad Gateway because the failure is upstream of Mattermost.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 503 - The upstream integration is unavailable. The original status code is preserved so clients can honor retry semantics.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

