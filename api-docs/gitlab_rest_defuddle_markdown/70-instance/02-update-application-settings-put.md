# 02-Update application settings [PUT]

`PUT /api/v4/application/settings`

Updates the current application settings for this GitLab instance.

### Request Body (application/json)

```json
{
  "admin_mode": boolean, // Require admin users to re-authenticate for administrative (i.e. potentially dangerous) operations
  "admin_notification_email": string, // Deprecated: Use :abuse_notification_email instead. Abuse reports will be sent to this address if it is set. Abuse reports are always available in the admin area.
  "abuse_notification_email": string, // Abuse reports will be sent to this address if it is set. Abuse reports are always available in the admin area.
  "after_sign_up_text": string, // Text shown after sign up
  "after_sign_out_path": string, // We will redirect users to this page after they sign out
  "akismet_enabled": boolean, // Helps prevent bots from creating issues
  "akismet_api_key": string, // Generate API key at http://www.akismet.com
  "asset_proxy_enabled": boolean, // Enable proxying of assets
  "asset_proxy_url": string, // URL of the asset proxy server
  "asset_proxy_secret_key": string, // Shared secret with the asset proxy server
  "asset_proxy_whitelist": [
    string
  ], // Deprecated: Use :asset_proxy_allowlist instead. Assets that match these domain(s) will NOT be proxied. Wildcards allowed. Your GitLab installation URL is automatically whitelisted.
  "asset_proxy_allowlist": [
    string
  ], // Assets that match these domain(s) will NOT be proxied. Wildcards allowed. Your GitLab installation URL is automatically allowed.
  "authn_data_retention_cleanup_enabled": boolean, // Enable authentication data retention cleanup workers to enforce retention policies
  "container_registry_token_expire_delay": integer, // Authorization token duration (minutes)
  "oauth_access_token_expires_in": integer, // Lifetime of OAuth access tokens in seconds.
  "decompress_archive_file_timeout": integer, // Default timeout for decompressing archived files, in seconds. Set to 0 to disable timeouts.
  "default_artifacts_expire_in": string, // Set the default expiration time for each job's artifacts
  "default_ci_config_path": string, // The instance default CI/CD configuration file and path for new projects
  "default_project_creation": enum(0 | 3 | 4 | 1 | 2), // Determine if developers can create projects in the group
  "default_branch_protection": enum(0 | 3 | 1 | 2 | 4), // Determine if developers can push to default branch
  "default_branch_protection_defaults": {
    "allowed_to_push": [
      {
        "access_level": enum(30 | 40 | 60 | 0) (required), // A valid access level
      }
    ], // An array of access levels allowed to push
    "allow_force_push": boolean, // Allow force push for all users with push access.
    "allowed_to_merge": [
      {
        "access_level": enum(30 | 40 | 60 | 0) (required), // A valid access level
      }
    ], // An array of access levels allowed to merge
    "code_owner_approval_required": boolean, // Require approval from code owners
    "developer_can_initial_push": boolean, // Allow developers to initial push
  }, // Determine if developers can push to default branch
  "default_group_visibility": enum("private" | "internal" | "public"), // The default group visibility
  "default_project_visibility": enum("private" | "internal" | "public"), // The default project visibility
  "default_projects_limit": integer, // The maximum number of personal projects
  "default_snippet_visibility": enum("private" | "internal" | "public"), // The default snippet visibility
  "dependency_management_settings": {
    "security_update_scheduler_max_concurrency": integer, // Maximum number of dependency management security update scheduler jobs that run concurrently across the Sidekiq fleet
  }, // Dependency management settings
  "disable_admin_oauth_scopes": boolean, // Stop administrators from connecting to non-trusted OAuth applications.
  "disable_feed_token": boolean, // Disable display of RSS/Atom and Calendar `feed_tokens`
  "disabled_oauth_sign_in_sources": [
    string
  ], // Disable certain OAuth sign-in sources
  "domain_denylist_enabled": boolean, // Enable domain denylist for sign ups
  "domain_denylist": [
    string
  ], // Users with e-mail addresses that match these domain(s) will NOT be able to sign-up. Wildcards allowed. Enter multiple entries on separate lines. Ex: domain.com, *.domain.com
  "domain_allowlist": [
    string
  ], // ONLY users with e-mail addresses that match these domain(s) will be able to sign-up. Wildcards allowed. Enter multiple entries on separate lines. Ex: domain.com, *.domain.com
  "outbound_local_requests_whitelist": [
    string
  ], // List of trusted domains or IP addresses to which local requests are allowed when local requests for webhooks and integrations are disabled.
  "email_otp_enabled": boolean, // Enable Email-based one-time passwords (OTP) as a multi-factor authentication method.
  "iframe_rendering_enabled": boolean, // Allow rendering of iframes in Markdown.
  "iframe_rendering_allowlist": [
    string
  ], // Allowed iframe src host[:port] entries. Enter multiple entries separated by commas or on separate lines.
  "iframe_rendering_allowlist_raw": string, // Raw newline- or comma-separated list of allowed iframe src host[:port] entries.
  "eks_integration_enabled": boolean, // Enable integration with Amazon EKS
  "eks_account_id": string, // Amazon account ID for EKS integration
  "eks_access_key_id": string, // Access key ID for the EKS integration IAM user
  "eks_secret_access_key": string, // Secret access key for the EKS integration IAM user
  "email_author_in_body": boolean, // Some email servers do not support overriding the email sender name. Enable this option to include the name of the author of the issue, merge request or comment in the email body instead.
  "email_confirmation_setting": enum("off" | "soft" | "hard"), // Email confirmation setting, possible values: `off`, `soft`, and `hard`
  "enabled_git_access_protocol": enum("ssh" | "http" | "all"), // Allow only the selected protocols to be used for Git access.
  "gitpod_enabled": boolean, // Enable Gitpod
  "gitpod_url": string, // The configured Gitpod instance URL
  "gitaly_timeout_default": integer, // Default Gitaly timeout, in seconds. Set to 0 to disable timeouts.
  "gitaly_timeout_fast": integer, // Gitaly fast operation timeout, in seconds. Set to 0 to disable timeouts.
  "gitaly_timeout_medium": integer, // Medium Gitaly timeout, in seconds. Set to 0 to disable timeouts.
  "grafana_enabled": boolean, // Enable Grafana
  "grafana_url": string, // Grafana URL
  "gravatar_enabled": boolean, // Flag indicating if the Gravatar service is enabled
  "help_page_hide_commercial_content": boolean, // Hide marketing-related entries from help
  "help_page_support_url": string, // Alternate support URL for help page and help dropdown
  "help_page_documentation_base_url": string, // Alternate documentation pages URL
  "help_page_text": string, // Custom text displayed on the help page
  "home_page_url": string, // We will redirect non-logged in users to this page
  "housekeeping_enabled": boolean, // Enable automatic repository housekeeping (git repack, git gc)
  "housekeeping_full_repack_period": integer, // Number of Git pushes after which a full 'git repack' is run.
  "housekeeping_gc_period": integer, // Number of Git pushes after which 'git gc' is run.
  "housekeeping_incremental_repack_period": integer, // Number of Git pushes after which an incremental 'git repack' is run.
  "housekeeping_optimize_repository_period": integer, // Number of Git pushes after which Gitaly is asked to optimize a repository.
  "html_emails_enabled": boolean, // By default GitLab sends emails in HTML and plain text formats so mail clients can choose what format to use. Disable this option if you only want to send emails in plain text format.
  "import_sources": [
    string
  ], // Enabled sources for code import during project creation. OmniAuth must be configured for GitHub, Bitbucket, and GitLab.com
  "invisible_captcha_enabled": boolean, // Enable Invisible Captcha spam detection during signup.
  "max_artifacts_size": integer, // Set the maximum file size for each job's artifacts
  "max_attachment_size": integer, // Maximum attachment size in MB
  "max_export_size": integer, // Maximum export size in MB
  "max_github_response_size_limit": integer, // Maximum allowed size in MB for GitHub API responses. 0 for unlimited.
  "max_github_response_json_value_count": integer, // Maximum allowed object count for GitHub API responses. 0 for unlimited. Count is an estimate based on the number of : , { and [ occurrences in the response.
  "max_import_size": integer, // Maximum import size in MB
  "max_import_remote_file_size": integer, // Maximum remote file size in MB for imports from external object storages
  "max_decompressed_archive_size": integer, // Maximum decompressed size in MB
  "max_pages_size": integer, // Maximum size of pages in MB
  "max_pages_custom_domains_per_project": integer, // Maximum number of GitLab Pages custom domains per project
  "max_terraform_state_size_bytes": integer, // Maximum size in bytes of the Terraform state file. Set this to 0 for unlimited file size.
  "metrics_method_call_threshold": integer, // A method call is only tracked when it takes longer to complete than the given amount of milliseconds.
  "password_authentication_enabled": boolean, // Flag indicating if password authentication is enabled for the web interface
  "password_authentication_enabled_for_web": boolean, // Flag indicating if password authentication is enabled for the web interface
  "signin_enabled": boolean, // Flag indicating if password authentication is enabled for the web interface
  "password_authentication_enabled_for_git": boolean, // Flag indicating if password authentication is enabled for Git over HTTP(S)
  "performance_bar_allowed_group_id": string, // Deprecated: Use :performance_bar_allowed_group_path instead. Path of the group that is allowed to toggle the performance bar.
  "performance_bar_allowed_group_path": string, // Path of the group that is allowed to toggle the performance bar.
  "performance_bar_enabled": string, // Deprecated: Pass `performance_bar_allowed_group_path: nil` instead. Allow enabling the performance.
  "personal_access_token_prefix": string, // Prefix to prepend to all personal access tokens
  "require_personal_access_token_expiry": boolean, // Flag indicating if Personal / Group / Project access token expiry is required
  "kroki_enabled": boolean, // Enable Kroki
  "kroki_url": string, // The Kroki server URL
  "plantuml_enabled": boolean, // Enable PlantUML
  "plantuml_url": string, // The PlantUML server URL
  "diagramsnet_enabled": boolean, // Enable Diagrams.net
  "diagramsnet_url": string, // The Diagrams.net server URL
  "polling_interval_multiplier": number, // Interval multiplier used by endpoints that perform polling. Set to 0 to disable polling.
  "project_export_enabled": boolean, // Enable project export
  "prometheus_metrics_enabled": boolean, // Enable Prometheus metrics
  "push_event_hooks_limit": integer, // Maximum number of changes (branches or tags) in a single push above which webhooks and integrations are not triggered. Setting to `0` does not disable throttling.
  "push_event_activities_limit": integer, // Maximum number of changes (branches or tags) in a single push above which a bulk push event is created. Setting to `0` does not disable throttling.
  "recaptcha_enabled": boolean, // Helps prevent bots from creating accounts
  "recaptcha_site_key": string, // Generate site key at http://www.google.com/recaptcha
  "recaptcha_private_key": string, // Generate private key at http://www.google.com/recaptcha
  "login_recaptcha_protection_enabled": boolean, // Helps prevent brute-force attacks
  "repository_checks_enabled": boolean, // GitLab will periodically run 'git fsck' in all project and wiki repositories to look for silent disk corruption issues.
  "repository_storages_weighted": {}, // Storage paths for new projects with a weighted value ranging from 0 to 100
  "require_two_factor_authentication": boolean, // Require all users to set up Two-factor authentication
  "two_factor_grace_period": integer, // Amount of time (in hours) that users are allowed to skip forced configuration of two-factor authentication
  "restricted_visibility_levels": [
    string
  ], // Selected levels cannot be used by non-admin users for groups, projects or snippets. If the public level is restricted, user profiles are only visible to logged in users.
  "session_expire_delay": integer, // Session duration in minutes. GitLab restart is required to apply changes.
  "session_expire_from_init": boolean, // Expires sessions based off the creation date rather than last activity
  "shared_runners_enabled": boolean, // Enable shared runners for new projects
  "shared_runners_text": string, // Shared runners text 
  "valid_runner_registrars": [
    string
  ], // List of types which are allowed to register a GitLab runner
  "signup_enabled": boolean, // Flag indicating if sign up is enabled
  "sourcegraph_enabled": boolean, // Enable Sourcegraph
  "sourcegraph_public_only": boolean, // Only allow public projects to communicate with Sourcegraph
  "sourcegraph_url": string, // The configured Sourcegraph instance URL
  "spam_check_endpoint_enabled": boolean, // Enable Spam Check via external API endpoint
  "spam_check_endpoint_url": string, // The URL of the external Spam Check service endpoint
  "terminal_max_session_time": integer, // Maximum time for web terminal websocket connection (in seconds). Set to 0 for unlimited time.
  "usage_ping_enabled": boolean, // Every week GitLab will report license usage back to GitLab, Inc.
  "local_markdown_version": integer, // Local markdown version, increase this value when any cached markdown should be invalidated
  "allow_local_requests_from_hooks_and_services": boolean, // Deprecated: Use :allow_local_requests_from_web_hooks_and_services instead. Allow requests to the local network from hooks and services.
  "mailgun_events_enabled": boolean, // Enable Mailgun event receiver
  "mailgun_signing_key": string, // The Mailgun HTTP webhook signing key for receiving events from webhook
  "snowplow_enabled": boolean, // Enable Snowplow tracking
  "snowplow_collector_hostname": string, // The Snowplow collector hostname
  "snowplow_cookie_domain": string, // The Snowplow cookie domain
  "snowplow_app_id": string, // The Snowplow site name / application id
  "issues_create_limit": integer, // Maximum number of issue creation requests allowed per minute per user. Set to 0 for unlimited requests per minute.
  "raw_blob_request_limit": integer, // Maximum number of requests per minute for each raw path. Set to 0 for unlimited requests per minute.
  "raw_blob_request_limit_unauthenticated": integer, // Maximum number of requests per minute for a raw blob for unauthenticated requests. Set to 0 for unlimited requests per minute.
  "wiki_page_max_content_bytes": integer, // Maximum wiki page content size in bytes
  "description_and_note_max_size": integer, // Maximum work item, merge request, and vulnerability description and comment content size in bytes.
  "wiki_asciidoc_allow_uri_includes": boolean, // Allow URI includes for AsciiDoc wiki pages
  "require_admin_approval_after_user_signup": boolean, // Require explicit admin approval for new signups
  "whats_new_variant": enum("all_tiers" | "current_tier" | "disabled"), // What's new variant, possible values: `all_tiers`, `current_tier`, and `disabled`.
  "floc_enabled": boolean, // Enable FloC (Federated Learning of Cohorts)
  "user_deactivation_emails_enabled": boolean, // Send emails to users upon account deactivation
  "suggest_pipeline_enabled": boolean, // Enable pipeline suggestion banner
  "show_migrate_from_jenkins_banner": boolean, // Enable Jenkins migration banner
  "enable_artifact_external_redirect_warning_page": boolean, // Show the external redirect page that warns you about user-generated content in GitLab Pages
  "users_get_by_id_limit": integer, // Maximum number of calls to the /users/:id API per 10 minutes per user. Set to 0 for unlimited requests.
  "runner_token_expiration_interval": integer, // Token expiration interval for shared runners, in seconds
  "group_runner_token_expiration_interval": integer, // Token expiration interval for group runners, in seconds
  "project_runner_token_expiration_interval": integer, // Token expiration interval for project runners, in seconds
  "pipeline_limit_per_project_user_sha": integer, // Maximum number of pipeline creation requests allowed per minute per user and commit. Set to 0 for unlimited requests per minute.
  "pipeline_limit_per_user": integer, // Maximum number of pipeline creation requests allowed per minute per user. Set to 0 for unlimited requests per minute.
  "ci_lint_limit_per_user": integer, // Maximum number of CI Lint requests allowed per minute per user. Set to 0 for unlimited requests per minute.
  "jira_connect_application_key": string, // ID of the OAuth application used to authenticate with the GitLab for Jira Cloud app.
  "jira_connect_public_key_storage_enabled": boolean, // Enable public key storage for the GitLab for Jira Cloud app.
  "jira_connect_proxy_url": string, // URL of the GitLab instance used as a proxy for the GitLab for Jira Cloud app.
  "jira_forge_app_id": string, // Atlassian Forge app ID (ARI) of the GitLab for Jira Cloud app, used to verify inbound Forge Invocation Tokens.
  "bulk_import_concurrent_pipeline_batch_limit": integer, // Maximum simultaneous direct transfer batch exports to process.
  "concurrent_relation_batch_export_limit": integer, // Maximum number of simultaneous batch export jobs to process.
  "bulk_import_enabled": boolean, // Enable migrating GitLab groups and projects by direct transfer
  "bulk_import_max_download_file": integer, // Maximum download file size in MB when importing from source GitLab instances by direct transfer
  "autocomplete_users_limit": integer, // Rate limit for authenticated requests to users autocomplete endpoint
  "autocomplete_users_unauthenticated_limit": integer, // Rate limit for authenticated requests to users autocomplete endpoint
  "concurrent_github_import_jobs_limit": integer, // Github Importer maximum number of simultaneous import jobs
  "concurrent_bitbucket_import_jobs_limit": integer, // Bitbucket Cloud Importer maximum number of simultaneous import jobs
  "concurrent_bitbucket_server_import_jobs_limit": integer, // Bitbucket Server Importer maximum number of simultaneous import jobs
  "allow_runner_registration_token": boolean, // Allow registering runners using a registration token
  "ci_max_includes": integer, // Maximum number of includes per pipeline
  "ci_max_caches_per_job": integer, // Maximum number of caches that can be defined in a single CI/CD job
  "ci_job_live_trace_enabled": boolean, // Turn on incremental logging for job logs.
  "git_push_pipeline_limit": integer, // Set the limit for pipelines and branches that can be triggered when creating a Git push. Set to 0 to disable the limit
  "security_policy_global_group_approvers_enabled": boolean, // Query scan result policy approval groups globally
  "slack_app_enabled": boolean, // Enable the GitLab for Slack app
  "slack_app_id": string, // The client ID of the GitLab for Slack app
  "slack_app_secret": string, // The client secret of the GitLab for Slack app. Used for authenticating OAuth requests from the app
  "slack_app_signing_secret": string, // The signing secret of the GitLab for Slack app. Used for authenticating API requests from the app
  "slack_app_verification_token": string, // The verification token of the GitLab for Slack app. This method of authentication is deprecated by Slack and used only for authenticating slash commands from the app
  "namespace_aggregation_schedule_lease_duration_in_seconds": integer, // Maximum duration (in seconds) between refreshes of namespace statistics (Default: 300)
  "project_jobs_api_rate_limit": integer, // Maximum authenticated requests to /project/:id/jobs per minute
  "security_txt_content": string, // Public security contact information made available at https://gitlab.example.com/.well-known/security.txt
  "downstream_pipeline_trigger_limit_per_project_user_sha": integer, // Maximum number of downstream pipelines that can be triggered per minute (for a given project, user, and commit).
  "ai_action_api_rate_limit": integer, // Maximum requests a user can make per 8 hours to aiAction endpoint
  "code_suggestions_api_rate_limit": integer, // Maximum requests a user can make per minute to code suggestions endpoint
  "resource_usage_limits": {}, // Definition for resource usage limits enforced in Sidekiq workers
  "vscode_extension_marketplace": {
    "enabled": boolean, // Enables VS Code Extension Marketplace for Web IDE and Workspaces
    "preset": string, // The preset configuration of URL's for the VS Code Extension Marketplace
    "custom_values": {}, // VS Code Extension Marketplace URL's when preset is 'custom'
  }, // Settings for VS Code Extension Marketplace
  "enable_language_server_restrictions": boolean, // Enables enforcing language server restrictions
  "minimum_language_server_version": string, // The minimum language server version to accept requests from
  "terraform_state_encryption_enabled": boolean, // Enable encryption for Terraform state files
  "logging_field_schema_version": enum(0 | 1), // Logging field schema version (v0, v1, …). Cannot be downgraded.
  "logging_field_dual_emit_target": enum(1), // Version to dual-emit alongside schema_version. Must be strictly greater than schema_version, or omit/null to disable.
  "rsa_key_restriction": enum(0 | 1024 | 2048 | 3072 | 4096 | -1), // Restrictions on the complexity of uploaded RSA keys. A value of -1 disables all RSA keys.
  "dsa_key_restriction": enum(0 | 1024 | 2048 | 3072 | -1), // Restrictions on the complexity of uploaded DSA keys. A value of -1 disables all DSA keys.
  "ecdsa_key_restriction": enum(0 | 256 | 384 | 521 | -1), // Restrictions on the complexity of uploaded ECDSA keys. A value of -1 disables all ECDSA keys.
  "ed25519_key_restriction": enum(0 | 256 | -1), // Restrictions on the complexity of uploaded ED25519 keys. A value of -1 disables all ED25519 keys.
  "ecdsa_sk_key_restriction": enum(0 | 256 | -1), // Restrictions on the complexity of uploaded ECDSA_SK keys. A value of -1 disables all ECDSA_SK keys.
  "ed25519_sk_key_restriction": enum(0 | 256 | -1), // Restrictions on the complexity of uploaded ED25519_SK keys. A value of -1 disables all ED25519_SK keys.
  "elasticsearch_aws": boolean, // Enable support for AWS hosted elasticsearch
  "elasticsearch_aws_access_key": string, // AWS IAM access key
  "elasticsearch_aws_region": string, // The AWS region the elasticsearch domain is configured
  "elasticsearch_aws_secret_access_key": string, // AWS IAM secret access key
  "elasticsearch_indexing": boolean, // Enable Elasticsearch indexing
  "elasticsearch_search": boolean, // Enable Elasticsearch search
  "elasticsearch_pause_indexing": boolean, // Pause Elasticsearch indexing (global control for both Advanced Search and ActiveContext)
  "elasticsearch_advanced_search_pause_indexing": boolean, // Pause advanced search indexing
  "elasticsearch_url": string, // The url to use for connecting to Elasticsearch. Use a comma-separated list to support clustering (e.g., "http://localhost:9200, http://localhost:9201")
  "elasticsearch_username": string, // The username of your Elasticsearch instance.
  "elasticsearch_password": string, // The password of your Elasticsearch instance.
  "elasticsearch_limit_indexing": boolean, // Limit Elasticsearch to index certain namespaces and projects
  "active_context_pause_indexing": boolean, // Pause ActiveContext indexing
  "elasticsearch_namespace_ids": [
    integer
  ], // The namespace ids to index with Elasticsearch.
  "elasticsearch_project_ids": [
    integer
  ], // The project ids to index with Elasticsearch.
  "secret_detection_token_revocation_enabled": boolean, // Enable Secret Detection Token Revocation
  "secret_detection_token_revocation_url": string, // The configured Secret Detection Token Revocation instance URL
  "secret_detection_revocation_token_types_url": string, // The configured Secret Detection Revocation Token Types instance URL
  "email_additional_text": string, // Additional text added to the bottom of every email for legal/auditing/compliance reasons
  "default_project_deletion_protection": boolean, // Disable project owners ability to delete project
  "disable_personal_access_tokens": boolean, // Disable personal access tokens
  "repository_size_limit": integer, // Size limit per repository (MB)
  "file_template_project_id": integer, // ID of project where instance-level file templates are stored.
  "updating_name_disabled_for_users": boolean, // Flag indicating if users are permitted to update their profile name
  "disable_overriding_approvers_per_merge_request": boolean, // Disable Users ability to overwrite approvers in merge requests.
  "prevent_merge_requests_author_approval": boolean, // Disable Merge request author ability to approve request.
  "prevent_merge_requests_committers_approval": boolean, // Disable Merge request committer ability to approve request.
  "maven_package_requests_forwarding": boolean, // Maven package requests are forwarded to repo.maven.apache.org if not found on GitLab.
  "npm_package_requests_forwarding": boolean, // NPM package requests are forwarded to npmjs.org if not found on GitLab.
  "pypi_package_requests_forwarding": boolean, // PyPI package requests are forwarded to pypi.org if not found on GitLab.
  "virtual_registries_endpoints_api_limit": integer, // Virtual Registries API endpoints rate limit.
  "group_owners_can_manage_default_branch_protection": boolean, // Allow owners to manage default branch protection in groups
  "maintenance_mode": boolean, // When instance is in maintenance mode, non-admin users can sign in with read-only access and make read-only API requests
  "maintenance_mode_message": string, // Message displayed when instance is in maintenance mode
  "git_two_factor_session_expiry": integer, // Maximum duration (in minutes) of a session for Git operations when 2FA is enabled
  "max_number_of_repository_downloads": integer, // Maximum number of unique repositories a user can download in the specified time period before they are banned
  "max_number_of_repository_downloads_within_time_period": integer, // Reporting time period (in seconds)
  "git_rate_limit_users_allowlist": [
    string
  ], // List of usernames excluded from Git anti-abuse rate limits
  "git_rate_limit_users_alertlist": [
    integer
  ], // List of user ids who will be emailed when Git abuse rate limit is exceeded
  "auto_ban_user_on_excessive_projects_download": boolean, // Ban users from the application when they exceed maximum number of unique projects download in the specified time period
  "make_profile_private": boolean, // Flag indicating if users are permitted to make their profiles private
  "service_access_tokens_expiration_enforced": boolean, // To enforce token expiration for Service accounts users
  "duo_features_enabled": boolean, // Indicates whether GitLab Duo features are enabled for the group
  "lock_duo_features_enabled": boolean, // Indicates if the GitLab Duo features enabled setting is enforced for all subgroups
  "disabled_direct_code_suggestions": boolean, // Indicates if direct connection for Code Suggestions is disabled for users
  "receptive_cluster_agents_enabled": boolean, // Enable receptive mode for GitLab Agents for Kubernetes
  "auto_duo_code_review_enabled": boolean, // Enable automatic reviews by GitLab Duo on merge requests
  "security_scan_stale_after_days": integer, // Number of days before security scan data is considered stale (7-90)
  "duo_custom_agents_enabled": boolean, // Indicates whether custom agents are allowed for this instance
  "lock_duo_custom_agents_enabled": boolean, // Indicates if the custom agents enabled setting is enforced for all groups
  "duo_custom_flows_enabled": boolean, // Indicates whether custom flows are allowed for this instance
  "lock_duo_custom_flows_enabled": boolean, // Indicates if the custom flows enabled setting is enforced for all groups
  "duo_external_agents_enabled": boolean, // Indicates whether external agents are allowed for this instance
  "lock_duo_external_agents_enabled": boolean, // Indicates if the external agents enabled setting is enforced for all groups
  "duo_remote_flows_enabled": boolean, // Indicates whether GitLab Duo remote flows are enabled for the instance
  "lock_duo_remote_flows_enabled": boolean, // Indicates if the GitLab Duo remote flows enabled setting is enforced for all subgroups
  "duo_workflows_default_image_registry": string, // Default container registry for Duo Agent Platform foundational flow images
  "ci_telemetry_otel_endpoint": string, // OTEL Collector endpoint URL for CI job telemetry
  "ci_job_telemetry_sampling_rate": number, // Sampling rate for CI job telemetry (0.0 to 1.0)
  "duo_namespace_access_rules": [
    {
      "through_namespace": {
        "id": integer (required), // ID of the through namespace
        "name": string, // Name of the through namespace
        "full_path": string, // Full path of the through namespace
      }, // Object containing through namespace information
      "features": [
        string
      ] (required), // List of accessible features
    }
  ], // AI entity access rules for controlling Duo feature access
  "built_in_project_templates_enabled": boolean, // Enable built-in project templates for project creation
  "lock_built_in_project_templates_enabled": boolean, // Enforce the built-in project templates setting for all groups
  "duo_template_project_id": integer, // The ID of a project to use as the Duo Code Review custom instructions template for this instance
  "allow_local_requests_from_web_hooks_and_services": string,
  "allow_local_requests_from_system_hooks": string,
  "allow_possible_spam": string,
  "dns_rebinding_protection_enabled": string,
  "archive_builds_in_human_readable": string,
  "static_objects_external_storage_auth_token": string,
  "static_objects_external_storage_url": string,
  "authorized_keys_enabled": string,
  "auto_devops_enabled": string,
  "auto_devops_domain": string,
  "allow_bypass_placeholder_confirmation": string,
  "ci_delete_pipelines_in_seconds_limit_human_readable": string,
  "ci_partitions_in_seconds_limit_human_readable": string,
  "container_expiration_policies_enable_historic_entries": string,
  "container_registry_expiration_policies_caching": string,
  "default_branch_name": string,
  "default_preferred_language": string,
  "default_syntax_highlighting_theme": string,
  "default_dark_syntax_highlighting_theme": string,
  "delete_inactive_projects": string,
  "deletion_adjourned_period": string,
  "deny_all_requests_except_allowed": string,
  "disable_password_authentication_for_users_with_sso_identities": string,
  "root_moved_permanently_redirection": string,
  "domain_denylist_raw": string,
  "domain_allowlist_raw": string,
  "outbound_local_requests_allowlist_raw": string,
  "enforce_ci_inbound_job_token_scope_enabled": string,
  "enforce_email_subaddress_restrictions": string,
  "require_email_verification_on_account_locked": string,
  "enforce_terms": string,
  "error_tracking_enabled": string,
  "error_tracking_api_url": string,
  "external_pipeline_validation_service_timeout": string,
  "external_pipeline_validation_service_token": string,
  "external_pipeline_validation_service_url": string,
  "failed_login_attempts_unlock_period_in_minutes": string,
  "first_day_of_week": string,
  "force_pages_access_control": string,
  "hashed_storage_enabled": string,
  "hide_third_party_offers": string,
  "inactive_resource_access_tokens_delete_after_days": string,
  "inactive_projects_delete_after_months": string,
  "inactive_projects_min_size_mb": string,
  "inactive_projects_send_warning_email_after_months": string,
  "include_optional_metrics_in_service_ping": string,
  "jira_connect_additional_audience_url": string,
  "math_rendering_limits_enabled": string,
  "require_sha_for_merge": string,
  "lock_require_sha_for_merge": string,
  "max_artifacts_content_include_size": string,
  "max_http_decompressed_size": string,
  "max_http_response_size_limit": string,
  "max_http_response_json_depth": string,
  "max_http_response_json_structural_chars": string,
  "max_http_response_xml_structural_chars": string,
  "max_http_response_csv_structural_chars": string,
  "max_login_attempts": string,
  "max_yaml_size_bytes": string,
  "max_yaml_depth": string,
  "minimum_password_length": string,
  "mirror_available": string,
  "notify_on_unknown_sign_in": string,
  "organization_cluster_agent_authorization_enabled": string,
  "pages_domain_verification_enabled": string,
  "pages_unique_domain_default_enabled": string,
  "instance_token_prefix": string,
  "kroki_formats": string,
  "kroki_diagram_proxy_enabled": string,
  "plantuml_diagram_proxy_enabled": string,
  "pages_extra_deployments_default_expiry_seconds": string,
  "receive_max_input_size": string,
  "require_admin_two_factor_authentication": string,
  "remember_me_enabled": string,
  "sign_in_restrictions": string,
  "silent_mode_enabled": string,
  "spam_check_api_key": string,
  "terms": string,
  "throttle_authenticated_api_enabled": string,
  "throttle_authenticated_api_period_in_seconds": string,
  "throttle_authenticated_api_requests_per_period": string,
  "throttle_authenticated_git_http_enabled": string,
  "throttle_authenticated_git_http_period_in_seconds": string,
  "throttle_authenticated_git_http_requests_per_period": string,
  "throttle_authenticated_git_lfs_enabled": string,
  "throttle_authenticated_git_lfs_period_in_seconds": string,
  "throttle_authenticated_git_lfs_requests_per_period": string,
  "throttle_authenticated_web_enabled": string,
  "throttle_authenticated_web_period_in_seconds": string,
  "throttle_authenticated_web_requests_per_period": string,
  "throttle_authenticated_packages_api_enabled": string,
  "throttle_authenticated_packages_api_period_in_seconds": string,
  "throttle_authenticated_packages_api_requests_per_period": string,
  "throttle_authenticated_files_api_enabled": string,
  "throttle_authenticated_files_api_period_in_seconds": string,
  "throttle_authenticated_files_api_requests_per_period": string,
  "throttle_authenticated_deprecated_api_enabled": string,
  "throttle_authenticated_deprecated_api_period_in_seconds": string,
  "throttle_authenticated_deprecated_api_requests_per_period": string,
  "throttle_unauthenticated_api_enabled": string,
  "throttle_unauthenticated_api_period_in_seconds": string,
  "throttle_unauthenticated_api_requests_per_period": string,
  "throttle_unauthenticated_enabled": string,
  "throttle_unauthenticated_period_in_seconds": string,
  "throttle_unauthenticated_requests_per_period": string,
  "throttle_unauthenticated_packages_api_enabled": string,
  "throttle_unauthenticated_packages_api_period_in_seconds": string,
  "throttle_unauthenticated_packages_api_requests_per_period": string,
  "throttle_unauthenticated_files_api_enabled": string,
  "throttle_unauthenticated_files_api_period_in_seconds": string,
  "throttle_unauthenticated_files_api_requests_per_period": string,
  "throttle_unauthenticated_git_http_enabled": string,
  "throttle_unauthenticated_git_http_period_in_seconds": string,
  "throttle_unauthenticated_git_http_requests_per_period": string,
  "throttle_unauthenticated_deprecated_api_enabled": string,
  "throttle_unauthenticated_deprecated_api_period_in_seconds": string,
  "throttle_unauthenticated_deprecated_api_requests_per_period": string,
  "throttle_protected_paths_enabled": string,
  "throttle_protected_paths_period_in_seconds": string,
  "throttle_protected_paths_requests_per_period": string,
  "top_level_group_creation_enabled": string,
  "protected_paths_raw": string,
  "protected_paths_for_get_request_raw": string,
  "time_tracking_limit_to_hours": string,
  "update_runner_versions_enabled": string,
  "unique_ips_limit_enabled": string,
  "unique_ips_limit_per_user": string,
  "unique_ips_limit_time_window": string,
  "usage_ping_generation_enabled": string,
  "usage_ping_features_enabled": string,
  "use_clickhouse_for_analytics": string,
  "user_default_external": string,
  "user_show_add_ssh_key_message": string,
  "user_default_internal_regex": string,
  "user_oauth_applications": string,
  "version_check_enabled": string,
  "diff_max_patch_bytes": string,
  "diff_max_files": string,
  "diff_max_lines": string,
  "diff_max_versions": string,
  "diff_max_commits": string,
  "commit_email_hostname": string,
  "protected_ci_variables": string,
  "snowplow_database_collector_hostname": string,
  "gitlab_product_usage_data_enabled": string,
  "custom_http_clone_url_root": string,
  "snippet_size_limit": string,
  "email_restrictions_enabled": string,
  "email_restrictions": string,
  "notes_create_limit": string,
  "notes_create_limit_allowlist_raw": string,
  "members_delete_limit": string,
  "project_import_limit": string,
  "project_export_limit": string,
  "project_download_export_limit": string,
  "group_import_limit": string,
  "group_export_limit": string,
  "group_download_export_limit": string,
  "container_registry_delete_tags_service_timeout": string,
  "rate_limiting_response_text": string,
  "package_registry_allow_anyone_to_pull_option": string,
  "package_registry_cleanup_policies_worker_capacity": string,
  "container_registry_expiration_policies_worker_capacity": string,
  "container_registry_cleanup_tags_service_max_list_size": string,
  "keep_latest_artifact": string,
  "resource_access_token_notify_inherited": string,
  "lock_resource_access_token_notify_inherited": string,
  "sentry_enabled": string,
  "sentry_dsn": string,
  "sentry_clientside_dsn": string,
  "sentry_environment": string,
  "sentry_clientside_traces_sample_rate": string,
  "sidekiq_job_limiter_mode": string,
  "sidekiq_job_limiter_compression_threshold_bytes": string,
  "sidekiq_job_limiter_limit_bytes": string,
  "search_rate_limit": string,
  "search_rate_limit_unauthenticated": string,
  "search_rate_limit_allowlist_raw": string,
  "users_get_by_id_limit_allowlist_raw": string,
  "invitation_flow_enforcement": string,
  "can_create_group": string,
  "can_create_organization": string,
  "relation_export_batch_size": string,
  "bulk_import_max_download_file_size": string,
  "silent_admin_exports_enabled": string,
  "allow_contribution_mapping_to_admins": string,
  "allow_s3_compatible_storage_for_offline_transfer": string,
  "user_defaults_to_private_profile": string,
  "deactivation_email_additional_text": string,
  "projects_api_rate_limit_unauthenticated": string,
  "group_api_limit": string,
  "group_archive_unarchive_api_limit": string,
  "group_invited_groups_api_limit": string,
  "group_shared_groups_api_limit": string,
  "group_projects_api_limit": string,
  "groups_api_limit": string,
  "project_api_limit": string,
  "project_invited_groups_api_limit": string,
  "projects_api_limit": string,
  "project_members_api_limit": string,
  "create_organization_api_limit": string,
  "user_contributed_projects_api_limit": string,
  "user_projects_api_limit": string,
  "user_starred_projects_api_limit": string,
  "users_api_limit_followers": string,
  "users_api_limit_following": string,
  "users_api_limit_status": string,
  "users_api_limit_ssh_keys": string,
  "users_api_limit_ssh_key": string,
  "users_api_limit_gpg_keys": string,
  "users_api_limit_gpg_key": string,
  "gitlab_dedicated_instance": string,
  "gitlab_environment_toolkit_instance": string,
  "allow_account_deletion": string,
  "gitlab_shell_operation_limit": string,
  "ci_max_total_yaml_size_bytes": string,
  "allow_project_creation_for_guest_and_below": string,
  "asciidoc_max_includes": string,
  "observability_backend_ssl_verification_enabled": string,
  "global_search_snippet_titles_enabled": string,
  "global_search_users_enabled": string,
  "global_search_work_items_enabled": string,
  "global_search_merge_requests_enabled": string,
  "global_search_block_anonymous_searches_enabled": string,
  "vscode_extension_marketplace_enabled": string,
  "vscode_extension_marketplace_extension_host_domain": string,
  "vscode_extension_marketplace_single_origin_fallback_enabled": string,
  "reindexing_minimum_index_size": string,
  "reindexing_minimum_relative_bloat_size": string,
  "anonymous_searches_allowed": string,
  "default_search_scope": string,
  "delay_user_account_self_deletion": string,
  "runner_jobs_request_api_limit": string,
  "runner_jobs_patch_trace_api_limit": string,
  "runner_jobs_endpoints_api_limit": string,
  "background_operations_max_jobs": string,
  "enforce_granular_tokens": string,
  "granular_tokens_enforced_after": string,
  "deactivate_dormant_users": string,
  "deactivate_dormant_users_period": string,
  "nuget_skip_metadata_url_validation": string,
  "helm_max_packages_count": string,
  "mcp_server_enabled": string,
  "allow_all_integrations": string,
  "allowed_integrations": string,
  "allow_group_owners_to_manage_ldap": string,
  "automatic_purchased_storage_allocation": string,
  "check_namespace_plan": string,
  "ci_cd_catalog_projects_allowlist": string,
  "ci_cd_catalog_projects_allowlist_raw": string,
  "duo_chat_expiration_column": string,
  "duo_chat_expiration_days": string,
  "elasticsearch_aws_role_arn": string,
  "elasticsearch_client_adapter": string,
  "elasticsearch_client_request_timeout": string,
  "elasticsearch_indexed_field_length_limit": string,
  "elasticsearch_indexed_file_size_limit_kb": string,
  "elasticsearch_indexing_timeout_minutes": string,
  "elasticsearch_requeue_workers": string,
  "elasticsearch_worker_number_of_shards": string,
  "elasticsearch_max_bulk_concurrency": string,
  "elasticsearch_max_bulk_size_mb": string,
  "elasticsearch_max_code_indexing_concurrency": string,
  "elasticsearch_retry_on_failure": string,
  "elasticsearch_replicas": string,
  "elasticsearch_shards": string,
  "elasticsearch_analyzers_smartcn_enabled": string,
  "elasticsearch_analyzers_smartcn_search": string,
  "elasticsearch_analyzers_kuromoji_enabled": string,
  "elasticsearch_analyzers_kuromoji_search": string,
  "elasticsearch_code_scope": string,
  "enforce_namespace_storage_limit": string,
  "geo_node_allowed_ips": string,
  "geo_status_timeout": string,
  "instance_level_ai_beta_features_enabled": string,
  "lock_memberships_to_ldap": string,
  "lock_memberships_to_saml": string,
  "lock_model_prompt_cache_enabled": string,
  "max_personal_access_token_lifetime": string,
  "max_ssh_key_lifetime": string,
  "model_prompt_cache_enabled": string,
  "search_max_shard_size_gb": string,
  "search_max_docs_denominator": string,
  "search_min_docs_before_rollover": string,
  "secret_detection_token_revocation_token": string,
  "shared_runners_minutes": string,
  "throttle_incident_management_notification_enabled": string,
  "throttle_incident_management_notification_per_period": string,
  "throttle_incident_management_notification_period_in_seconds": string,
  "package_metadata_purl_types": string,
  "product_analytics_enabled": string,
  "product_analytics_data_collector_host": string,
  "product_analytics_configurator_connection_string": string,
  "cube_api_base_url": string,
  "cube_api_key": string,
  "security_approval_policies_limit": string,
  "duo_availability": string,
  "duo_agent_platform_enabled": string,
  "duo_cli_enabled": string,
  "ai_audit_events_streaming_enabled": string,
  "duo_remote_flows_availability": string,
  "duo_foundational_flows_enabled": string,
  "duo_foundational_flows_availability": string,
  "duo_custom_agents_availability": string,
  "duo_custom_flows_availability": string,
  "duo_external_agents_availability": string,
  "tool_approval_for_session_enabled": string,
  "tool_approval_for_session_availability": string,
  "enabled_expanded_logging": string,
  "foundational_agents_default_enabled": string,
  "foundational_agents_statuses": string,
  "zoekt_indexing_enabled": string,
  "zoekt_search_enabled": string,
  "zoekt_indexing_paused": string,
  "zoekt_auto_index_root_namespace": string,
  "zoekt_cache_response": string,
  "zoekt_cpu_to_tasks_ratio": string,
  "zoekt_force_reindexing_percentage": string,
  "zoekt_indexing_parallelism": string,
  "zoekt_rollout_batch_size": string,
  "zoekt_lost_node_threshold": string,
  "zoekt_indexing_timeout": string,
  "zoekt_maximum_files": string,
  "zoekt_indexed_file_size_limit": string,
  "zoekt_trigram_max": string,
  "zoekt_rollout_retry_interval": string,
  "zoekt_default_number_of_replicas": string,
  "zoekt_max_projects_for_legacy_search": string,
  "zoekt_max_restarts_15m": string,
  "duo_workflow_oauth_application_id": string,
  "scan_execution_policies_action_limit": string,
  "scan_execution_policies_schedule_limit": string,
  "pipeline_execution_policies_per_configuration_limit": string,
  "scan_execution_policies_per_configuration_limit": string,
  "vulnerability_management_policies_per_configuration_limit": string,
  "dependency_firewall_policies_per_configuration_limit": string,
  "secret_detection_service_auth_token": string,
  "secret_detection_service_url": string,
  "fetch_observability_alerts_from_cloud": string,
  "global_search_code_enabled": string,
  "global_search_commits_enabled": string,
  "global_search_wiki_enabled": string,
  "global_search_limited_indexing_enabled": string,
  "elastic_migration_worker_enabled": string,
  "enforce_pipl_compliance": string,
  "display_gitlab_credits_user_data": string,
  "project_secrets_limit": string,
  "group_secrets_limit": string,
  "security_mr_report_cache_lifetime_minutes": string,
  "vac_project_ids_raw": string,
  "enable_member_promotion_management": string,
  "external_auth_client_cert": string,
  "external_auth_client_key": string,
  "external_auth_client_key_pass": string,
  "external_authorization_service_default_label": string,
  "external_authorization_service_enabled": string,
  "external_authorization_service_timeout": string,
  "external_authorization_service_url": string,
  "allow_deploy_tokens_and_keys_with_external_authn": string,
  "ci_partitions_in_seconds_limit": string,
  "throttle_unauthenticated_web_enabled": string,
  "throttle_unauthenticated_web_period_in_seconds": string,
  "throttle_unauthenticated_web_requests_per_period": string,
  "mirror_max_capacity": string,
  "mirror_max_delay": string,
  "mirror_capacity_threshold": string,
  "password_number_required": string,
  "password_symbol_required": string,
  "password_uppercase_required": string,
  "password_lowercase_required": string,
  "delete_unconfirmed_users": string,
  "unconfirmed_users_delete_after_days": string,
  "secret_push_protection_available": string,
  "globally_allowed_ips": string,
  "allow_top_level_group_owners_to_create_service_accounts": string,
  "dependency_scanning_sbom_scan_api_upload_limit": string,
  "dependency_scanning_sbom_scan_api_download_limit": string,
  "disable_invite_members": string,
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "performance_bar_allowed_group_id": string,
  "abuse_notification_email": string,
  "admin_mode": string,
  "after_sign_out_path": string,
  "after_sign_up_text": string,
  "akismet_api_key": string,
  "akismet_enabled": string,
  "allow_local_requests_from_web_hooks_and_services": string,
  "allow_local_requests_from_system_hooks": string,
  "allow_possible_spam": string,
  "dns_rebinding_protection_enabled": string,
  "archive_builds_in_human_readable": string,
  "asset_proxy_enabled": string,
  "asset_proxy_url": string,
  "asset_proxy_allowlist": string,
  "static_objects_external_storage_auth_token": string,
  "static_objects_external_storage_url": string,
  "authn_data_retention_cleanup_enabled": string,
  "authorized_keys_enabled": string,
  "auto_devops_enabled": string,
  "auto_devops_domain": string,
  "autocomplete_users_limit": string,
  "autocomplete_users_unauthenticated_limit": string,
  "allow_bypass_placeholder_confirmation": string,
  "ci_delete_pipelines_in_seconds_limit_human_readable": string,
  "ci_job_live_trace_enabled": string,
  "ci_partitions_in_seconds_limit_human_readable": string,
  "concurrent_github_import_jobs_limit": string,
  "concurrent_bitbucket_import_jobs_limit": string,
  "concurrent_bitbucket_server_import_jobs_limit": string,
  "container_expiration_policies_enable_historic_entries": string,
  "container_registry_expiration_policies_caching": string,
  "container_registry_token_expire_delay": string,
  "oauth_access_token_expires_in": string,
  "decompress_archive_file_timeout": string,
  "default_artifacts_expire_in": string,
  "default_branch_name": string,
  "default_branch_protection": string,
  "default_branch_protection_defaults": string,
  "default_ci_config_path": string,
  "default_group_visibility": string,
  "default_preferred_language": string,
  "default_project_creation": string,
  "default_project_visibility": string,
  "default_projects_limit": string,
  "default_snippet_visibility": string,
  "default_syntax_highlighting_theme": string,
  "default_dark_syntax_highlighting_theme": string,
  "delete_inactive_projects": string,
  "deletion_adjourned_period": string,
  "deny_all_requests_except_allowed": string,
  "dependency_management_settings": string,
  "disable_admin_oauth_scopes": string,
  "disable_feed_token": string,
  "disable_password_authentication_for_users_with_sso_identities": string,
  "root_moved_permanently_redirection": string,
  "disabled_oauth_sign_in_sources": string,
  "domain_denylist": string,
  "domain_denylist_enabled": string,
  "domain_denylist_raw": string,
  "domain_allowlist": string,
  "domain_allowlist_raw": string,
  "outbound_local_requests_allowlist_raw": string,
  "outbound_local_requests_whitelist": string,
  "dsa_key_restriction": string,
  "ecdsa_key_restriction": string,
  "ecdsa_sk_key_restriction": string,
  "ed25519_key_restriction": string,
  "ed25519_sk_key_restriction": string,
  "eks_integration_enabled": string,
  "eks_account_id": string,
  "eks_access_key_id": string,
  "email_author_in_body": string,
  "email_confirmation_setting": string,
  "email_otp_enabled": string,
  "enabled_git_access_protocol": string,
  "enforce_ci_inbound_job_token_scope_enabled": string,
  "enforce_email_subaddress_restrictions": string,
  "require_email_verification_on_account_locked": string,
  "enforce_terms": string,
  "error_tracking_enabled": string,
  "error_tracking_api_url": string,
  "external_pipeline_validation_service_timeout": string,
  "external_pipeline_validation_service_token": string,
  "external_pipeline_validation_service_url": string,
  "failed_login_attempts_unlock_period_in_minutes": string,
  "first_day_of_week": string,
  "floc_enabled": string,
  "force_pages_access_control": string,
  "gitaly_timeout_default": string,
  "gitaly_timeout_medium": string,
  "gitaly_timeout_fast": string,
  "gitpod_enabled": string,
  "gitpod_url": string,
  "grafana_enabled": string,
  "grafana_url": string,
  "gravatar_enabled": string,
  "hashed_storage_enabled": string,
  "help_page_hide_commercial_content": string,
  "help_page_support_url": string,
  "help_page_documentation_base_url": string,
  "help_page_text": string,
  "hide_third_party_offers": string,
  "home_page_url": string,
  "housekeeping_enabled": string,
  "housekeeping_full_repack_period": string,
  "housekeeping_gc_period": string,
  "housekeeping_incremental_repack_period": string,
  "housekeeping_optimize_repository_period": string,
  "html_emails_enabled": string,
  "iframe_rendering_enabled": string,
  "iframe_rendering_allowlist": string,
  "iframe_rendering_allowlist_raw": string,
  "import_sources": string,
  "inactive_resource_access_tokens_delete_after_days": string,
  "inactive_projects_delete_after_months": string,
  "inactive_projects_min_size_mb": string,
  "inactive_projects_send_warning_email_after_months": string,
  "include_optional_metrics_in_service_ping": string,
  "invisible_captcha_enabled": string,
  "jira_connect_application_key": string,
  "jira_connect_public_key_storage_enabled": string,
  "jira_connect_proxy_url": string,
  "jira_connect_additional_audience_url": string,
  "jira_forge_app_id": string,
  "math_rendering_limits_enabled": string,
  "require_sha_for_merge": string,
  "lock_require_sha_for_merge": string,
  "max_artifacts_content_include_size": string,
  "max_artifacts_size": string,
  "max_attachment_size": string,
  "max_decompressed_archive_size": string,
  "max_export_size": string,
  "max_github_response_size_limit": string,
  "max_github_response_json_value_count": string,
  "max_http_decompressed_size": string,
  "max_http_response_size_limit": string,
  "max_http_response_json_depth": string,
  "max_http_response_json_structural_chars": string,
  "max_http_response_xml_structural_chars": string,
  "max_http_response_csv_structural_chars": string,
  "max_import_size": string,
  "max_import_remote_file_size": string,
  "max_login_attempts": string,
  "max_pages_size": string,
  "max_pages_custom_domains_per_project": string,
  "max_terraform_state_size_bytes": string,
  "max_yaml_size_bytes": string,
  "max_yaml_depth": string,
  "metrics_method_call_threshold": string,
  "minimum_password_length": string,
  "mirror_available": string,
  "notify_on_unknown_sign_in": string,
  "organization_cluster_agent_authorization_enabled": string,
  "pages_domain_verification_enabled": string,
  "pages_unique_domain_default_enabled": string,
  "password_authentication_enabled_for_web": string,
  "password_authentication_enabled_for_git": string,
  "personal_access_token_prefix": string,
  "instance_token_prefix": string,
  "kroki_enabled": string,
  "kroki_url": string,
  "kroki_formats": string,
  "kroki_diagram_proxy_enabled": string,
  "plantuml_enabled": string,
  "plantuml_url": string,
  "plantuml_diagram_proxy_enabled": string,
  "diagramsnet_enabled": string,
  "diagramsnet_url": string,
  "pages_extra_deployments_default_expiry_seconds": string,
  "polling_interval_multiplier": string,
  "project_export_enabled": string,
  "prometheus_metrics_enabled": string,
  "recaptcha_enabled": string,
  "recaptcha_private_key": string,
  "recaptcha_site_key": string,
  "login_recaptcha_protection_enabled": string,
  "receive_max_input_size": string,
  "repository_checks_enabled": string,
  "require_admin_approval_after_user_signup": string,
  "require_admin_two_factor_authentication": string,
  "require_two_factor_authentication": string,
  "remember_me_enabled": string,
  "restricted_visibility_levels": string,
  "rsa_key_restriction": string,
  "session_expire_delay": string,
  "session_expire_from_init": string,
  "shared_runners_enabled": string,
  "shared_runners_text": string,
  "sign_in_restrictions": string,
  "signup_enabled": string,
  "silent_mode_enabled": string,
  "slack_app_enabled": string,
  "slack_app_id": string,
  "slack_app_secret": string,
  "slack_app_signing_secret": string,
  "slack_app_verification_token": string,
  "sourcegraph_enabled": string,
  "sourcegraph_url": string,
  "sourcegraph_public_only": string,
  "spam_check_endpoint_enabled": string,
  "spam_check_endpoint_url": string,
  "spam_check_api_key": string,
  "terminal_max_session_time": string,
  "terms": string,
  "terraform_state_encryption_enabled": string,
  "throttle_authenticated_api_enabled": string,
  "throttle_authenticated_api_period_in_seconds": string,
  "throttle_authenticated_api_requests_per_period": string,
  "throttle_authenticated_git_http_enabled": string,
  "throttle_authenticated_git_http_period_in_seconds": string,
  "throttle_authenticated_git_http_requests_per_period": string,
  "throttle_authenticated_git_lfs_enabled": string,
  "throttle_authenticated_git_lfs_period_in_seconds": string,
  "throttle_authenticated_git_lfs_requests_per_period": string,
  "throttle_authenticated_web_enabled": string,
  "throttle_authenticated_web_period_in_seconds": string,
  "throttle_authenticated_web_requests_per_period": string,
  "throttle_authenticated_packages_api_enabled": string,
  "throttle_authenticated_packages_api_period_in_seconds": string,
  "throttle_authenticated_packages_api_requests_per_period": string,
  "throttle_authenticated_files_api_enabled": string,
  "throttle_authenticated_files_api_period_in_seconds": string,
  "throttle_authenticated_files_api_requests_per_period": string,
  "throttle_authenticated_deprecated_api_enabled": string,
  "throttle_authenticated_deprecated_api_period_in_seconds": string,
  "throttle_authenticated_deprecated_api_requests_per_period": string,
  "throttle_unauthenticated_api_enabled": string,
  "throttle_unauthenticated_api_period_in_seconds": string,
  "throttle_unauthenticated_api_requests_per_period": string,
  "throttle_unauthenticated_enabled": string,
  "throttle_unauthenticated_period_in_seconds": string,
  "throttle_unauthenticated_requests_per_period": string,
  "throttle_unauthenticated_packages_api_enabled": string,
  "throttle_unauthenticated_packages_api_period_in_seconds": string,
  "throttle_unauthenticated_packages_api_requests_per_period": string,
  "throttle_unauthenticated_files_api_enabled": string,
  "throttle_unauthenticated_files_api_period_in_seconds": string,
  "throttle_unauthenticated_files_api_requests_per_period": string,
  "throttle_unauthenticated_git_http_enabled": string,
  "throttle_unauthenticated_git_http_period_in_seconds": string,
  "throttle_unauthenticated_git_http_requests_per_period": string,
  "throttle_unauthenticated_deprecated_api_enabled": string,
  "throttle_unauthenticated_deprecated_api_period_in_seconds": string,
  "throttle_unauthenticated_deprecated_api_requests_per_period": string,
  "throttle_protected_paths_enabled": string,
  "throttle_protected_paths_period_in_seconds": string,
  "throttle_protected_paths_requests_per_period": string,
  "top_level_group_creation_enabled": string,
  "protected_paths_raw": string,
  "protected_paths_for_get_request_raw": string,
  "time_tracking_limit_to_hours": string,
  "two_factor_grace_period": string,
  "update_runner_versions_enabled": string,
  "unique_ips_limit_enabled": string,
  "unique_ips_limit_per_user": string,
  "unique_ips_limit_time_window": string,
  "usage_ping_enabled": string,
  "usage_ping_generation_enabled": string,
  "usage_ping_features_enabled": string,
  "use_clickhouse_for_analytics": string,
  "user_default_external": string,
  "user_show_add_ssh_key_message": string,
  "user_default_internal_regex": string,
  "user_oauth_applications": string,
  "version_check_enabled": string,
  "diff_max_patch_bytes": string,
  "diff_max_files": string,
  "diff_max_lines": string,
  "diff_max_versions": string,
  "diff_max_commits": string,
  "commit_email_hostname": string,
  "protected_ci_variables": string,
  "local_markdown_version": string,
  "mailgun_signing_key": string,
  "mailgun_events_enabled": string,
  "snowplow_collector_hostname": string,
  "snowplow_cookie_domain": string,
  "snowplow_database_collector_hostname": string,
  "snowplow_enabled": string,
  "snowplow_app_id": string,
  "gitlab_product_usage_data_enabled": string,
  "push_event_hooks_limit": string,
  "push_event_activities_limit": string,
  "custom_http_clone_url_root": string,
  "snippet_size_limit": string,
  "description_and_note_max_size": string,
  "email_restrictions_enabled": string,
  "email_restrictions": string,
  "issues_create_limit": string,
  "notes_create_limit": string,
  "notes_create_limit_allowlist_raw": string,
  "members_delete_limit": string,
  "raw_blob_request_limit": string,
  "raw_blob_request_limit_unauthenticated": string,
  "project_import_limit": string,
  "project_export_limit": string,
  "project_download_export_limit": string,
  "group_import_limit": string,
  "group_export_limit": string,
  "group_download_export_limit": string,
  "wiki_page_max_content_bytes": string,
  "wiki_asciidoc_allow_uri_includes": string,
  "container_registry_delete_tags_service_timeout": string,
  "rate_limiting_response_text": string,
  "package_registry_allow_anyone_to_pull_option": string,
  "package_registry_cleanup_policies_worker_capacity": string,
  "container_registry_expiration_policies_worker_capacity": string,
  "container_registry_cleanup_tags_service_max_list_size": string,
  "keep_latest_artifact": string,
  "whats_new_variant": string,
  "user_deactivation_emails_enabled": string,
  "resource_access_token_notify_inherited": string,
  "lock_resource_access_token_notify_inherited": string,
  "sentry_enabled": string,
  "sentry_dsn": string,
  "sentry_clientside_dsn": string,
  "sentry_environment": string,
  "sentry_clientside_traces_sample_rate": string,
  "sidekiq_job_limiter_mode": string,
  "sidekiq_job_limiter_compression_threshold_bytes": string,
  "sidekiq_job_limiter_limit_bytes": string,
  "suggest_pipeline_enabled": string,
  "enable_artifact_external_redirect_warning_page": string,
  "search_rate_limit": string,
  "search_rate_limit_unauthenticated": string,
  "search_rate_limit_allowlist_raw": string,
  "users_get_by_id_limit": string,
  "users_get_by_id_limit_allowlist_raw": string,
  "runner_token_expiration_interval": string,
  "group_runner_token_expiration_interval": string,
  "project_runner_token_expiration_interval": string,
  "pipeline_limit_per_project_user_sha": string,
  "pipeline_limit_per_user": string,
  "ci_lint_limit_per_user": string,
  "invitation_flow_enforcement": string,
  "can_create_group": string,
  "can_create_organization": string,
  "bulk_import_concurrent_pipeline_batch_limit": string,
  "concurrent_relation_batch_export_limit": string,
  "relation_export_batch_size": string,
  "bulk_import_enabled": string,
  "bulk_import_max_download_file_size": string,
  "silent_admin_exports_enabled": string,
  "allow_contribution_mapping_to_admins": string,
  "allow_s3_compatible_storage_for_offline_transfer": string,
  "allow_runner_registration_token": string,
  "valid_runner_registrars": string,
  "user_defaults_to_private_profile": string,
  "deactivation_email_additional_text": string,
  "projects_api_rate_limit_unauthenticated": string,
  "group_api_limit": string,
  "group_archive_unarchive_api_limit": string,
  "group_invited_groups_api_limit": string,
  "group_shared_groups_api_limit": string,
  "group_projects_api_limit": string,
  "groups_api_limit": string,
  "project_api_limit": string,
  "project_invited_groups_api_limit": string,
  "projects_api_limit": string,
  "project_members_api_limit": string,
  "create_organization_api_limit": string,
  "user_contributed_projects_api_limit": string,
  "user_projects_api_limit": string,
  "user_starred_projects_api_limit": string,
  "users_api_limit_followers": string,
  "users_api_limit_following": string,
  "users_api_limit_status": string,
  "users_api_limit_ssh_keys": string,
  "users_api_limit_ssh_key": string,
  "users_api_limit_gpg_keys": string,
  "users_api_limit_gpg_key": string,
  "gitlab_dedicated_instance": string,
  "gitlab_environment_toolkit_instance": string,
  "ci_max_includes": string,
  "ci_max_caches_per_job": string,
  "allow_account_deletion": string,
  "gitlab_shell_operation_limit": string,
  "namespace_aggregation_schedule_lease_duration_in_seconds": string,
  "ci_max_total_yaml_size_bytes": string,
  "project_jobs_api_rate_limit": string,
  "security_txt_content": string,
  "allow_project_creation_for_guest_and_below": string,
  "downstream_pipeline_trigger_limit_per_project_user_sha": string,
  "asciidoc_max_includes": string,
  "ai_action_api_rate_limit": string,
  "code_suggestions_api_rate_limit": string,
  "require_personal_access_token_expiry": string,
  "observability_backend_ssl_verification_enabled": string,
  "show_migrate_from_jenkins_banner": string,
  "global_search_snippet_titles_enabled": string,
  "global_search_users_enabled": string,
  "global_search_work_items_enabled": string,
  "global_search_merge_requests_enabled": string,
  "global_search_block_anonymous_searches_enabled": string,
  "enable_language_server_restrictions": string,
  "minimum_language_server_version": string,
  "vscode_extension_marketplace": string,
  "vscode_extension_marketplace_enabled": string,
  "vscode_extension_marketplace_extension_host_domain": string,
  "vscode_extension_marketplace_single_origin_fallback_enabled": string,
  "reindexing_minimum_index_size": string,
  "reindexing_minimum_relative_bloat_size": string,
  "anonymous_searches_allowed": string,
  "default_search_scope": string,
  "git_push_pipeline_limit": string,
  "delay_user_account_self_deletion": string,
  "resource_usage_limits": string,
  "runner_jobs_request_api_limit": string,
  "runner_jobs_patch_trace_api_limit": string,
  "runner_jobs_endpoints_api_limit": string,
  "background_operations_max_jobs": string,
  "enforce_granular_tokens": string,
  "granular_tokens_enforced_after": string,
  "logging_field_schema_version": integer,
  "logging_field_dual_emit_target": integer,
  "deactivate_dormant_users": string,
  "deactivate_dormant_users_period": string,
  "nuget_skip_metadata_url_validation": string,
  "helm_max_packages_count": string,
  "mcp_server_enabled": string,
  "active_context_pause_indexing": string,
  "allow_all_integrations": string,
  "allowed_integrations": string,
  "allow_group_owners_to_manage_ldap": string,
  "automatic_purchased_storage_allocation": string,
  "check_namespace_plan": string,
  "ci_cd_catalog_projects_allowlist": string,
  "ci_cd_catalog_projects_allowlist_raw": string,
  "duo_chat_expiration_column": string,
  "duo_chat_expiration_days": string,
  "elasticsearch_aws_access_key": string,
  "elasticsearch_aws_region": string,
  "elasticsearch_aws_role_arn": string,
  "elasticsearch_aws_secret_access_key": string,
  "elasticsearch_aws": string,
  "elasticsearch_client_adapter": string,
  "elasticsearch_client_request_timeout": string,
  "elasticsearch_indexed_field_length_limit": string,
  "elasticsearch_indexed_file_size_limit_kb": string,
  "elasticsearch_indexing_timeout_minutes": string,
  "elasticsearch_indexing": string,
  "elasticsearch_requeue_workers": string,
  "elasticsearch_limit_indexing": string,
  "elasticsearch_worker_number_of_shards": string,
  "elasticsearch_max_bulk_concurrency": string,
  "elasticsearch_max_bulk_size_mb": string,
  "elasticsearch_max_code_indexing_concurrency": string,
  "elasticsearch_namespace_ids": string,
  "elasticsearch_pause_indexing": string,
  "elasticsearch_advanced_search_pause_indexing": string,
  "elasticsearch_project_ids": string,
  "elasticsearch_retry_on_failure": string,
  "elasticsearch_replicas": string,
  "elasticsearch_search": string,
  "elasticsearch_shards": string,
  "elasticsearch_url": string,
  "elasticsearch_username": string,
  "elasticsearch_password": string,
  "elasticsearch_analyzers_smartcn_enabled": string,
  "elasticsearch_analyzers_smartcn_search": string,
  "elasticsearch_analyzers_kuromoji_enabled": string,
  "elasticsearch_analyzers_kuromoji_search": string,
  "elasticsearch_code_scope": string,
  "enforce_namespace_storage_limit": string,
  "geo_node_allowed_ips": string,
  "geo_status_timeout": string,
  "instance_level_ai_beta_features_enabled": string,
  "lock_memberships_to_ldap": string,
  "lock_memberships_to_saml": string,
  "lock_model_prompt_cache_enabled": string,
  "max_personal_access_token_lifetime": string,
  "max_ssh_key_lifetime": string,
  "model_prompt_cache_enabled": string,
  "receptive_cluster_agents_enabled": string,
  "repository_size_limit": string,
  "search_max_shard_size_gb": string,
  "search_max_docs_denominator": string,
  "search_min_docs_before_rollover": string,
  "secret_detection_token_revocation_enabled": string,
  "secret_detection_token_revocation_url": string,
  "secret_detection_token_revocation_token": string,
  "secret_detection_revocation_token_types_url": string,
  "shared_runners_minutes": string,
  "throttle_incident_management_notification_enabled": string,
  "throttle_incident_management_notification_per_period": string,
  "throttle_incident_management_notification_period_in_seconds": string,
  "package_metadata_purl_types": string,
  "product_analytics_enabled": string,
  "product_analytics_data_collector_host": string,
  "product_analytics_configurator_connection_string": string,
  "cube_api_base_url": string,
  "cube_api_key": string,
  "security_policy_global_group_approvers_enabled": string,
  "security_approval_policies_limit": string,
  "duo_features_enabled": string,
  "lock_duo_features_enabled": string,
  "duo_availability": string,
  "duo_agent_platform_enabled": string,
  "duo_cli_enabled": string,
  "ai_audit_events_streaming_enabled": boolean,
  "duo_namespace_access_rules": string,
  "duo_remote_flows_enabled": string,
  "duo_remote_flows_availability": string,
  "duo_foundational_flows_enabled": string,
  "duo_foundational_flows_availability": string,
  "duo_custom_agents_enabled": boolean,
  "duo_custom_agents_availability": string,
  "duo_custom_flows_enabled": boolean,
  "duo_custom_flows_availability": string,
  "duo_external_agents_enabled": boolean,
  "duo_external_agents_availability": string,
  "tool_approval_for_session_enabled": string,
  "tool_approval_for_session_availability": string,
  "enabled_expanded_logging": string,
  "foundational_agents_default_enabled": string,
  "foundational_agents_statuses": string,
  "zoekt_indexing_enabled": string,
  "zoekt_search_enabled": string,
  "zoekt_indexing_paused": string,
  "zoekt_auto_index_root_namespace": string,
  "zoekt_cache_response": string,
  "zoekt_cpu_to_tasks_ratio": string,
  "zoekt_force_reindexing_percentage": string,
  "zoekt_indexing_parallelism": string,
  "zoekt_rollout_batch_size": string,
  "zoekt_lost_node_threshold": string,
  "zoekt_indexing_timeout": string,
  "zoekt_maximum_files": string,
  "zoekt_indexed_file_size_limit": string,
  "zoekt_trigram_max": string,
  "zoekt_rollout_retry_interval": string,
  "zoekt_default_number_of_replicas": string,
  "zoekt_max_projects_for_legacy_search": string,
  "zoekt_max_restarts_15m": string,
  "duo_workflow_oauth_application_id": string,
  "scan_execution_policies_action_limit": string,
  "scan_execution_policies_schedule_limit": string,
  "pipeline_execution_policies_per_configuration_limit": string,
  "scan_execution_policies_per_configuration_limit": string,
  "vulnerability_management_policies_per_configuration_limit": string,
  "dependency_firewall_policies_per_configuration_limit": string,
  "secret_detection_service_auth_token": string,
  "secret_detection_service_url": string,
  "fetch_observability_alerts_from_cloud": string,
  "global_search_code_enabled": string,
  "global_search_commits_enabled": string,
  "global_search_wiki_enabled": string,
  "global_search_limited_indexing_enabled": string,
  "elastic_migration_worker_enabled": string,
  "enforce_pipl_compliance": string,
  "display_gitlab_credits_user_data": string,
  "project_secrets_limit": string,
  "group_secrets_limit": string,
  "security_mr_report_cache_lifetime_minutes": string,
  "security_scan_stale_after_days": string,
  "vac_project_ids_raw": string,
  "enable_member_promotion_management": string,
  "external_auth_client_cert": string,
  "external_auth_client_key": string,
  "external_auth_client_key_pass": string,
  "external_authorization_service_default_label": string,
  "external_authorization_service_enabled": string,
  "external_authorization_service_timeout": string,
  "external_authorization_service_url": string,
  "allow_deploy_tokens_and_keys_with_external_authn": string,
  "throttle_unauthenticated_web_enabled": string,
  "throttle_unauthenticated_web_period_in_seconds": string,
  "throttle_unauthenticated_web_requests_per_period": string,
  "password_authentication_enabled": string,
  "signin_enabled": string,
  "allow_local_requests_from_hooks_and_services": string,
  "asset_proxy_whitelist": string,
  "housekeeping_bitmaps_enabled": string,
  "repository_storages_weighted": string,
  "gitlab_product_usage_data_source": string,
  "container_registry_import_max_tags_count": string,
  "container_registry_import_max_retries": string,
  "container_registry_import_start_max_retries": string,
  "container_registry_import_max_step_duration": string,
  "container_registry_pre_import_tags_rate": string,
  "container_registry_pre_import_timeout": string,
  "container_registry_import_timeout": string,
  "container_registry_import_target_plan": string,
  "container_registry_import_created_before": string,
  "mirror_max_capacity": string,
  "mirror_max_delay": string,
  "mirror_capacity_threshold": string,
  "disable_overriding_approvers_per_merge_request": string,
  "prevent_merge_requests_author_approval": string,
  "prevent_merge_requests_committers_approval": string,
  "password_number_required": string,
  "password_symbol_required": string,
  "password_uppercase_required": string,
  "password_lowercase_required": string,
  "email_additional_text": string,
  "file_template_project_id": string,
  "default_project_deletion_protection": string,
  "disable_personal_access_tokens": string,
  "updating_name_disabled_for_users": string,
  "maven_package_requests_forwarding": string,
  "npm_package_requests_forwarding": string,
  "virtual_registries_endpoints_api_limit": string,
  "dependency_scanning_sbom_scan_api_upload_limit": string,
  "dependency_scanning_sbom_scan_api_download_limit": string,
  "secret_push_protection_available": string,
  "pre_receive_secret_detection_enabled": string,
  "pypi_package_requests_forwarding": string,
  "group_owners_can_manage_default_branch_protection": string,
  "maintenance_mode": string,
  "maintenance_mode_message": string,
  "service_access_tokens_expiration_enforced": string,
  "git_two_factor_session_expiry": string,
  "max_number_of_repository_downloads": string,
  "max_number_of_repository_downloads_within_time_period": string,
  "git_rate_limit_users_allowlist": string,
  "git_rate_limit_users_alertlist": string,
  "auto_ban_user_on_excessive_projects_download": string,
  "delete_unconfirmed_users": string,
  "unconfirmed_users_delete_after_days": string,
  "make_profile_private": string,
  "lock_duo_custom_agents_enabled": boolean,
  "lock_duo_custom_flows_enabled": boolean,
  "lock_duo_external_agents_enabled": boolean,
  "duo_workflows_default_image_registry": string,
  "duo_template_project_id": string,
  "ci_telemetry_otel_endpoint": string,
  "ci_job_telemetry_sampling_rate": string,
  "disabled_direct_code_suggestions": string,
  "allow_top_level_group_owners_to_create_service_accounts": string,
  "auto_duo_code_review_enabled": string,
  "elasticsearch_index_settings": [
    {
      "alias_name": string, // Name of the Elasticsearch index alias.
      "number_of_shards": integer, // Number of shards for the Elasticsearch index.
      "number_of_replicas": integer, // Number of replicas for the Elasticsearch index.
    }
  ], // Elasticsearch index settings.
  "built_in_project_templates_enabled": boolean,
  "lock_built_in_project_templates_enabled": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

