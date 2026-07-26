# 45-Executes an inplace upgrade from Team Edition to Enterprise Edition [POST]

`POST /api/v4/upgrade_to_enterprise`

It downloads the Mattermost Enterprise Edition of your current version and replace your current version with it. After the upgrade you need to restart the Mattermost server.
__Minimum server version__: 5.27
##### Permissions
Must have `manage_system` permission.


### Responses

#### 202 - Upgrade started

Schema (application/json):
```json
{
  "ack_id": string,
  "platform": string,
  "server_id": string,
  "device_id": string,
  "post_id": string,
  "category": string,
  "sound": string,
  "message": string,
  "badge": number,
  "cont_ava": number,
  "team_id": string,
  "channel_id": string,
  "root_id": string,
  "channel_name": string,
  "type": string,
  "sub_type": string, // Additional message type information for mobile clients. Use "calls" for Calls plugin notifications.
  "transport": enum("" | "voip"), // Delivery path for the push proxy. Use "voip" for VoIP (CallKit) notifications; omit for standard delivery.
  "sender_id": string,
  "sender_name": string,
  "override_username": string,
  "override_icon_url": string,
  "from_webhook": string,
  "version": string,
  "is_crt_enabled": boolean, // Whether Collapsed Reply Threads is enabled for the recipient.
  "is_id_loaded": boolean,
  "signature": string,
}
```

#### 403 - 

#### 429 - 

