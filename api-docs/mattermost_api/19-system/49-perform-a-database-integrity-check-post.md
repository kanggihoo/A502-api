# 49-Perform a database integrity check [POST]

`POST /api/v4/integrity`

Performs a database integrity check.


__Note__: This check may temporarily harm system performance.


__Minimum server version__: 5.28.0


__Local mode only__: This endpoint is only available through [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).


### Responses

#### 200 - Integrity check successful

Schema (application/json):
```json
[
  {
    "data": {
      "parent_name": string, // the name of the parent relation (table).
      "child_name": string, // the name of the child relation (table).
      "parent_id_attr": string, // the name of the attribute (column) containing the parent id.
      "child_id_attr": string, // the name of the attribute (column) containing the child id.
      "records": [
        {
          "parent_id": string, // the id of the parent relation (table) entry.
          "child_id": string, // the id of the child relation (table) entry.
        }
      ], // the list of orphaned records found.
    },
    "err": string, // a string value set in case of error.
  }
]
```

