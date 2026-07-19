# 18-Get configuration [GET]

`GET /api/v4/config`

Retrieve the current server configuration
##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remove_masked` | `boolean` | `query` | No | Remove masked values from the exported configuration.<br><br>__Minimum server version__: 10.4.0<br> |
| `remove_defaults` | `string` | `query` | No | Remove default values from the exported configuration.<br><br>__Minimum server version__: 10.4.0<br> |

### Responses

#### 200 - Configuration retrieval successful

Schema (application/json):
```json
{
  "ServiceSettings": {
    "SiteURL": string,
    "ListenAddress": string,
    "ConnectionSecurity": string,
    "TLSCertFile": string,
    "TLSKeyFile": string,
    "UseLetsEncrypt": boolean,
    "LetsEncryptCertificateCacheFile": string,
    "Forward80To443": boolean,
    "ReadTimeout": integer,
    "WriteTimeout": integer,
    "MaximumLoginAttempts": integer,
    "SegmentDeveloperKey": string,
    "GoogleDeveloperKey": string,
    "EnableOAuthServiceProvider": boolean,
    "EnableIncomingWebhooks": boolean,
    "EnableOutgoingWebhooks": boolean,
    "EnableCommands": boolean,
    "EnableOnlyAdminIntegrations": boolean,
    "EnablePostUsernameOverride": boolean,
    "EnablePostIconOverride": boolean,
    "EnableTesting": boolean, // Intended only for isolated non-production environments and must never be enabled in production.
    "EnableDeveloper": boolean,
    "EnableSecurityFixAlert": boolean,
    "EnableInsecureOutgoingConnections": boolean,
    "EnableMultifactorAuthentication": boolean,
    "EnforceMultifactorAuthentication": boolean,
    "AllowCorsFrom": string,
    "SessionLengthWebInDays": integer,
    "SessionLengthMobileInDays": integer,
    "SessionLengthSSOInDays": integer,
    "SessionCacheInMinutes": integer,
    "WebsocketSecurePort": integer,
    "WebsocketPort": integer,
    "WebserverMode": string,
    "EnableCustomEmoji": boolean,
    "RestrictCustomEmojiCreation": string,
  },
  "TeamSettings": {
    "SiteName": string,
    "MaxUsersPerTeam": integer,
    "EnableTeamCreation": boolean,
    "EnableUserCreation": boolean,
    "EnableOpenServer": boolean,
    "RestrictCreationToDomains": string,
    "EnableCustomBrand": boolean,
    "CustomBrandText": string,
    "CustomDescriptionText": string,
    "RestrictDirectMessage": string,
    "RestrictTeamInvite": string,
    "RestrictPublicChannelManagement": string,
    "RestrictPrivateChannelManagement": string,
    "RestrictPublicChannelCreation": string,
    "RestrictPrivateChannelCreation": string,
    "RestrictPublicChannelDeletion": string,
    "RestrictPrivateChannelDeletion": string,
    "UserStatusAwayTimeout": integer,
    "MaxChannelsPerTeam": integer,
    "MaxNotificationsPerChannel": integer,
  },
  "SqlSettings": {
    "DriverName": string,
    "DataSource": string,
    "DataSourceReplicas": [
      string
    ],
    "MaxIdleConns": integer,
    "MaxOpenConns": integer,
    "Trace": boolean,
    "AtRestEncryptKey": string,
  },
  "LogSettings": {
    "EnableConsole": boolean,
    "ConsoleLevel": string,
    "EnableFile": boolean,
    "FileLevel": string,
    "FileLocation": string,
    "EnableWebhookDebugging": boolean,
    "EnableDiagnostics": boolean,
  },
  "PasswordSettings": {
    "MinimumLength": integer,
    "Lowercase": boolean,
    "Number": boolean,
    "Uppercase": boolean,
    "Symbol": boolean,
  },
  "FileSettings": {
    "MaxFileSize": integer,
    "DriverName": string,
    "Directory": string,
    "EnablePublicLink": boolean,
    "PublicLinkSalt": string,
    "ThumbnailWidth": integer,
    "ThumbnailHeight": integer,
    "PreviewWidth": integer,
    "PreviewHeight": integer,
    "ProfileWidth": integer,
    "ProfileHeight": integer,
    "InitialFont": string,
    "AmazonS3AccessKeyId": string,
    "AmazonS3SecretAccessKey": string,
    "AmazonS3Bucket": string,
    "AmazonS3Region": string,
    "AmazonS3Endpoint": string,
    "AmazonS3SSL": boolean,
    "AmazonS3StorageClass": string,
  },
  "EmailSettings": {
    "EnableSignUpWithEmail": boolean,
    "EnableSignInWithEmail": boolean,
    "EnableSignInWithUsername": boolean,
    "SendEmailNotifications": boolean,
    "RequireEmailVerification": boolean,
    "FeedbackName": string,
    "FeedbackEmail": string,
    "FeedbackOrganization": string,
    "SMTPUsername": string,
    "SMTPPassword": string,
    "SMTPServer": string,
    "SMTPPort": string,
    "ConnectionSecurity": string,
    "InviteSalt": string,
    "PasswordResetSalt": string,
    "SendPushNotifications": boolean,
    "PushNotificationServer": string,
    "PushNotificationContents": string,
    "EnableEmailBatching": boolean,
    "EmailBatchingBufferSize": integer,
    "EmailBatchingInterval": integer,
  },
  "RateLimitSettings": {
    "Enable": boolean,
    "PerSec": integer,
    "MaxBurst": integer,
    "MemoryStoreSize": integer,
    "VaryByRemoteAddr": boolean,
    "VaryByHeader": string,
  },
  "PrivacySettings": {
    "ShowEmailAddress": boolean,
    "ShowFullName": boolean,
  },
  "SupportSettings": {
    "TermsOfServiceLink": string,
    "PrivacyPolicyLink": string,
    "AboutLink": string,
    "HelpLink": string,
    "ReportAProblemLink": string,
    "ReportAProblemType": string,
    "ReportAProblemMail": string,
    "AllowDownloadLogs": boolean,
    "SupportEmail": string,
  },
  "GitLabSettings": {
    "Enable": boolean,
    "Secret": string,
    "Id": string,
    "Scope": string,
    "AuthEndpoint": string,
    "TokenEndpoint": string,
    "UserApiEndpoint": string,
  },
  "GoogleSettings": {
    "Enable": boolean,
    "Secret": string,
    "Id": string,
    "Scope": string,
    "AuthEndpoint": string,
    "TokenEndpoint": string,
    "UserApiEndpoint": string,
  },
  "Office365Settings": {
    "Enable": boolean,
    "Secret": string,
    "Id": string,
    "Scope": string,
    "AuthEndpoint": string,
    "TokenEndpoint": string,
    "UserApiEndpoint": string,
  },
  "LdapSettings": {
    "Enable": boolean,
    "LdapServer": string,
    "LdapPort": integer,
    "ConnectionSecurity": string,
    "BaseDN": string,
    "BindUsername": string,
    "BindPassword": string,
    "UserFilter": string,
    "FirstNameAttribute": string,
    "LastNameAttribute": string,
    "EmailAttribute": string,
    "UsernameAttribute": string,
    "NicknameAttribute": string,
    "IdAttribute": string,
    "PositionAttribute": string,
    "SyncIntervalMinutes": integer,
    "SkipCertificateVerification": boolean,
    "QueryTimeout": integer,
    "MaxPageSize": integer,
    "LoginFieldName": string,
  },
  "ComplianceSettings": {
    "Enable": boolean,
    "Directory": string,
    "EnableDaily": boolean,
  },
  "LocalizationSettings": {
    "DefaultServerLocale": string,
    "DefaultClientLocale": string,
    "AvailableLocales": string,
  },
  "SamlSettings": {
    "Enable": boolean,
    "Verify": boolean,
    "Encrypt": boolean,
    "IdpUrl": string,
    "IdpDescriptorUrl": string,
    "AssertionConsumerServiceURL": string,
    "IdpCertificateFile": string,
    "PublicCertificateFile": string,
    "PrivateKeyFile": string,
    "FirstNameAttribute": string,
    "LastNameAttribute": string,
    "EmailAttribute": string,
    "UsernameAttribute": string,
    "NicknameAttribute": string,
    "LocaleAttribute": string,
    "PositionAttribute": string,
    "LoginButtonText": string,
  },
  "NativeAppSettings": {
    "AppDownloadLink": string,
    "AndroidAppDownloadLink": string,
    "IosAppDownloadLink": string,
  },
  "ClusterSettings": {
    "Enable": boolean,
    "InterNodeListenAddress": string,
    "InterNodeUrls": [
      string
    ],
  },
  "MetricsSettings": {
    "Enable": boolean,
    "BlockProfileRate": integer,
    "ListenAddress": string,
  },
  "AnalyticsSettings": {
    "MaxUsersForStatistics": integer,
  },
}
```

#### 400 - 

#### 403 - 

