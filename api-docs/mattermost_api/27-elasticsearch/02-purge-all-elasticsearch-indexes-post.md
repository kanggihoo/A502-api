# 02-Purge all Elasticsearch indexes [POST]

`POST /api/v4/elasticsearch/purge_indexes`

Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
__Minimum server version__: 4.1
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Indexes purged successfully.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 500 - 

#### 501 - 

