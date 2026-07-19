# 02-Submit a dialog [POST]

`POST /api/v4/actions/dialogs/submit`

Endpoint used by the Mattermost clients to submit a dialog. See https://docs.mattermost.com/developer/interactive-dialogs.html for more information on interactive dialogs.
__Minimum server version: 5.6__


### Request Body (application/json)

```json
{
  "url": string (required), // The URL to send the submitted dialog payload to
  "channel_id": string (required), // Channel ID the user submitted the dialog from
  "team_id": string, // Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team). 
  "submission": {} (required), // String map where keys are element names and values are the element input values
  "callback_id": string, // Callback ID sent when the dialog was opened
  "state": string, // State sent when the dialog was opened
  "cancelled": boolean, // Set to true if the dialog was cancelled
  "file_ids": [
    string
  ], // List of file IDs uploaded as part of the dialog submission. Each file must have been uploaded by the submitting user. A maximum of 10 file IDs may be submitted. 
}
```
### Responses

#### 200 - Dialog submission successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
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

