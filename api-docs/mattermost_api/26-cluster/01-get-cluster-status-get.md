# 01-Get cluster status [GET]

`GET /api/v4/cluster/status`

Get a list of all healthy nodes, including local information and status of each one. If a node is not present, it means it is not healthy.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Cluster status retrieval successful

Schema (application/json):
```json
[
  [
    any
  ]
]
```

#### 403 - 

