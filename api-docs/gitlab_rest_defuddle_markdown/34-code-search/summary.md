# Code Search API 명세서 (관리자 권한 미필요 API)

본 문서는 `_34-code-search` 디렉토리 내의 GitLab Code Search (Zoekt 코드 검색 인덱싱 노드 및 네임스페이스 인덱스 관리) 관련 API를 정리한 문서입니다.

> **관리자(Admin) 전용 API 제외 및 비대상 안내**
>
> `_34-code-search` 디렉토리 내에 포함된 6개 API 전체는 최고 관리자(Instance Administrator) 권한이 필수인 인프라/서버 레벨 인덱싱 노드 관리 API (`/api/v4/admin/zoekt/...`)입니다.
> 따라서 관리자 권한이 필요 없는 일반 유저/프로젝트 멤버용 API는 **0개**입니다.

---

## 관리자 전용 API 필터링 제외 목록 (총 6개)

1. **`01. Triggers indexing for the specified project [PUT]`**
   - `PUT /api/v4/admin/zoekt/projects/{project_id}/index`
   - 특정 프로젝트의 Zoekt 코드 검색 인덱싱 트리거 (Admin 전용)
2. **`02. Update the number of replicas override for an enabled namespace [PATCH]`**
   - `PATCH /api/v4/admin/zoekt/namespaces/{id}`
   - Zoekt 인덱싱 네임스페이스의 복제본 수 재정의 설정 (Admin 전용)
3. **`03. Get all the Zoekt nodes [GET]`**
   - `GET /api/v4/admin/zoekt/shards`
   - Zoekt 인덱싱 노드/샤드 목록 조회 (Admin 전용)
4. **`04. Get all the indexed namespaces for this node [GET]`**
   - `GET /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces`
   - 특정 Zoekt 노드에 인덱싱된 네임스페이스 목록 조회 (Admin 전용)
5. **`05. Add a namespace to a node for Zoekt indexing [PUT]`**
   - `PUT /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces/{namespace_id}`
   - Zoekt 노드에 인덱싱할 네임스페이스 추가 (Admin 전용)
6. **`06. Remove a namespace from a node for Zoekt indexing [DEL]`**
   - `DELETE /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces/{namespace_id}`
   - Zoekt 노드에서 인덱싱된 네임스페이스 제거 (Admin 전용)
