# __29-issue-links API 요약

이 리소스 그룹은 이슈 간의 링크(관계)를 조회, 생성, 삭제하는 Jira REST API 모음이다. 사이트에 Issue Linking 기능이 활성화되어 있어야 사용할 수 있다.

## 제외된 API

- 없음 (모든 엔드포인트가 프로젝트 권한 수준(Browse project, Link issues)으로 호출 가능하며 사이트 전체 관리자 권한을 요구하지 않음)

---

### [높음] 1. 이슈 링크 생성 (POST /rest/api/3/issueLink)

## 기본 정보

- **기능:** 두 이슈 사이에 링크(관계)를 생성한다. 필요시 from(outward) 이슈에 코멘트를 함께 추가할 수 있다.
- **Endpoint:** `POST /rest/api/3/issueLink`
- **인증:** 불필요 (익명 접근 가능, 단 결과는 권한에 따라 제한됨)
- **권한:** 연결하려는 모든 프로젝트에 대한 *Browse project* 권한, outward(from) 이슈가 속한 프로젝트에 대한 *Link issues* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한도 필요. 코멘트에 공개 범위 제한이 있으면 해당 그룹/역할에 속해야 함.

## 설명

이슈 링크 생성은 두 이슈 간 관계(예: Duplicate, Blocks 등)를 등록하는 핵심 API로, 팀 프로젝트 운영 지원에서 이슈 간 의존성/관계를 자동으로 관리할 때 사용할 수 있다. 링크 생성 시 중복된 링크 요청이 들어와도 성공 응답을 반환하며, 코멘트가 포함된 요청이면 코멘트도 함께 등록된다. 이 엔드포인트는 생성된 링크에 대한 어떤 데이터도 응답으로 반환하지 않으므로, 링크 ID가 필요하면 `GET /rest/api/3/issue/{linked issue key}?fields=issuelinks`를 별도로 호출해야 한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `comment` | object | N | - | from(outward) 이슈에 추가할 코멘트 객체 (ADF 형식의 `body` 포함) | `{"body": "..."}` |
| `inwardIssue` | object | Y | `id` 또는 `key` 중 하나 필수 | 링크의 inward 쪽 이슈 | `{"key": "PR-3"}` |
| `outwardIssue` | object | Y | `id` 또는 `key` 중 하나 필수 | 링크의 outward(from) 쪽 이슈 | `{"key": "PR-2"}` |
| `type` | object | Y | `id` 또는 `name` 중 하나로 링크 타입 지정 | 이슈 링크 타입 (예: Duplicate) | `{"name": "Duplicate"}` |

```json
{
  "comment": {
    "body": "Linked related issue!"
  },
  "inwardIssue": {
    "key": "PR-3"
  },
  "outwardIssue": {
    "key": "PR-2"
  },
  "type": {
    "name": "Duplicate"
  }
}
```

## Response

### `201 Created`

응답 본문 없음 (요청이 성공했음을 의미하며, 생성된 링크의 상세 정보는 반환되지 않는다).

## Errors

| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| 400 | 코멘트가 생성되지 못함 (이 경우 이슈 링크도 생성되지 않음) | 오류 메시지를 확인하여 코멘트 본문/형식을 수정 후 재시도 |
| 401 | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | 이슈 링크 기능 비활성화 / 이슈를 볼 권한 없음(Browse project 없음) / Link issues 권한 없음 / 연결할 이슈를 찾을 수 없음 / 링크 타입을 찾을 수 없음 | 사이트의 Issue Linking 활성화 여부, 프로젝트 권한, 이슈 키/링크 타입명 확인 |
| 413 | 이슈당 링크 개수 제한 초과 | 기존 링크 정리 필요 |

## 주의 사항

- 응답으로 링크 ID가 오지 않으므로, 생성 직후 링크 ID가 필요하면 이슈 조회 API(`fields=issuelinks`)를 추가로 호출해야 한다.
- 중복된 링크를 요청해도 오류가 아니라 성공으로 처리된다.
- `type`은 `id` 또는 `name` 중 하나만 있으면 되고, `inwardIssue`/`outwardIssue`도 `id` 또는 `key` 중 하나만 있으면 된다.

---

### [높음] 2. 이슈 링크 조회 (GET /rest/api/3/issueLink/{linkId})

## 기본 정보

- **기능:** 특정 이슈 링크의 상세 정보(연결된 두 이슈, 링크 타입 등)를 조회한다.
- **Endpoint:** `GET /rest/api/3/issueLink/{linkId}`
- **인증:** 불필요 (익명 접근 가능, 단 결과는 권한에 따라 제한됨)
- **권한:** 링크된 이슈들이 속한 모든 프로젝트에 대한 *Browse project* 권한. 이슈 수준 보안이 설정된 경우 두 이슈 모두를 볼 수 있는 권한 필요.

