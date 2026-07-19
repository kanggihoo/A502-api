# 02-Create a playbook [POST]

`POST /plugins/playbooks/api/v0/playbooks`

Create a playbook

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the playbook.
  "description": string, // The description of the playbook.
  "team_id": string (required), // The identifier of the team where the playbook is in.
  "create_public_playbook_run": boolean (required), // A boolean indicating whether the playbook runs created from this playbook should be public or private.
  "public": boolean, // A boolean indicating whether the playbook is licensed as public or private. Required 'true' for free tier.
  "checklists": [
    {
      "title": string (required), // The title of the checklist.
      "items": [
        {
          "title": string (required), // The title of the checklist item.
          "command": string, // The slash command associated with this item. If the item has no slash command associated, this is an empty string
          "description": string, // A detailed description of the checklist item, formatted with Markdown.
        }
      ] (required), // The list of tasks to do.
    }
  ] (required), // The stages defined by this playbook.
  "member_ids": [
    string
  ] (required), // The identifiers of all the users that are members of this playbook.
  "broadcast_channel_ids": [
    string
  ], // The IDs of the channels where all the status updates will be broadcasted. The team of the broadcast channel must be the same as the playbook's team.
  "invited_user_ids": [
    string
  ], // A list with the IDs of the members to be automatically invited to the playbook run's channel as soon as the playbook run is created.
  "invite_users_enabled": boolean, // Boolean that indicates whether the members declared in invited_user_ids will be automatically invited.
  "default_owner_id": string, // User ID of the member that will be automatically assigned as owner as soon as the playbook run is created. If the member is not part of the playbook run's channel or is not included in the invited_user_ids list, they will be automatically invited to the channel.
  "default_owner_enabled": string, // Boolean that indicates whether the member declared in default_owner_id will be automatically assigned as owner.
  "announcement_channel_id": string, // ID of the channel where the playbook run will be automatically announced as soon as the playbook run is created.
  "announcement_channel_enabled": boolean, // Boolean that indicates whether the playbook run creation will be announced in the channel declared in announcement_channel_id.
  "webhook_on_creation_url": string, // An absolute URL where a POST request will be sent as soon as the playbook run is created. The allowed protocols are HTTP and HTTPS.
  "webhook_on_creation_enabled": boolean, // Boolean that indicates whether the webhook declared in webhook_on_creation_url will be automatically sent.
  "webhook_on_status_update_url": string, // An absolute URL where a POST request will be sent as soon as the playbook run's status is updated. The allowed protocols are HTTP and HTTPS.
  "webhook_on_status_update_enabled": boolean, // Boolean that indicates whether the webhook declared in webhook_on_status_update_url will be automatically sent.
}
```
### Responses

#### 201 - ID of the created playbook.

Schema (application/json):
```json
{
  "id": string (required),
}
```

#### 400 - 

#### 403 - 

#### 500 - 

