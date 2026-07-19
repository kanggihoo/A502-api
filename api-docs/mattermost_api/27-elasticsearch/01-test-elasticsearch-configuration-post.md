# 01-Test Elasticsearch configuration [POST]

`POST /api/v4/elasticsearch/test`

Test the current Elasticsearch configuration to see if the Elasticsearch server can be contacted successfully.
Optionally provide a configuration in the request body to test. If no valid configuration is present in the
request body the current server configuration will be tested.

__Minimum server version__: 4.1
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Elasticsearch test successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 500 - 

#### 501 - 

