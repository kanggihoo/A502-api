# 11-Reset AI bridge E2E test helper [DELETE]

`DELETE /api/v4/system/e2e/ai_bridge`

Reset the in-memory AI bridge test helper state used for end-to-end tests.
This endpoint is only available when `EnableTesting` is enabled. `EnableTesting` is intended only for isolated non-production environments and must never be enabled in production.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - AI bridge test helper was reset successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

#### 501 - 

