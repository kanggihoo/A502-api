# 09-Installs a marketplace plugin [POST]

`POST /api/v4/plugins/marketplace`

Installs a plugin listed in the marketplace server.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.16


### Request Body (application/json)

```json
{
  "id": string (required), // The ID of the plugin to install.
  "version": string, // Optional plugin version. If omitted, the latest compatible version is installed.
}
```
### Responses

#### 200 - Plugin installed successfully

Schema (application/json):
```json
{
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
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

