# __45-issue-votes API 요약

이 리소스 그룹은 이슈에 대한 사용자 투표(vote)를 다룬다. 이슈의 투표 상세 조회, 투표 등록(Vote), 투표 취소(Unvote) 기능을 제공한다.

## 제외된 API

- 없음 (모든 API가 프로젝트 단위 권한(Browse projects)만 요구하며, 사이트 전체 관리자 권한이 필요한 API는 없음)

### [중간] 1. Get votes (GET /rest/api/3/issue/{issueIdOrKey}/votes)

## 기본 정보

- **기능:** 이슈에 대한 투표 상세 정보(투표 여부, 투표 수, 투표자 목록) 조회
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/votes`
- **인증:** 익명 접근 가능 (Bearer Token 불필요, 단 인증 시 자격 증명이 올바라야 함)
- **권한:** *Browse projects* 프로젝트 권한 (이슈가 속한 프로젝트에 대해). 이슈 수준 보안이 설정된 경우 해당 보안 권한도 필요. `voters` 필드는 *View voters and watchers* 권한이 없으면 상세 정보가 반환되지 않음

## 설명

이슈에 대한 투표 현황을 조회하는 API로, 현재 사용자가 투표했는지 여부(`hasVoted`), 총 투표 수(`votes`), 투표한 사용자 목록(`voters`)을 반환한다. Jira 전역 설정에서 "Allow users to vote on issues" 옵션이 켜져 있어야 동작한다. 익명으로도 호출할 수 있으나 익명 사용자는 `voters` 상세 정보를 볼 권한이 없을 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `hasVoted` | `boolean` | 현재 사용자의 투표 여부 | `true` |
| `self` | `string` | 이 리소스의 API 링크 | `https://your-domain.atlassian.net/rest/api/issue/MKY-1/votes` |
| `votes` | `integer` | 총 투표 수 | `24` |
| `voters` | `array` | 투표한 사용자 목록 (User 객체 배열) | 아래 예시 참고 |

```json
{
  "hasVoted": true,
  "self": "https://your-domain.atlassian.net/rest/api/issue/MKY-1/votes",
  "voters": [
    {
      "accountId": "5b10a2844c20165700ede21g",
      "accountType": "atlassian",
      "active": false,
      "avatarUrls": {
        "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16",
        "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24",
        "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32",
        "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48"
      },
      "displayName": "Mia Krystof",
      "key": "",
      "name": "",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
    }
  ],
  "votes": 24
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 자격 증명이 올바르지 않거나 없음 | 인증 정보 확인 후 재요청 |
| 404 | - | 투표 기능이 비활성화된 경우 / 이슈를 볼 권한이 없는 경우 / 이슈를 찾을 수 없는 경우 | 투표 설정 및 이슈 존재 여부, 권한 확인 |

## 주의 사항

- Jira 전역 설정 "Allow users to vote on issues" 옵션이 꺼져 있으면 404가 반환된다.
- *View voters and watchers* 권한이 없는 사용자에게는 `voters` 필드 상세 정보가 채워지지 않는다.

### [중간] 2. Add vote (POST /rest/api/3/issue/{issueIdOrKey}/votes)

## 기본 정보

- **기능:** 현재 사용자의 투표를 이슈에 추가 (Jira UI의 "Vote" 클릭과 동일)
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/votes`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 프로젝트 권한 (이슈가 속한 프로젝트에 대해). 이슈 수준 보안이 설정된 경우 해당 보안 권한도 필요

## 설명

지정한 이슈에 현재 인증된 사용자의 투표를 추가한다. Jira 전역 설정에서 "Allow users to vote on issues" 옵션이 켜져 있어야 하며, 성공 시 본문 없이 204를 반환한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

## Response

### `204 No Content`

성공 시 응답 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 형식 확인 |
| 401 | - | 인증 자격 증명이 올바르지 않거나 없음 | 인증 정보 확인 후 재요청 |
| 404 | - | 투표 기능이 비활성화된 경우 / 이슈를 찾을 수 없는 경우 | 투표 설정 및 이슈 존재 여부 확인 |

## 주의 사항

- 익명 접근은 불가하며 인증된 사용자만 호출 가능하다.
- 이미 투표한 이슈에 다시 호출했을 때의 동작은 문서에 명시되어 있지 않다.

### [중간] 3. Delete vote (DELETE /rest/api/3/issue/{issueIdOrKey}/votes)

## 기본 정보

- **기능:** 현재 사용자의 투표를 이슈에서 삭제 (Jira UI의 "Unvote" 클릭과 동일)
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/votes`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 프로젝트 권한 (이슈가 속한 프로젝트에 대해). 이슈 수준 보안이 설정된 경우 해당 보안 권한도 필요

## 설명

지정한 이슈에서 현재 인증된 사용자의 투표를 제거한다. Jira 전역 설정에서 "Allow users to vote on issues" 옵션이 켜져 있어야 하며, 성공 시 본문 없이 204를 반환한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | `string` | Yes | 이슈의 ID 또는 키 | `MKY-1` |

## Response

### `204 No Content`

성공 시 응답 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 자격 증명이 올바르지 않거나 없음 | 인증 정보 확인 후 재요청 |
| 404 | - | 투표 기능이 비활성화된 경우 / 사용자가 해당 이슈에 투표한 적이 없는 경우 / 이슈를 찾을 수 없는 경우 | 투표 설정, 기존 투표 여부, 이슈 존재 여부 확인 |

## 주의 사항

- 투표한 적이 없는 이슈에 대해 호출하면 404가 반환된다.
