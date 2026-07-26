# 10-Execute a command [POST]

`POST /api/v4/commands/execute`

Execute a command on a team.
##### Permissions
Must have `use_slash_commands` permission for the team the command is in.


### Request Body (application/json)

```json
{
  "channel_id": string (required), // Channel Id where the command will execute
  "command": string (required), // The slash command to execute, including parameters. Eg, `'/echo bounces around the room'`
}
```
### Responses

#### 200 - Command execution successful

Schema (application/json):
```json
{
  "ResponseType": string, // The response type either in_channel or ephemeral
  "Text": string,
  "Username": string,
  "IconURL": string,
  "GotoLocation": string,
  "Attachments": [
    {
      "Id": string,
      "Fallback": string,
      "Color": string,
      "Pretext": string,
      "AuthorName": string,
      "AuthorLink": string,
      "AuthorIcon": string,
      "Title": string,
      "TitleLink": string,
      "Text": string,
      "Fields": [
        {
          "Title": string,
          "Value": string, // The value of the attachment, set as string but capable with golang interface
          "Short": boolean,
        }
      ],
      "ImageURL": string,
      "ThumbURL": string,
      "Footer": string,
      "FooterIcon": string,
      "Timestamp": string, // The timestamp of the message attachment, either type of string or integer
    }
  ],
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