## 설명

이 API는 이슈 링크 ID로 링크의 상세 정보(inward/outward 이슈, 링크 타입 등)를 가져온다. 통합 대시보드에서 이슈 간 관계 정보를 표시하거나, 링크 생성 후 실제 반영 여부를 확인할 때 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `linkId` | string | Y | 이슈 링크의 ID | `10001` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 이슈 링크 ID | `"10001"` |
| `inwardIssue` | object | inward 쪽 이슈 정보 (fields, id, key, self) | `{"key": "PR-3", ...}` |
| `outwardIssue` | object | outward 쪽 이슈 정보 (fields, id, key, self) | `{"key": "PR-2", ...}` |
| `type` | object | 링크 타입 정보 (id, name, inward, outward, self) | `{"name": "Duplicate", "inward": "Duplicated by", "outward": "Duplicates"}` |

```json
{
  "id": "10001",
  "inwardIssue": {
    "fields": {
      "issuetype": {
        "id": "1",
        "name": "Bug",
        "subtask": false
      },
      "priority": {
        "id": "2",
        "name": "Trivial"
      },
      "status": {
        "id": "5",
        "name": "Closed"
      }
    },
    "id": "10004",
    "key": "PR-3",
    "self": "https://your-domain.atlassian.net/rest/api/3/issue/PR-3"
  },
  "outwardIssue": {
    "fields": {
      "issuetype": {
        "id": "3",
        "name": "Task",
        "subtask": false
      },
      "priority": {
        "id": "1",
        "name": "Major"
      },
      "status": {
        "id": "10000",
        "name": "In Progress"
      }
    },
    "id": "10004L",
    "key": "PR-2",
    "self": "https://your-domain.atlassian.net/rest/api/3/issue/PR-2"
  },
  "type": {
    "id": "1000",
    "inward": "Duplicated by",
    "name": "Duplicate",
    "outward": "Duplicates",
    "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000"
  }
}
```

## Errors

| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| 400 | 이슈 링크 ID가 유효하지 않음 | `linkId` 형식 확인 |
| 401 | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | 이슈 링크 기능 비활성화 / 링크를 찾을 수 없음 / 필요한 권한 없음 | 링크 존재 여부와 프로젝트 권한 확인 |

## 주의 사항

- 링크된 두 이슈 중 하나라도 조회 권한이 없으면 404가 반환되므로, 대시보드에서 사용할 때는 조회 실패를 "링크 없음"과 구분해서 처리할 필요가 있다.

---

### [중간] 3. 이슈 링크 삭제 (DELETE /rest/api/3/issueLink/{linkId})

## 기본 정보

- **기능:** 특정 이슈 링크를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issueLink/{linkId}`
- **인증:** 불필요 (익명 접근 가능, 단 결과는 권한에 따라 제한됨)
- **권한:** 링크에 포함된 이슈들이 속한 모든 프로젝트에 대한 *Browse project* 권한, 링크에 포함된 이슈가 속한 프로젝트 중 최소 하나에 대한 *Link issues* 권한. 이슈 수준 보안이 설정된 경우 두 이슈 모두를 볼 수 있는 권한 필요.

## 설명

지정된 링크 ID의 이슈 링크를 삭제하는 보조 유지보수용 API이다. 잘못 생성된 링크를 정리하거나 이슈 관계가 더 이상 유효하지 않을 때 사용하며, 핵심 자동화/알림 흐름보다는 데이터 정합성 관리에 가깝다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `linkId` | string | Y | 이슈 링크의 ID | `10001` |

## Response

### `204 No Content`

요청이 성공하면 본문 없이 204를 반환한다. (문서상 200 응답도 명시되어 있으나 본문 스키마는 정의되어 있지 않음)

## Errors

| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| 400 | 이슈 링크 ID가 유효하지 않음 | `linkId` 형식 확인 |
| 401 | 인증 정보가 없거나 잘못됨 | 인증 토큰 확인 |
| 404 | 이슈 링크 기능 비활성화 / 링크를 찾을 수 없음 / 필요한 권한 없음 | 링크 존재 여부와 프로젝트 권한(Link issues) 확인 |

## 주의 사항

- 삭제는 되돌릴 수 없으므로, 자동화 스크립트에서 호출 전 대상 링크 ID를 명확히 확인해야 한다.
- *Link issues* 권한은 연결된 프로젝트 중 하나만 있어도 충분하다 (생성과 달리 특정 방향의 프로젝트로 제한되지 않음).
