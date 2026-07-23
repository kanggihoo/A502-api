# Metadata API 명세서 (관리자 권한 미필요 API)

본 문서는 `_95-metadata` 디렉토리 내의 GitLab Metadata (GitLab 인스턴스의 버전, 리비전, KAS 및 에디션 메타데이터 조회) 관련 API 중 일반 사용자 및 인증된 유저 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 2개)

---

## 01. Retrieve metadata information for this GitLab instance [GET]

### 기본 정보

- **기능:** 현재 사용 중인 GitLab 인스턴스의 버전, 리비전, KAS 및 에디션 메타데이터를 조회한다.
- **Endpoint:** `GET /api/v4/metadata`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

Self-hosted 및 SaaS GitLab 인스턴스의 현재 소프트웨어 버전(`version`), Git 커밋 리비전(`revision`), Kubernetes Agent Server(KAS) 정보, 엔터프라이즈 에디션 여부(`enterprise`)를 확인합니다. 외부 연동 도구(SSAFY 워크스페이스 대시보드)에서 호환되는 API 버전을 판별할 때 주로 호출됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

없음

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `version` | string | GitLab 소프트웨어 버전 | `17.1.0-ee` |
| `revision` | string | Build Git 리비전 SHA | `a1b2c3d4e5f` |
| `kas` | object | Kubernetes Agent Server 상태 객체 | `{ "enabled": true, "version": "17.1.0" }` |
| `enterprise` | boolean | Enterprise Edition 여부 | `true` |

```json
{
  "version": "17.1.0-ee",
  "revision": "a1b2c3d4e5f",
  "kas": {
    "enabled": true,
    "version": "17.1.0",
    "external_url": "wss://kas.ssafy.com"
  },
  "enterprise": true
}
```


