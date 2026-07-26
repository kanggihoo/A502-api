# 1. Get the policies which are applied to a user's teams

## 기본 정보
- **기능**: 사용자가 속한 모든 팀에 적용되는 데이터 보존 정책을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/data_retention/team_policies`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인 조회 시. `manage_system` 권한이 있으면 타인 조회 가능)

## 설명
사용자가 속한 모든 팀에 적용되는 데이터 보존 정책 목록을 반환한다. 본인으로 로그인한 경우 자신의 정책을 조회할 수 있다. 최소 서버 버전은 5.35이며, E20 라이선스가 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 정책 수 |

## Response

### 200 - Teams for retention policy successfully retrieved.
| 필드 | 타입 | 설명 |
|---|---|---|
| policies | array | 팀 정책 목록. 각 항목은 `team_id`(string, 팀 ID), `post_duration`(integer, 메시지가 삭제되기 전 보존되는 일수) 포함 |
| total_count | integer | 전체 팀 정책 수 |

```json
{
  "policies": [
    {
      "team_id": "string",
      "post_duration": 0
    }
  ],
  "total_count": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 500 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항
- E20 라이선스가 필요하다. 라이선스가 없는 서버에서는 사용할 수 없다.

---

# 2. Get the policies which are applied to a user's channels

## 기본 정보
- **기능**: 사용자가 속한 모든 채널에 적용되는 데이터 보존 정책을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/data_retention/channel_policies`
- **인증**: Bearer Token 필요
- **권한**: 없음 (본인 조회 시. `manage_system` 권한이 있으면 타인 조회 가능)

## 설명
사용자가 속한 모든 채널에 적용되는 데이터 보존 정책 목록을 반환한다. 본인으로 로그인한 경우 자신의 정책을 조회할 수 있다. 최소 서버 버전은 5.35이며, E20 라이선스가 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"를 사용하면 현재 사용자를 가리킴 |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 정책 수 |

## Response

### 200 - Channels for retention policy successfully retrieved.
| 필드 | 타입 | 설명 |
|---|---|---|
| policies | array | 채널 정책 목록. 각 항목은 `channel_id`(string, 채널 ID), `post_duration`(integer, 메시지가 삭제되기 전 보존되는 일수) 포함 |
| total_count | integer | 전체 채널 정책 수 |

```json
{
  "policies": [
    {
      "channel_id": "string",
      "post_duration": 0
    }
  ],
  "total_count": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 500 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항
- E20 라이선스가 필요하다. 라이선스가 없는 서버에서는 사용할 수 없다.

---

# 3. Get the global data retention policy

## 기본 정보
- **기능**: 서버의 전역 데이터 보존 정책을 조회한다.
- **Endpoint**: `GET /api/v4/data_retention/policy`
- **인증**: Bearer Token 필요
- **권한**: 없음 (활성 세션만 필요)

## 설명
어떤 데이터가 삭제 대상인지, 삭제 대상 데이터 유형별 컷오프 시각이 언제인지를 포함한 현재 전역 데이터 보존 정책 상세를 반환한다. 최소 서버 버전은 4.3이며, E20 라이선스가 필요하다.

## Request

파라미터 없음.

## Response

### 200 - Global data retention policy details retrieved successfully.
| 필드 | 타입 | 설명 |
|---|---|---|
| message_deletion_enabled | boolean | 메시지에 대한 보존 정책 삭제의 전역 활성화 여부 |
| file_deletion_enabled | boolean | 파일 첨부에 대한 보존 정책 삭제의 전역 활성화 여부 |
| message_retention_cutoff | integer | 이 시각 이전의 메시지는 삭제 대상 (서버 타임스탬프) |
| file_retention_cutoff | integer | 이 시각 이전의 파일은 삭제 대상 (서버 타임스탬프) |

```json
{
  "message_deletion_enabled": true,
  "file_deletion_enabled": true,
  "message_retention_cutoff": 0,
  "file_retention_cutoff": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 500 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항
- E20 라이선스가 필요하다. 라이선스가 없는 서버에서는 사용할 수 없다.
