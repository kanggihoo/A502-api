# Deploy Resources API 명세서 (관리자 권한 미필요 API)

본 문서는 `_45-deploy-resources` 디렉토리 내의 GitLab Deploy Resources (프로젝트/그룹 배포 환경, Deploy Token 및 Deploy Key) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 24개)

> **관리자(Admin) 전용 API 제외 목록 (1개)**
> - `19-create-a-deploy-key-post.md`: GitLab 인스턴스 전역 디플로이 키 생성 (`POST /api/v4/deploy_keys` - Admin 전용)

---


## 02 ~ 08. Project Deployments (GET, POST, GET, PUT, DEL, GET MRs, POST Approve/Reject)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/deployments`: 프로젝트의 배포(Deployment) 이력 목록 조회
  - `POST /api/v4/projects/{id}/deployments`: 신규 배포 기록 생성 (`environment`, `sha`, `ref`, `status`)
  - `GET /api/v4/projects/{id}/deployments/{deployment_id}`: 단일 배포 상세 정보 조회
  - `PUT /api/v4/projects/{id}/deployments/{deployment_id}`: 배포 상태(`status`: `running`, `success`, `failed`, `canceled`) 업데이트
  - `DELETE /api/v4/projects/{id}/deployments/{deployment_id}`: 배포 기록 삭제
  - `GET /api/v4/projects/{id}/deployments/{deployment_id}/merge_requests`: 해당 배포에 포함된 Merge Request 목록 조회
  - `POST /api/v4/projects/{id}/deployments/{deployment_id}/approval`: 승인 필요 배포에 대한 승인/거절 처리 (`status`: `approved` \| `rejected`)
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상, 승인 처리는 Maintainer/Protected Environment 승인권자)
- **설명:** SSAFY EC2 인스턴스로의 자동 배포 상태 트래킹, 배포 완료 알림, 배포 승인 워크플로우 구성 시 활용됩니다.

---

## 09 ~ 13. Project Deploy Tokens (GET, GET, POST, GET, DEL)

- **Endpoints:**
  - `GET /api/v4/deploy_tokens`: 접근 가능한 디플로이 토큰 목록 조회
  - `GET /api/v4/projects/{id}/deploy_tokens`: 프로젝트의 디플로이 토큰 목록 조회
  - `POST /api/v4/projects/{id}/deploy_tokens`: 프로젝트 디플로이 토큰 생성 (`name`, `scopes`: `read_repository`, `read_registry`)
  - `GET /api/v4/projects/{id}/deploy_tokens/{token_id}`: 단일 프로젝트 디플로이 토큰 상세 조회
  - `DELETE /api/v4/projects/{id}/deploy_tokens/{token_id}`: 프로젝트 디플로이 토큰 폐기/삭제
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner
- **설명:** CI/CD 파이프라인이나 외부 EC2 서버에서 비밀번호 없이 저장소 코드 및 컨테이너 레지스트리(GitLab Container Registry) 이미지를 다운로드할 수 있는 전용 디플로이 토큰을 관리합니다.

---


## 18, 20 ~ 25. Project Deploy Keys (GET, GET, POST, GET, PUT, DEL, POST Enable)

- **Endpoints:**
  - `GET /api/v4/deploy_keys`: 전체 접근 가능한 디플로이 SSH 키 목록 조회
  - `GET /api/v4/projects/{id}/deploy_keys`: 프로젝트에 등록된 SSH 디플로이 키 목록 조회
  - `POST /api/v4/projects/{id}/deploy_keys`: 프로젝트 전용 SSH 디플로이 키 생성 및 등록 (`title`, `key`, `can_push`)
  - `GET /api/v4/projects/{id}/deploy_keys/{key_id}`: 단일 디플로이 키 상세 조회
  - `PUT /api/v4/projects/{id}/deploy_keys/{key_id}`: 디플로이 키 설정(제목, 푸시 권한 여부) 수정
  - `DELETE /api/v4/projects/{id}/deploy_keys/{key_id}`: 프로젝트 디플로이 키 삭제
  - `POST /api/v4/projects/{id}/deploy_keys/{key_id}/enable`: 기존 공개 디플로이 키를 프로젝트에 활성화 연결
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner
- **설명:** EC2 인스턴스 서버에서 GitLab 저장소로 SSH 통신을 수행할 수 있도록 SSH 디플로이 키를 등록/연결 관리합니다.
