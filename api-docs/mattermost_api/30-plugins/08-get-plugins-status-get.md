# 08-Get plugins status [GET]

`GET /api/v4/plugins/statuses`

Returns the status for plugins installed anywhere in the cluster

##### Permissions
No permissions required.

__Minimum server version__: 4.4


### Responses

#### 200 - Plugin status retreived successfully

Schema (application/json):
```json
[
  {
    "plugin_id": string, // Globally unique identifier that represents the plugin.
    "name": string, // Name of the plugin.
    "description": string, // Description of what the plugin is and does.
    "version": string, // Version number of the plugin.
    "cluster_id": string, // ID of the cluster in which plugin is running
    "plugin_path": string, // Path to the plugin on the server
    "state": enum("NotRunning" | "Starting" | "Running" | "FailedToStart" | "FailedToStayRunning" | "Stopping"), // State of the plugin
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

