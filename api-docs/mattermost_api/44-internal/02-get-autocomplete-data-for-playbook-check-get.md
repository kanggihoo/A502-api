# 02-Get autocomplete data for /playbook check [GET]

`GET /plugins/playbooks/api/v0/runs/checklist-autocomplete`

This is an internal endpoint used by the autocomplete system to retrieve the data needed to show the list of items that the user can check.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_ID` | `string` | `query` | Yes | ID of the channel the user is in. |

### Responses

#### 200 - List of autocomplete items for this channel.

Schema (application/json):
```json
[
  {
    "item": string (required), // A string containing a pair of integers separated by a space. The first integer is the index of the checklist; the second is the index of the item within the checklist.
    "hint": string (required), // The title of the corresponding item.
    "helptext": string (required), // Always the value "Check/uncheck this item".
  }
]
```

#### 500 - 

