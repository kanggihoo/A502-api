# 15-Get cloud preview modal data [GET]

`GET /api/v4/cloud/preview/modal_data`

Retrieves modal content data from the configured S3 bucket for displaying cloud product preview modals.
##### Permissions
Must be authenticated. Must be in a Cloud Preview environment.
__Minimum server version__: 10.0 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Preview modal data returned successfully

Schema (application/json):
```json
[
  {
    "skuLabel": {
      "id": string, // The i18n message ID
      "defaultMessage": string, // The default message text
      "values": {}, // Optional values for message interpolation
    },
    "title": {
      "id": string, // The i18n message ID
      "defaultMessage": string, // The default message text
      "values": {}, // Optional values for message interpolation
    },
    "subtitle": {
      "id": string, // The i18n message ID
      "defaultMessage": string, // The default message text
      "values": {}, // Optional values for message interpolation
    },
    "videoUrl": string, // URL of the video content
    "videoPoster": string, // URL of the video poster/thumbnail image
    "useCase": string, // The use case category for this content
  }
]
```

#### 401 - 

#### 404 - 

#### 500 - 

