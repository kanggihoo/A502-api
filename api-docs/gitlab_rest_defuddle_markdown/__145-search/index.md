# Search

  ### 3. Search API

  • 유용성: P1 (통합 검색 기능 유용).
      • Search within project (06번), Search within group (05번): 통합 대시보드 검색창에서
      프로젝트/그룹 내 이슈, MR, 커밋, 댓글, 사용자 원문 검색.
      • Search instance (04번): 접근 권한이 있는 전역 항목 검색.
  • 제약 사항 (일부 기능 제한):
      • Search using natural language (01번): GitLab Duo Enterprise (유료 AI 구독) 전용.
      • Advanced search migrations (02, 03번): Elasticsearch/Opensearch 검색 인덱싱 Admin 전용.
  • 티어/권한: 기본 표준 검색(04, 05, 06번)은 Free / CE 지원. Developer 이상 가능.
## Endpoints

- [01-Search project code using natural language [GET]](./01-search-project-code-using-natural-language-get.md)
- [02-List all advanced search migrations [GET]](./02-list-all-advanced-search-migrations-get.md)
- [03-Retrieve an advanced search migration [GET]](./03-retrieve-an-advanced-search-migration-get.md)
- [04-Search an instance [GET]](./04-search-an-instance-get.md)
- [05-Search on GitLab within a group [GET]](./05-search-on-gitlab-within-a-group-get.md)
- [06-Search on GitLab within a project [GET]](./06-search-on-gitlab-within-a-project-get.md)
