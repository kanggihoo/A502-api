# Commit statuses

Operations related to commit statuses.

## Endpoints

- [01-List all commit statuses [GET]](./01-list-all-commit-statuses-get.md)
- [02-Create or update a commit pipeline status [POST]](./02-create-or-update-a-commit-pipeline-status-post.md)


**핵심 유용! (Jenkins-GitLab 연동 필수 API)**

---

### 주요 역할
외부 CI 도구(**Jenkins**)와 **GitLab** 간 파이프라인 빌드 상태(`success`, `failed`, `running`)를 주고받는 API.

---

### 활용 시나리오 (SSAFY EC2 Jenkins 환경)

1. **`02` Create or update commit pipeline status** (`POST /statuses/{sha}`)
   - **시나리오**: Jenkins에서 빌드/테스트 후, 이 API를 쏴서 GitLab 커밋 상에 **"Jenkins 빌드 성공 ✅"** / **"빌드 실패 ❌"** 표시 갱신.
   - **이점**: `target_url`에 Jenkins 빌드 로그 상세 URL을 연동하여 GitLab MR 화면에서 클릭 한 번으로 Jenkins 로그로 바로 이동 가능.

2. **`01` List all commit statuses** (`GET /repository/commits/{sha}/statuses`)
   - **시나리오**: 통합 대시보드에서 특정 커밋/MR의 젠킨스 빌드 상태 및 Jenkins 결과 URL 획득.

---

### 결론
SSAFY 제공 도구인 **Jenkins와 GitLab을 연결할 때 반드시 필요한 핵심 연동 API.**
