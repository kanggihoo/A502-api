# 07-Get webapp plugins [GET]

`GET /api/v4/plugins/webapp`

Get a list of web app plugins installed and activated on the server.

##### Permissions
No permissions required.

__Minimum server version__: 4.4


### Responses

#### 200 - Plugin deactivated successfully

Schema (application/json):
```json
[
  {
    "id": string, // Globally unique identifier that represents the plugin.
    "version": string, // Version number of the plugin.
    "webapp": {
      "bundle_path": string, // Path to the webapp JavaScript bundle.
    },
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

