# 12-Reattach a plugin process [POST]

`POST /api/v4/plugins/reattach`

Reattaches the server to an already running plugin process.
This endpoint is only exposed over a local socket.

##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "Manifest": {
    "id": string, // Globally unique identifier that represents the plugin.
    "name": string, // Name of the plugin.
    "description": string, // Description of what the plugin is and does.
    "version": string, // Version number of the plugin.
    "min_server_version": string, // The minimum Mattermost server version required for the plugin.  Available as server version 5.6. 
    "backend": {
      "executable": string, // Path to the executable binary.
    }, // Deprecated in Mattermost 5.2 release.
    "server": {
      "executables": {
        "linux-amd64": string,
        "darwin-amd64": string,
        "windows-amd64": string,
      }, // Paths to executable binaries, specifying multiple entry points for different platforms when bundled together in a single plugin.
      "executable": string, // Path to the executable binary.
    },
    "webapp": {
      "bundle_path": string, // Path to the webapp JavaScript bundle.
    },
    "settings_schema": {}, // Settings schema used to define the System Console UI for the plugin.
  } (required),
  "PluginReattachConfig": {
    "Protocol": string,
    "ProtocolVersion": integer,
    "Addr": {
      "Name": string,
      "Net": string,
    },
    "Pid": integer,
    "Test": boolean,
  } (required),
}
```
### Responses

#### 200 - Plugin reattached successfully

#### 400 - 

#### 401 - 

#### 403 - 

