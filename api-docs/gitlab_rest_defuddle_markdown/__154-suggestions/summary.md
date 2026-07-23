# Suggestions API 명세서 (관리자 권한 미필요 API)

본 문서는 `_154-suggestions` 디렉토리 내의 GitLab Suggestions (Merge Request 코드 리뷰 인라인 코드 제안 반영) 관련 API 중 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 2개)

---

## 01. Apply a suggestion to a merge request [PUT]

### 기본 정보

- **기능:** Merge Request의 특정 인라인 코드 제안(Suggestion)을 커밋으로 반영 적용한다.
- **Endpoint:** `PUT /api/v4/suggestions/{id}/apply`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer, Maintainer, Owner)

### 설명

Merge Request의 코드 리뷰 작성자가 등록한 단일 인라인 코드 제안(`suggestion`)을 소스코드 브랜치에 커밋 패치로 적용합니다. 커밋 시 기본 메시지 대신 커스텀 커밋 메시지(`commit_message`)를 지정할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer | Y | 코드 제안(Suggestion) ID | `1005` |

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `commit_message` | string | N | - | 커스텀 커밋 메시지 (미지정 시 기본 생성 메시지 사용) | `Apply suggestion from code review` |

```json
{
  "commit_message": "Apply suggestion from code review"
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 코드 제안 ID | `1005` |
| `from_line` | integer | 대상 시작 라인 번호 | `42` |
| `to_line` | integer | 대상 종료 라인 번호 | `45` |
| `appliable` | boolean | 적용 가능 여부 | `true` |
| `applied` | boolean | 커밋 반영 완료 여부 | `true` |
| `from_content` | string | 기존 원본 코드 내용 | `old code line` |
| `to_content` | string | 변경 제안된 코드 내용 | `new suggested code line` |

```json
{
  "id": 1005,
  "from_line": 42,
  "to_line": 45,
  "appliable": true,
  "applied": true,
  "from_content": "old code line",
  "to_content": "new suggested code line"
}
```

---

## 02. Apply multiple suggestions to a merge request [PUT]

### 기본 정보

- **기능:** Merge Request의 여러 인라인 코드 제안(Suggestions)을 단일 배치 커밋으로 일괄 반영 적용한다.
- **Endpoint:** `PUT /api/v4/suggestions/batch_apply`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer, Maintainer, Owner)

### 설명

Merge Request 내에서 여러 개의 인라인 코드 수정 제안 ID 배열(`ids`)을 전달하여 하나의 통합 커밋 패치로 일괄 반영시킵니다. 커스텀 커밋 메시지를 지정할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

없음

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ids` | array[integer] | Y | 1개 이상 | 일괄 적용할 코드 제안 ID 목록 | `[1005, 1006, 1007]` |
| `commit_message` | string | N | - | 일괄 커밋 메시지 | `Apply batch code review suggestions` |

```json
{
  "ids": [
    1005,
    1006,
    1007
  ],
  "commit_message": "Apply batch code review suggestions"
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 처리된 제안 ID | `1005` |
| `applied` | boolean | 커밋 반영 완료 여부 | `true` |
| `from_content` | string | 기존 원본 코드 | `old code` |
| `to_content` | string | 제안된 변경 코드 | `new code` |

```json
{
  "id": 1005,
  "from_line": 42,
  "to_line": 45,
  "appliable": true,
  "applied": true,
  "from_content": "old code",
  "to_content": "new code"
}
```
