# 20-Posts the current node status to the primary site [POST]

`POST /api/v4/geo/status`

Posts the current node status to the primary site

### Request Body (application/json)

```json
{
  "data": {
    "geo_node_id": integer (required), // Geo Node ID to look up its status
    "db_replication_lag_seconds": integer, // DB replication lag in seconds
    "last_event_id": integer, // Last event ID
    "last_event_date": string, // Last event date
    "cursor_last_event_id": integer, // Cursor last event ID
    "cursor_last_event_date": string, // Cursor last event date
    "last_successful_status_check_at": string, // Last successful status check date
    "status_message": string, // Status message
    "replication_slots_count": integer, // Replication slots count
    "replication_slots_used_count": integer, // Replication slots used count
    "replication_slots_max_retained_wal_bytes": integer, // Maximum number of bytes retained in the WAL on the primary
    "version": string, // Gitlab version
    "revision": string, // Gitlab revision
    "status": {
      "projects_count": integer, // Projects count
      "container_repositories_replication_enabled": boolean, // Container repositories replication enabled
      "lfs_objects_count": integer, // LFS objects count
      "lfs_objects_checksum_total_count": integer, // LFS objects checksum total count
      "lfs_objects_checksummed_count": integer, // LFS objects checksummed count
      "lfs_objects_checksum_failed_count": integer, // LFS objects checksum failed count
      "lfs_objects_synced_count": integer, // LFS objects synced count
      "lfs_objects_failed_count": integer, // LFS objects failed count
      "lfs_objects_registry_count": integer, // LFS objects registry count
      "lfs_objects_verification_total_count": integer, // LFS objects verification total count
      "lfs_objects_verified_count": integer, // LFS objects verified count
      "lfs_objects_verification_failed_count": integer, // LFS objects verification failed count
      "merge_request_diffs_count": integer, // Merge request diffs count
      "merge_request_diffs_checksum_total_count": integer, // Merge request diffs checksum total count
      "merge_request_diffs_checksummed_count": integer, // Merge request diffs checksummed count
      "merge_request_diffs_checksum_failed_count": integer, // Merge request diffs checksum failed count
      "merge_request_diffs_synced_count": integer, // Merge request diffs synced count
      "merge_request_diffs_failed_count": integer, // Merge request diffs failed count
      "merge_request_diffs_registry_count": integer, // Merge request diffs registry count
      "merge_request_diffs_verification_total_count": integer, // Merge request diffs verification total count
      "merge_request_diffs_verified_count": integer, // Merge request diffs verified count
      "merge_request_diffs_verification_failed_count": integer, // Merge request diffs verified count
      "package_files_count": integer, // Packages files count
      "package_files_checksum_total_count": integer, // Packages files checksum total count
      "package_files_checksummed_count": integer, // Packages files checksummed count
      "package_files_checksum_failed_count": integer, // Packages files checksum failed count
      "package_files_synced_count": integer, // Packages files synced count
      "package_files_failed_count": integer, // Packages files failed count
      "package_files_registry_count": integer, // Packages files registry count
      "package_files_verification_total_count": integer, // Packages files verification total count
      "package_files_verified_count": integer, // Packages files verified count
      "package_files_verification_failed_count": integer, // Packages files verification failed count
      "packages_nuget_symbols_count": integer, // NuGet symbols count
      "packages_nuget_symbols_checksum_total_count": integer, // NuGet symbols checksum total count
      "packages_nuget_symbols_checksummed_count": integer, // NuGet symbols checksummed count
      "packages_nuget_symbols_checksum_failed_count": integer, // NuGet symbols checksum failed count
      "packages_nuget_symbols_synced_count": integer, // NuGet symbols synced count
      "packages_nuget_symbols_failed_count": integer, // NuGet symbols failed count
      "packages_nuget_symbols_registry_count": integer, // NuGet symbols registry count
      "packages_nuget_symbols_verification_total_count": integer, // NuGet symbols verification total count
      "packages_nuget_symbols_verified_count": integer, // NuGet symbols verified count
      "packages_nuget_symbols_verification_failed_count": integer, // NuGet symbols verification failed count
      "terraform_state_versions_count": integer, // Terraform state versions count
      "terraform_state_versions_checksum_total_count": integer, // Terraform state versions checksum total count
      "terraform_state_versions_checksummed_count": integer, // Terraform state versions checksummed count
      "terraform_state_versions_checksum_failed_count": integer, // Terraform state versions checksum failed count
      "terraform_state_versions_synced_count": integer, // Terraform state versions synced count
      "terraform_state_versions_failed_count": integer, // Terraform state versions failed count
      "terraform_state_versions_registry_count": integer, // Terraform state versions registry count
      "terraform_state_versions_verification_total_count": integer, // Terraform state versions verification total count
      "terraform_state_versions_verified_count": integer, // Terraform state versions verified count
      "terraform_state_versions_verification_failed_count": integer, // Terraform state versions verification failed count
      "snippet_repositories_count": integer, // Snippet repositories count
      "snippet_repositories_checksum_total_count": integer, // Snippet repositories checksum total count
      "snippet_repositories_checksummed_count": integer, // Snippet repositories checksummed count
      "snippet_repositories_checksum_failed_count": integer, // Snippet repositories checksum failed count
      "snippet_repositories_synced_count": integer, // Snippet repositories synced count
      "snippet_repositories_failed_count": integer, // Snippet repositories failed count
      "snippet_repositories_registry_count": integer, // Snippet repositories registry count
      "snippet_repositories_verification_total_count": integer, // Snippet repositories verification total count
      "snippet_repositories_verified_count": integer, // Snippet repositories verified count
      "snippet_repositories_verification_failed_count": integer, // Snippet repositories verification failed count
      "group_wiki_repositories_count": integer, // Group wiki repositories count
      "group_wiki_repositories_checksum_total_count": integer, // Group wiki repositories checksum total count
      "group_wiki_repositories_checksummed_count": integer, // Group wiki repositories checksummed count
      "group_wiki_repositories_checksum_failed_count": integer, // Group wiki repositories checksum failed count
      "group_wiki_repositories_synced_count": integer, // Group wiki repositories synced count
      "group_wiki_repositories_failed_count": integer, // Group wiki repositories failed count
      "group_wiki_repositories_registry_count": integer, // Group wiki repositories registry count
      "group_wiki_repositories_verification_total_count": integer, // Group wiki repositories verification total count
      "group_wiki_repositories_verified_count": integer, // Group wiki repositories verified count
      "group_wiki_repositories_verification_failed_count": integer, // Group wiki repositories verification failed count
      "pipeline_artifacts_count": integer, // Pipeline artifacts count
      "pipeline_artifacts_checksum_total_count": integer, // Pipeline artifacts checksum total count
      "pipeline_artifacts_checksummed_count": integer, // Pipeline artifacts checksummed count
      "pipeline_artifacts_checksum_failed_count": integer, // Pipeline artifacts checksum failed count
      "pipeline_artifacts_synced_count": integer, // Pipeline artifacts synced count
      "pipeline_artifacts_failed_count": integer, // Pipeline artifacts failed count
      "pipeline_artifacts_registry_count": integer, // Pipeline artifacts registry count
      "pipeline_artifacts_verification_total_count": integer, // Pipeline artifacts verification total count
      "pipeline_artifacts_verified_count": integer, // Pipeline artifacts verified count
      "pipeline_artifacts_verification_failed_count": integer, // Pipeline artifacts verification failed count
      "pages_deployments_count": integer, // Pages deployments count
      "pages_deployments_checksum_total_count": integer, // Pages deployments checksum total count
      "pages_deployments_checksummed_count": integer, // Pages deployments checksummed count
      "pages_deployments_checksum_failed_count": integer, // Pages deployments checksum failed count
      "pages_deployments_synced_count": integer, // Pages deployments synced count
      "pages_deployments_failed_count": integer, // Pages deployments failed count
      "pages_deployments_registry_count": integer, // Pages deployments registry count
      "pages_deployments_verification_total_count": integer, // Pages deployments verification total count
      "pages_deployments_verified_count": integer, // Pages deployments verified count
      "pages_deployments_verification_failed_count": integer, // Pages deployments verification failed count
      "uploads_count": integer, // Uploads count
      "uploads_checksum_total_count": integer, // Uploads checksum total count
      "uploads_checksummed_count": integer, // Uploads checksummed count
      "uploads_checksum_failed_count": integer, // Uploads checksum failed count
      "uploads_synced_count": integer, // Uploads synced count
      "uploads_failed_count": integer, // Uploads failed count
      "uploads_registry_count": integer, // Uploads registry count
      "uploads_verification_total_count": integer, // Uploads verification total count
      "uploads_verified_count": integer, // Uploads verified count
      "uploads_verification_failed_count": integer, // Uploads verification failed count
      "job_artifacts_count": integer, // Job artifacts count
      "job_artifacts_checksum_total_count": integer, // Job artifacts checksum total count
      "job_artifacts_checksummed_count": integer, // Job artifacts checksummed count
      "job_artifacts_checksum_failed_count": integer, // Job artifacts checksum failed count
      "job_artifacts_synced_count": integer, // Job artifacts synced count
      "job_artifacts_failed_count": integer, // Job artifacts failed count
      "job_artifacts_registry_count": integer, // Job artifacts registry count
      "job_artifacts_verification_total_count": integer, // Job artifacts verification total count
      "job_artifacts_verified_count": integer, // Job artifacts verified count
      "job_artifacts_verification_failed_count": integer, // Job artifacts verification failed count
      "ci_secure_files_count": integer, // CI secure files count
      "ci_secure_files_checksum_total_count": integer, // CI secure files checksum total count
      "ci_secure_files_checksummed_count": integer, // CI secure files checksummed count
      "ci_secure_files_checksum_failed_count": integer, // CI secure files checksum failed count
      "ci_secure_files_synced_count": integer, // CI secure files synced count
      "ci_secure_files_failed_count": integer, // CI secure files failed count
      "ci_secure_files_registry_count": integer, // CI secure files registry count
      "ci_secure_files_verification_total_count": integer, // CI secure files verification total count
      "ci_secure_files_verified_count": integer, // CI secure files verified count
      "ci_secure_files_verification_failed_count": integer, // CI secure files verification failed count
      "container_repositories_count": integer, // Container repositories count
      "container_repositories_checksum_total_count": integer, // Container repositories checksum total count
      "container_repositories_checksummed_count": integer, // Container repositories checksummed count
      "container_repositories_checksum_failed_count": integer, // Container repositories checksum failed count
      "container_repositories_synced_count": integer, // Container repositories synced count
      "container_repositories_failed_count": integer, // Container repositories failed count
      "container_repositories_registry_count": integer, // Container repositories registry count
      "container_repositories_verification_total_count": integer, // Container repositories verification total count
      "container_repositories_verified_count": integer, // Container repositories verified count
      "container_repositories_verification_failed_count": integer, // Container repositories verification failed count
      "git_fetch_event_count_weekly": integer, // Git fetch event count weekly
      "git_push_event_count_weekly": integer, // Git push event count weekly
      "proxy_remote_requests_event_count_weekly": integer, // Proxy remote requests event count weekly
      "proxy_local_requests_event_count_weekly": integer, // Proxy local requests event count weekly
    }, // Object that contains information on replication and verification                 status metrics for GitLab resources on Geo nodes
  }, // Object that contains status information               and replication metrics for the Geo node
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "geo_node_id": string,
  "projects_count": string,
  "container_repositories_replication_enabled": string,
  "abuse_report_uploads_count": string,
  "abuse_report_uploads_checksum_total_count": string,
  "abuse_report_uploads_checksummed_count": string,
  "abuse_report_uploads_checksum_failed_count": string,
  "abuse_report_uploads_synced_count": string,
  "abuse_report_uploads_failed_count": string,
  "abuse_report_uploads_registry_count": string,
  "abuse_report_uploads_verification_total_count": string,
  "abuse_report_uploads_verified_count": string,
  "abuse_report_uploads_verification_failed_count": string,
  "abuse_report_uploads_oldest_unsynced_time": string,
  "achievement_uploads_count": string,
  "achievement_uploads_checksum_total_count": string,
  "achievement_uploads_checksummed_count": string,
  "achievement_uploads_checksum_failed_count": string,
  "achievement_uploads_synced_count": string,
  "achievement_uploads_failed_count": string,
  "achievement_uploads_registry_count": string,
  "achievement_uploads_verification_total_count": string,
  "achievement_uploads_verified_count": string,
  "achievement_uploads_verification_failed_count": string,
  "achievement_uploads_oldest_unsynced_time": string,
  "ai_vectorizable_file_uploads_count": string,
  "ai_vectorizable_file_uploads_checksum_total_count": string,
  "ai_vectorizable_file_uploads_checksummed_count": string,
  "ai_vectorizable_file_uploads_checksum_failed_count": string,
  "ai_vectorizable_file_uploads_synced_count": string,
  "ai_vectorizable_file_uploads_failed_count": string,
  "ai_vectorizable_file_uploads_registry_count": string,
  "ai_vectorizable_file_uploads_verification_total_count": string,
  "ai_vectorizable_file_uploads_verified_count": string,
  "ai_vectorizable_file_uploads_verification_failed_count": string,
  "ai_vectorizable_file_uploads_oldest_unsynced_time": string,
  "alert_management_metric_image_uploads_count": string,
  "alert_management_metric_image_uploads_checksum_total_count": string,
  "alert_management_metric_image_uploads_checksummed_count": string,
  "alert_management_metric_image_uploads_checksum_failed_count": string,
  "alert_management_metric_image_uploads_synced_count": string,
  "alert_management_metric_image_uploads_failed_count": string,
  "alert_management_metric_image_uploads_registry_count": string,
  "alert_management_metric_image_uploads_verification_total_count": string,
  "alert_management_metric_image_uploads_verified_count": string,
  "alert_management_metric_image_uploads_verification_failed_count": string,
  "alert_management_metric_image_uploads_oldest_unsynced_time": string,
  "appearance_uploads_count": string,
  "appearance_uploads_checksum_total_count": string,
  "appearance_uploads_checksummed_count": string,
  "appearance_uploads_checksum_failed_count": string,
  "appearance_uploads_synced_count": string,
  "appearance_uploads_failed_count": string,
  "appearance_uploads_registry_count": string,
  "appearance_uploads_verification_total_count": string,
  "appearance_uploads_verified_count": string,
  "appearance_uploads_verification_failed_count": string,
  "appearance_uploads_oldest_unsynced_time": string,
  "bulk_import_export_upload_uploads_count": string,
  "bulk_import_export_upload_uploads_checksum_total_count": string,
  "bulk_import_export_upload_uploads_checksummed_count": string,
  "bulk_import_export_upload_uploads_checksum_failed_count": string,
  "bulk_import_export_upload_uploads_synced_count": string,
  "bulk_import_export_upload_uploads_failed_count": string,
  "bulk_import_export_upload_uploads_registry_count": string,
  "bulk_import_export_upload_uploads_verification_total_count": string,
  "bulk_import_export_upload_uploads_verified_count": string,
  "bulk_import_export_upload_uploads_verification_failed_count": string,
  "bulk_import_export_upload_uploads_oldest_unsynced_time": string,
  "ci_secure_files_count": string,
  "ci_secure_files_checksum_total_count": string,
  "ci_secure_files_checksummed_count": string,
  "ci_secure_files_checksum_failed_count": string,
  "ci_secure_files_synced_count": string,
  "ci_secure_files_failed_count": string,
  "ci_secure_files_registry_count": string,
  "ci_secure_files_verification_total_count": string,
  "ci_secure_files_verified_count": string,
  "ci_secure_files_verification_failed_count": string,
  "ci_secure_files_oldest_unsynced_time": string,
  "container_repositories_count": string,
  "container_repositories_checksum_total_count": string,
  "container_repositories_checksummed_count": string,
  "container_repositories_checksum_failed_count": string,
  "container_repositories_synced_count": string,
  "container_repositories_failed_count": string,
  "container_repositories_registry_count": string,
  "container_repositories_verification_total_count": string,
  "container_repositories_verified_count": string,
  "container_repositories_verification_failed_count": string,
  "container_repositories_oldest_unsynced_time": string,
  "dependency_list_export_part_uploads_count": string,
  "dependency_list_export_part_uploads_checksum_total_count": string,
  "dependency_list_export_part_uploads_checksummed_count": string,
  "dependency_list_export_part_uploads_checksum_failed_count": string,
  "dependency_list_export_part_uploads_synced_count": string,
  "dependency_list_export_part_uploads_failed_count": string,
  "dependency_list_export_part_uploads_registry_count": string,
  "dependency_list_export_part_uploads_verification_total_count": string,
  "dependency_list_export_part_uploads_verified_count": string,
  "dependency_list_export_part_uploads_verification_failed_count": string,
  "dependency_list_export_part_uploads_oldest_unsynced_time": string,
  "dependency_list_export_uploads_count": string,
  "dependency_list_export_uploads_checksum_total_count": string,
  "dependency_list_export_uploads_checksummed_count": string,
  "dependency_list_export_uploads_checksum_failed_count": string,
  "dependency_list_export_uploads_synced_count": string,
  "dependency_list_export_uploads_failed_count": string,
  "dependency_list_export_uploads_registry_count": string,
  "dependency_list_export_uploads_verification_total_count": string,
  "dependency_list_export_uploads_verified_count": string,
  "dependency_list_export_uploads_verification_failed_count": string,
  "dependency_list_export_uploads_oldest_unsynced_time": string,
  "dependency_proxy_blobs_count": string,
  "dependency_proxy_blobs_checksum_total_count": string,
  "dependency_proxy_blobs_checksummed_count": string,
  "dependency_proxy_blobs_checksum_failed_count": string,
  "dependency_proxy_blobs_synced_count": string,
  "dependency_proxy_blobs_failed_count": string,
  "dependency_proxy_blobs_registry_count": string,
  "dependency_proxy_blobs_verification_total_count": string,
  "dependency_proxy_blobs_verified_count": string,
  "dependency_proxy_blobs_verification_failed_count": string,
  "dependency_proxy_blobs_oldest_unsynced_time": string,
  "dependency_proxy_manifests_count": string,
  "dependency_proxy_manifests_checksum_total_count": string,
  "dependency_proxy_manifests_checksummed_count": string,
  "dependency_proxy_manifests_checksum_failed_count": string,
  "dependency_proxy_manifests_synced_count": string,
  "dependency_proxy_manifests_failed_count": string,
  "dependency_proxy_manifests_registry_count": string,
  "dependency_proxy_manifests_verification_total_count": string,
  "dependency_proxy_manifests_verified_count": string,
  "dependency_proxy_manifests_verification_failed_count": string,
  "dependency_proxy_manifests_oldest_unsynced_time": string,
  "design_management_action_uploads_count": string,
  "design_management_action_uploads_checksum_total_count": string,
  "design_management_action_uploads_checksummed_count": string,
  "design_management_action_uploads_checksum_failed_count": string,
  "design_management_action_uploads_synced_count": string,
  "design_management_action_uploads_failed_count": string,
  "design_management_action_uploads_registry_count": string,
  "design_management_action_uploads_verification_total_count": string,
  "design_management_action_uploads_verified_count": string,
  "design_management_action_uploads_verification_failed_count": string,
  "design_management_action_uploads_oldest_unsynced_time": string,
  "design_management_repositories_count": string,
  "design_management_repositories_checksum_total_count": string,
  "design_management_repositories_checksummed_count": string,
  "design_management_repositories_checksum_failed_count": string,
  "design_management_repositories_synced_count": string,
  "design_management_repositories_failed_count": string,
  "design_management_repositories_registry_count": string,
  "design_management_repositories_verification_total_count": string,
  "design_management_repositories_verified_count": string,
  "design_management_repositories_verification_failed_count": string,
  "design_management_repositories_oldest_unsynced_time": string,
  "group_uploads_count": string,
  "group_uploads_checksum_total_count": string,
  "group_uploads_checksummed_count": string,
  "group_uploads_checksum_failed_count": string,
  "group_uploads_synced_count": string,
  "group_uploads_failed_count": string,
  "group_uploads_registry_count": string,
  "group_uploads_verification_total_count": string,
  "group_uploads_verified_count": string,
  "group_uploads_verification_failed_count": string,
  "group_uploads_oldest_unsynced_time": string,
  "group_wiki_repositories_count": string,
  "group_wiki_repositories_checksum_total_count": string,
  "group_wiki_repositories_checksummed_count": string,
  "group_wiki_repositories_checksum_failed_count": string,
  "group_wiki_repositories_synced_count": string,
  "group_wiki_repositories_failed_count": string,
  "group_wiki_repositories_registry_count": string,
  "group_wiki_repositories_verification_total_count": string,
  "group_wiki_repositories_verified_count": string,
  "group_wiki_repositories_verification_failed_count": string,
  "group_wiki_repositories_oldest_unsynced_time": string,
  "import_export_upload_uploads_count": string,
  "import_export_upload_uploads_checksum_total_count": string,
  "import_export_upload_uploads_checksummed_count": string,
  "import_export_upload_uploads_checksum_failed_count": string,
  "import_export_upload_uploads_synced_count": string,
  "import_export_upload_uploads_failed_count": string,
  "import_export_upload_uploads_registry_count": string,
  "import_export_upload_uploads_verification_total_count": string,
  "import_export_upload_uploads_verified_count": string,
  "import_export_upload_uploads_verification_failed_count": string,
  "import_export_upload_uploads_oldest_unsynced_time": string,
  "issuable_metric_image_uploads_count": string,
  "issuable_metric_image_uploads_checksum_total_count": string,
  "issuable_metric_image_uploads_checksummed_count": string,
  "issuable_metric_image_uploads_checksum_failed_count": string,
  "issuable_metric_image_uploads_synced_count": string,
  "issuable_metric_image_uploads_failed_count": string,
  "issuable_metric_image_uploads_registry_count": string,
  "issuable_metric_image_uploads_verification_total_count": string,
  "issuable_metric_image_uploads_verified_count": string,
  "issuable_metric_image_uploads_verification_failed_count": string,
  "issuable_metric_image_uploads_oldest_unsynced_time": string,
  "job_artifacts_count": string,
  "job_artifacts_checksum_total_count": string,
  "job_artifacts_checksummed_count": string,
  "job_artifacts_checksum_failed_count": string,
  "job_artifacts_synced_count": string,
  "job_artifacts_failed_count": string,
  "job_artifacts_registry_count": string,
  "job_artifacts_verification_total_count": string,
  "job_artifacts_verified_count": string,
  "job_artifacts_verification_failed_count": string,
  "job_artifacts_oldest_unsynced_time": string,
  "lfs_objects_count": string,
  "lfs_objects_checksum_total_count": string,
  "lfs_objects_checksummed_count": string,
  "lfs_objects_checksum_failed_count": string,
  "lfs_objects_synced_count": string,
  "lfs_objects_failed_count": string,
  "lfs_objects_registry_count": string,
  "lfs_objects_verification_total_count": string,
  "lfs_objects_verified_count": string,
  "lfs_objects_verification_failed_count": string,
  "lfs_objects_oldest_unsynced_time": string,
  "merge_request_diffs_count": string,
  "merge_request_diffs_checksum_total_count": string,
  "merge_request_diffs_checksummed_count": string,
  "merge_request_diffs_checksum_failed_count": string,
  "merge_request_diffs_synced_count": string,
  "merge_request_diffs_failed_count": string,
  "merge_request_diffs_registry_count": string,
  "merge_request_diffs_verification_total_count": string,
  "merge_request_diffs_verified_count": string,
  "merge_request_diffs_verification_failed_count": string,
  "merge_request_diffs_oldest_unsynced_time": string,
  "organization_detail_uploads_count": string,
  "organization_detail_uploads_checksum_total_count": string,
  "organization_detail_uploads_checksummed_count": string,
  "organization_detail_uploads_checksum_failed_count": string,
  "organization_detail_uploads_synced_count": string,
  "organization_detail_uploads_failed_count": string,
  "organization_detail_uploads_registry_count": string,
  "organization_detail_uploads_verification_total_count": string,
  "organization_detail_uploads_verified_count": string,
  "organization_detail_uploads_verification_failed_count": string,
  "organization_detail_uploads_oldest_unsynced_time": string,
  "package_files_count": string,
  "package_files_checksum_total_count": string,
  "package_files_checksummed_count": string,
  "package_files_checksum_failed_count": string,
  "package_files_synced_count": string,
  "package_files_failed_count": string,
  "package_files_registry_count": string,
  "package_files_verification_total_count": string,
  "package_files_verified_count": string,
  "package_files_verification_failed_count": string,
  "package_files_oldest_unsynced_time": string,
  "packages_debian_project_component_files_count": string,
  "packages_debian_project_component_files_checksum_total_count": string,
  "packages_debian_project_component_files_checksummed_count": string,
  "packages_debian_project_component_files_checksum_failed_count": string,
  "packages_debian_project_component_files_synced_count": string,
  "packages_debian_project_component_files_failed_count": string,
  "packages_debian_project_component_files_registry_count": string,
  "packages_debian_project_component_files_verification_total_count": string,
  "packages_debian_project_component_files_verified_count": string,
  "packages_debian_project_component_files_verification_failed_count": string,
  "packages_debian_project_component_files_oldest_unsynced_time": string,
  "packages_helm_metadata_caches_count": string,
  "packages_helm_metadata_caches_checksum_total_count": string,
  "packages_helm_metadata_caches_checksummed_count": string,
  "packages_helm_metadata_caches_checksum_failed_count": string,
  "packages_helm_metadata_caches_synced_count": string,
  "packages_helm_metadata_caches_failed_count": string,
  "packages_helm_metadata_caches_registry_count": string,
  "packages_helm_metadata_caches_verification_total_count": string,
  "packages_helm_metadata_caches_verified_count": string,
  "packages_helm_metadata_caches_verification_failed_count": string,
  "packages_helm_metadata_caches_oldest_unsynced_time": string,
  "packages_nuget_symbols_count": string,
  "packages_nuget_symbols_checksum_total_count": string,
  "packages_nuget_symbols_checksummed_count": string,
  "packages_nuget_symbols_checksum_failed_count": string,
  "packages_nuget_symbols_synced_count": string,
  "packages_nuget_symbols_failed_count": string,
  "packages_nuget_symbols_registry_count": string,
  "packages_nuget_symbols_verification_total_count": string,
  "packages_nuget_symbols_verified_count": string,
  "packages_nuget_symbols_verification_failed_count": string,
  "packages_nuget_symbols_oldest_unsynced_time": string,
  "pages_deployments_count": string,
  "pages_deployments_checksum_total_count": string,
  "pages_deployments_checksummed_count": string,
  "pages_deployments_checksum_failed_count": string,
  "pages_deployments_synced_count": string,
  "pages_deployments_failed_count": string,
  "pages_deployments_registry_count": string,
  "pages_deployments_verification_total_count": string,
  "pages_deployments_verified_count": string,
  "pages_deployments_verification_failed_count": string,
  "pages_deployments_oldest_unsynced_time": string,
  "personal_snippet_uploads_count": string,
  "personal_snippet_uploads_checksum_total_count": string,
  "personal_snippet_uploads_checksummed_count": string,
  "personal_snippet_uploads_checksum_failed_count": string,
  "personal_snippet_uploads_synced_count": string,
  "personal_snippet_uploads_failed_count": string,
  "personal_snippet_uploads_registry_count": string,
  "personal_snippet_uploads_verification_total_count": string,
  "personal_snippet_uploads_verified_count": string,
  "personal_snippet_uploads_verification_failed_count": string,
  "personal_snippet_uploads_oldest_unsynced_time": string,
  "pipeline_artifacts_count": string,
  "pipeline_artifacts_checksum_total_count": string,
  "pipeline_artifacts_checksummed_count": string,
  "pipeline_artifacts_checksum_failed_count": string,
  "pipeline_artifacts_synced_count": string,
  "pipeline_artifacts_failed_count": string,
  "pipeline_artifacts_registry_count": string,
  "pipeline_artifacts_verification_total_count": string,
  "pipeline_artifacts_verified_count": string,
  "pipeline_artifacts_verification_failed_count": string,
  "pipeline_artifacts_oldest_unsynced_time": string,
  "project_import_export_relation_export_upload_uploads_count": string,
  "project_import_export_relation_export_upload_uploads_checksum_total_count": string,
  "project_import_export_relation_export_upload_uploads_checksummed_count": string,
  "project_import_export_relation_export_upload_uploads_checksum_failed_count": string,
  "project_import_export_relation_export_upload_uploads_synced_count": string,
  "project_import_export_relation_export_upload_uploads_failed_count": string,
  "project_import_export_relation_export_upload_uploads_registry_count": string,
  "project_import_export_relation_export_upload_uploads_verification_total_count": string,
  "project_import_export_relation_export_upload_uploads_verified_count": string,
  "project_import_export_relation_export_upload_uploads_verification_failed_count": string,
  "project_import_export_relation_export_upload_uploads_oldest_unsynced_time": string,
  "project_repositories_count": string,
  "project_repositories_checksum_total_count": string,
  "project_repositories_checksummed_count": string,
  "project_repositories_checksum_failed_count": string,
  "project_repositories_synced_count": string,
  "project_repositories_failed_count": string,
  "project_repositories_registry_count": string,
  "project_repositories_verification_total_count": string,
  "project_repositories_verified_count": string,
  "project_repositories_verification_failed_count": string,
  "project_repositories_oldest_unsynced_time": string,
  "project_topic_uploads_count": string,
  "project_topic_uploads_checksum_total_count": string,
  "project_topic_uploads_checksummed_count": string,
  "project_topic_uploads_checksum_failed_count": string,
  "project_topic_uploads_synced_count": string,
  "project_topic_uploads_failed_count": string,
  "project_topic_uploads_registry_count": string,
  "project_topic_uploads_verification_total_count": string,
  "project_topic_uploads_verified_count": string,
  "project_topic_uploads_verification_failed_count": string,
  "project_topic_uploads_oldest_unsynced_time": string,
  "project_uploads_count": string,
  "project_uploads_checksum_total_count": string,
  "project_uploads_checksummed_count": string,
  "project_uploads_checksum_failed_count": string,
  "project_uploads_synced_count": string,
  "project_uploads_failed_count": string,
  "project_uploads_registry_count": string,
  "project_uploads_verification_total_count": string,
  "project_uploads_verified_count": string,
  "project_uploads_verification_failed_count": string,
  "project_uploads_oldest_unsynced_time": string,
  "project_wiki_repositories_count": string,
  "project_wiki_repositories_checksum_total_count": string,
  "project_wiki_repositories_checksummed_count": string,
  "project_wiki_repositories_checksum_failed_count": string,
  "project_wiki_repositories_synced_count": string,
  "project_wiki_repositories_failed_count": string,
  "project_wiki_repositories_registry_count": string,
  "project_wiki_repositories_verification_total_count": string,
  "project_wiki_repositories_verified_count": string,
  "project_wiki_repositories_verification_failed_count": string,
  "project_wiki_repositories_oldest_unsynced_time": string,
  "snippet_repositories_count": string,
  "snippet_repositories_checksum_total_count": string,
  "snippet_repositories_checksummed_count": string,
  "snippet_repositories_checksum_failed_count": string,
  "snippet_repositories_synced_count": string,
  "snippet_repositories_failed_count": string,
  "snippet_repositories_registry_count": string,
  "snippet_repositories_verification_total_count": string,
  "snippet_repositories_verified_count": string,
  "snippet_repositories_verification_failed_count": string,
  "snippet_repositories_oldest_unsynced_time": string,
  "supply_chain_attestations_count": string,
  "supply_chain_attestations_checksum_total_count": string,
  "supply_chain_attestations_checksummed_count": string,
  "supply_chain_attestations_checksum_failed_count": string,
  "supply_chain_attestations_synced_count": string,
  "supply_chain_attestations_failed_count": string,
  "supply_chain_attestations_registry_count": string,
  "supply_chain_attestations_verification_total_count": string,
  "supply_chain_attestations_verified_count": string,
  "supply_chain_attestations_verification_failed_count": string,
  "supply_chain_attestations_oldest_unsynced_time": string,
  "terraform_state_versions_count": string,
  "terraform_state_versions_checksum_total_count": string,
  "terraform_state_versions_checksummed_count": string,
  "terraform_state_versions_checksum_failed_count": string,
  "terraform_state_versions_synced_count": string,
  "terraform_state_versions_failed_count": string,
  "terraform_state_versions_registry_count": string,
  "terraform_state_versions_verification_total_count": string,
  "terraform_state_versions_verified_count": string,
  "terraform_state_versions_verification_failed_count": string,
  "terraform_state_versions_oldest_unsynced_time": string,
  "uploads_count": string,
  "uploads_checksum_total_count": string,
  "uploads_checksummed_count": string,
  "uploads_checksum_failed_count": string,
  "uploads_synced_count": string,
  "uploads_failed_count": string,
  "uploads_registry_count": string,
  "uploads_verification_total_count": string,
  "uploads_verified_count": string,
  "uploads_verification_failed_count": string,
  "uploads_oldest_unsynced_time": string,
  "user_permission_export_upload_uploads_count": string,
  "user_permission_export_upload_uploads_checksum_total_count": string,
  "user_permission_export_upload_uploads_checksummed_count": string,
  "user_permission_export_upload_uploads_checksum_failed_count": string,
  "user_permission_export_upload_uploads_synced_count": string,
  "user_permission_export_upload_uploads_failed_count": string,
  "user_permission_export_upload_uploads_registry_count": string,
  "user_permission_export_upload_uploads_verification_total_count": string,
  "user_permission_export_upload_uploads_verified_count": string,
  "user_permission_export_upload_uploads_verification_failed_count": string,
  "user_permission_export_upload_uploads_oldest_unsynced_time": string,
  "user_uploads_count": string,
  "user_uploads_checksum_total_count": string,
  "user_uploads_checksummed_count": string,
  "user_uploads_checksum_failed_count": string,
  "user_uploads_synced_count": string,
  "user_uploads_failed_count": string,
  "user_uploads_registry_count": string,
  "user_uploads_verification_total_count": string,
  "user_uploads_verified_count": string,
  "user_uploads_verification_failed_count": string,
  "user_uploads_oldest_unsynced_time": string,
  "vulnerability_archive_export_uploads_count": string,
  "vulnerability_archive_export_uploads_checksum_total_count": string,
  "vulnerability_archive_export_uploads_checksummed_count": string,
  "vulnerability_archive_export_uploads_checksum_failed_count": string,
  "vulnerability_archive_export_uploads_synced_count": string,
  "vulnerability_archive_export_uploads_failed_count": string,
  "vulnerability_archive_export_uploads_registry_count": string,
  "vulnerability_archive_export_uploads_verification_total_count": string,
  "vulnerability_archive_export_uploads_verified_count": string,
  "vulnerability_archive_export_uploads_verification_failed_count": string,
  "vulnerability_archive_export_uploads_oldest_unsynced_time": string,
  "vulnerability_export_part_uploads_count": string,
  "vulnerability_export_part_uploads_checksum_total_count": string,
  "vulnerability_export_part_uploads_checksummed_count": string,
  "vulnerability_export_part_uploads_checksum_failed_count": string,
  "vulnerability_export_part_uploads_synced_count": string,
  "vulnerability_export_part_uploads_failed_count": string,
  "vulnerability_export_part_uploads_registry_count": string,
  "vulnerability_export_part_uploads_verification_total_count": string,
  "vulnerability_export_part_uploads_verified_count": string,
  "vulnerability_export_part_uploads_verification_failed_count": string,
  "vulnerability_export_part_uploads_oldest_unsynced_time": string,
  "vulnerability_export_uploads_count": string,
  "vulnerability_export_uploads_checksum_total_count": string,
  "vulnerability_export_uploads_checksummed_count": string,
  "vulnerability_export_uploads_checksum_failed_count": string,
  "vulnerability_export_uploads_synced_count": string,
  "vulnerability_export_uploads_failed_count": string,
  "vulnerability_export_uploads_registry_count": string,
  "vulnerability_export_uploads_verification_total_count": string,
  "vulnerability_export_uploads_verified_count": string,
  "vulnerability_export_uploads_verification_failed_count": string,
  "vulnerability_export_uploads_oldest_unsynced_time": string,
  "vulnerability_remediation_uploads_count": string,
  "vulnerability_remediation_uploads_checksum_total_count": string,
  "vulnerability_remediation_uploads_checksummed_count": string,
  "vulnerability_remediation_uploads_checksum_failed_count": string,
  "vulnerability_remediation_uploads_synced_count": string,
  "vulnerability_remediation_uploads_failed_count": string,
  "vulnerability_remediation_uploads_registry_count": string,
  "vulnerability_remediation_uploads_verification_total_count": string,
  "vulnerability_remediation_uploads_verified_count": string,
  "vulnerability_remediation_uploads_verification_failed_count": string,
  "vulnerability_remediation_uploads_oldest_unsynced_time": string,
  "git_fetch_event_count_weekly": string,
  "git_push_event_count_weekly": string,
  "proxy_remote_requests_event_count_weekly": string,
  "proxy_local_requests_event_count_weekly": string,
  "repositories_checked_in_percentage": string,
  "replication_slots_used_in_percentage": string,
  "abuse_report_uploads_synced_in_percentage": string,
  "abuse_report_uploads_verified_in_percentage": string,
  "achievement_uploads_synced_in_percentage": string,
  "achievement_uploads_verified_in_percentage": string,
  "ai_vectorizable_file_uploads_synced_in_percentage": string,
  "ai_vectorizable_file_uploads_verified_in_percentage": string,
  "alert_management_metric_image_uploads_synced_in_percentage": string,
  "alert_management_metric_image_uploads_verified_in_percentage": string,
  "appearance_uploads_synced_in_percentage": string,
  "appearance_uploads_verified_in_percentage": string,
  "bulk_import_export_upload_uploads_synced_in_percentage": string,
  "bulk_import_export_upload_uploads_verified_in_percentage": string,
  "ci_secure_files_synced_in_percentage": string,
  "ci_secure_files_verified_in_percentage": string,
  "container_repositories_synced_in_percentage": string,
  "container_repositories_verified_in_percentage": string,
  "dependency_list_export_part_uploads_synced_in_percentage": string,
  "dependency_list_export_part_uploads_verified_in_percentage": string,
  "dependency_list_export_uploads_synced_in_percentage": string,
  "dependency_list_export_uploads_verified_in_percentage": string,
  "dependency_proxy_blobs_synced_in_percentage": string,
  "dependency_proxy_blobs_verified_in_percentage": string,
  "dependency_proxy_manifests_synced_in_percentage": string,
  "dependency_proxy_manifests_verified_in_percentage": string,
  "design_management_action_uploads_synced_in_percentage": string,
  "design_management_action_uploads_verified_in_percentage": string,
  "design_management_repositories_synced_in_percentage": string,
  "design_management_repositories_verified_in_percentage": string,
  "group_uploads_synced_in_percentage": string,
  "group_uploads_verified_in_percentage": string,
  "group_wiki_repositories_synced_in_percentage": string,
  "group_wiki_repositories_verified_in_percentage": string,
  "import_export_upload_uploads_synced_in_percentage": string,
  "import_export_upload_uploads_verified_in_percentage": string,
  "issuable_metric_image_uploads_synced_in_percentage": string,
  "issuable_metric_image_uploads_verified_in_percentage": string,
  "job_artifacts_synced_in_percentage": string,
  "job_artifacts_verified_in_percentage": string,
  "lfs_objects_synced_in_percentage": string,
  "lfs_objects_verified_in_percentage": string,
  "merge_request_diffs_synced_in_percentage": string,
  "merge_request_diffs_verified_in_percentage": string,
  "organization_detail_uploads_synced_in_percentage": string,
  "organization_detail_uploads_verified_in_percentage": string,
  "package_files_synced_in_percentage": string,
  "package_files_verified_in_percentage": string,
  "packages_debian_project_component_files_synced_in_percentage": string,
  "packages_debian_project_component_files_verified_in_percentage": string,
  "packages_helm_metadata_caches_synced_in_percentage": string,
  "packages_helm_metadata_caches_verified_in_percentage": string,
  "packages_nuget_symbols_synced_in_percentage": string,
  "packages_nuget_symbols_verified_in_percentage": string,
  "pages_deployments_synced_in_percentage": string,
  "pages_deployments_verified_in_percentage": string,
  "personal_snippet_uploads_synced_in_percentage": string,
  "personal_snippet_uploads_verified_in_percentage": string,
  "pipeline_artifacts_synced_in_percentage": string,
  "pipeline_artifacts_verified_in_percentage": string,
  "project_import_export_relation_export_upload_uploads_synced_in_percentage": string,
  "project_import_export_relation_export_upload_uploads_verified_in_percentage": string,
  "project_repositories_synced_in_percentage": string,
  "project_repositories_verified_in_percentage": string,
  "project_topic_uploads_synced_in_percentage": string,
  "project_topic_uploads_verified_in_percentage": string,
  "project_uploads_synced_in_percentage": string,
  "project_uploads_verified_in_percentage": string,
  "project_wiki_repositories_synced_in_percentage": string,
  "project_wiki_repositories_verified_in_percentage": string,
  "snippet_repositories_synced_in_percentage": string,
  "snippet_repositories_verified_in_percentage": string,
  "supply_chain_attestations_synced_in_percentage": string,
  "supply_chain_attestations_verified_in_percentage": string,
  "terraform_state_versions_synced_in_percentage": string,
  "terraform_state_versions_verified_in_percentage": string,
  "uploads_synced_in_percentage": string,
  "uploads_verified_in_percentage": string,
  "user_permission_export_upload_uploads_synced_in_percentage": string,
  "user_permission_export_upload_uploads_verified_in_percentage": string,
  "user_uploads_synced_in_percentage": string,
  "user_uploads_verified_in_percentage": string,
  "vulnerability_archive_export_uploads_synced_in_percentage": string,
  "vulnerability_archive_export_uploads_verified_in_percentage": string,
  "vulnerability_export_part_uploads_synced_in_percentage": string,
  "vulnerability_export_part_uploads_verified_in_percentage": string,
  "vulnerability_export_uploads_synced_in_percentage": string,
  "vulnerability_export_uploads_verified_in_percentage": string,
  "vulnerability_remediation_uploads_synced_in_percentage": string,
  "vulnerability_remediation_uploads_verified_in_percentage": string,
  "repositories_count": string,
  "replication_slots_count": string,
  "replication_slots_used_count": string,
  "healthy": string,
  "health": string,
  "health_status": string,
  "missing_oauth_application": string,
  "db_replication_lag_seconds": string,
  "replication_slots_max_retained_wal_bytes": string,
  "repositories_checked_count": string,
  "repositories_checked_failed_count": string,
  "last_event_id": string,
  "last_event_timestamp": string,
  "cursor_last_event_id": string,
  "cursor_last_event_timestamp": string,
  "last_successful_status_check_timestamp": string,
  "version": string,
  "revision": string,
  "selective_sync_type": string,
  "namespaces": {
    "id": integer,
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
  "updated_at": string,
  "storage_shards": {
    "name": string,
  },
  "storage_shards_match": string,
  "_links": string,
}
```

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

