# 50-Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance. [GET]

`GET /api/v4/system/support_packet`

Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance.
__Minimum server version: 5.32__
##### Permissions
Must have any of the system console read permissions.
##### License
Requires either a E10 or E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `basic_server_logs` | `boolean` | `query` | No | Specifies whether the server should include or exclude log files. Default value is true.<br><br>__Minimum server version__: 9.8.0<br> |
| `plugin_packets` | `string` | `query` | No | Specifies plugin identifiers whose content should be included in the Support Packet.<br><br>__Minimum server version__: 9.8.0<br> |

### Responses

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

