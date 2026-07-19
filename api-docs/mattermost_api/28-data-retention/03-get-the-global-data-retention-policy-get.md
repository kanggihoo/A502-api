# 03-Get the global data retention policy [GET]

`GET /api/v4/data_retention/policy`

Gets the current global data retention policy details from the server,
including what data should be purged and the cutoff times for each data
type that should be purged.

__Minimum server version__: 4.3

##### Permissions
Requires an active session but no other permissions.

##### License
Requires an E20 license.


### Responses

#### 200 - Global data retention policy details retrieved successfully.

Schema (application/json):
```json
{
  "message_deletion_enabled": boolean, // Indicates whether data retention policy deletion of messages is enabled globally.
  "file_deletion_enabled": boolean, // Indicates whether data retention policy deletion of file attachments is enabled globally.
  "message_retention_cutoff": integer, // The current server timestamp before which messages should be deleted.
  "file_retention_cutoff": integer, // The current server timestamp before which files should be deleted.
}
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

