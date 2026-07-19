# 10-Gets all the marketplace plugins [GET]

`GET /api/v4/plugins/marketplace`

Gets all plugins from the marketplace server, merging data from locally installed plugins as well as prepackaged plugins shipped with the server.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.16


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Page number to be fetched. (not yet implemented) |
| `per_page` | `integer` | `query` | No | Number of item per page. (not yet implemented) |
| `filter` | `string` | `query` | No | Set to filter plugins by ID, name, or description. |
| `server_version` | `string` | `query` | No | Set to filter minimum plugin server version. (not yet implemented) |
| `local_only` | `boolean` | `query` | No | Set true to only retrieve local plugins. |

### Responses

#### 200 - Plugins retrieval successful

Schema (application/json):
```json
[
  {
    "homepage_url": string, // URL that leads to the homepage of the plugin.
    "icon_data": string, // Base64 encoding of a plugin icon SVG.
    "download_url": string, // URL to download the plugin.
    "release_notes_url": string, // URL that leads to the release notes of the plugin.
    "labels": [
      string
    ], // A list of the plugin labels.
    "signature": string, // Base64 encoded signature of the plugin.
    "manifest": {
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
    },
    "installed_version": string, // Version number of the already installed plugin, if any.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

