# 25 CI Lint API Spec

---

## 1. Validate existing CI/CD configuration [GET]

### 기본 정보
- **기능:** 프로젝트의 `.gitlab-ci.yml` 설정 유효성 검증
- **Endpoint:** `GET /api/v4/projects/{id}/ci/lint`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 `.gitlab-ci.yml` 설정이 유효한지 정적 검사 또는 dry run 방식으로 검증한다. `content_ref`로 특정 커밋/브랜치/태그의 설정을 검사할 수 있고, `dry_run`을 활성화하면 파이프라인 생성을 시뮬레이션한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `sha` | `string` | N | (Deprecated) `content_ref` 사용 |
| `content_ref` | `string` | N | CI/CD 설정을 가져올 커밋 SHA, 브랜치 또는 태그. 기본값은 HEAD |
| `dry_run` | `boolean` | N | 파이프라인 생성 시뮬레이션 실행 여부 (기본값: false) |
| `include_jobs` | `boolean` | N | 응답에 job 목록 포함 여부 (기본값: false) |
| `ref` | `string` | N | (Deprecated) `dry_run_ref` 사용 |
| `dry_run_ref` | `string` | N | dry run 실행 시 컨텍스트로 사용할 브랜치/태그. 기본값은 default 브랜치 |

### Response
#### `200 OK`
```json
{
  "valid": "boolean",
  "errors": ["string"],
  "warnings": ["string"],
  "merged_yaml": "string",
  "includes": [
    {
      "type": "string",
      "location": "string",
      "blob": "string",
      "raw": "string",
      "extra": {},
      "context_project": "string",
      "context_sha": "string"
    }
  ],
  "jobs": [{}]
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `valid` | `boolean` | 설정 유효 여부 |
| `errors` | `string[]` | 오류 메시지 목록 |
| `warnings` | `string[]` | 경고 메시지 목록 |
| `merged_yaml` | `string` | include가 병합된 최종 YAML |
| `includes` | `object[]` | include 항목 목록 |
| `jobs` | `object[]` | dry_run/include_jobs 활성화 시 job 목록 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
