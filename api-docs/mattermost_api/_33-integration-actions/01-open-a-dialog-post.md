# 01-Open a dialog [POST]

`POST /api/v4/actions/dialogs/open`

Open an interactive dialog using a trigger ID provided by a slash command, or some other action payload. See https://docs.mattermost.com/developer/interactive-dialogs.html for more information on interactive dialogs.

Up to 3 interactive dialogs may be open at once (minimum server version 11.10). Additional `open_dialog` events beyond this limit are silently ignored by the client.
__Minimum server version: 5.6__


### Request Body (application/json)

```json
{
  "trigger_id": string (required), // Trigger ID provided by other action
  "url": string (required), // The URL to send the submitted dialog payload to
  "dialog": {
    "callback_id": string, // Set an ID that will be included when the dialog is submitted
    "title": string (required), // Title of the dialog
    "introduction_text": string, // Markdown formatted introductory paragraph
    "elements": [
      {}
    ] (required), // Input elements, see https://docs.mattermost.com/developer/interactive-dialogs.html#elements. Supported element types include `text`, `textarea`, `select`, `radio`, `bool`, and `action_button`. An `action_button` element (minimum server version 11.10) renders a clickable button — fields: `name`, `display_name`, `type` set to "action_button", and an `action_button` object with a required `url` (must be a valid lookup URL) and optional `context` (string map). Clicking it calls `POST /api/v4/actions/dialogs/execute`. `action_button` elements are not included in the dialog submission payload. 
    "submit_label": string, // Label on the submit button
    "notify_on_cancel": boolean, // Set true to receive payloads when user cancels a dialog
    "state": string, // Set some state to be echoed back with the dialog submission
  } (required), // Post object to create
}
```
### Responses

#### 200 - Dialog open successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

